#!/usr/bin/env node

/**
 * Visual Testing Script for PRP Validation
 * 
 * This script captures screenshots, console logs, and network errors
 * for visual validation of implemented features.
 * 
 * Usage: node visual-test.js <url> [options]
 * 
 * Options:
 *   --output-dir <dir>    Directory to save screenshots (default: ../screenshots)
 *   --timeout <ms>        Page load timeout in milliseconds (default: 30000)
 *   --viewport <WxH>      Viewport size (default: 1920x1080)
 *   --wait-for <selector> Wait for specific element before screenshot
 *   --interactions <file> JSON file with interactions to perform
 *   --name <name>         Custom name for the test run
 */

const puppeteer = require('puppeteer');
const fs = require('fs').promises;
const path = require('path');

class VisualTester {
  constructor(options = {}) {
    this.options = {
      outputDir: options.outputDir || path.join(process.cwd(), 'testing/screenshots'),
      timeout: options.timeout || 30000,
      viewport: options.viewport || { width: 1920, height: 1080 },
      waitFor: options.waitFor,
      interactions: options.interactions,
      name: options.name || 'test',
      ...options
    };
    
    this.logs = {
      console: [],
      network: [],
      errors: [],
      performance: {}
    };
  }

  async init() {
    // Ensure output directory exists
    await fs.mkdir(this.options.outputDir, { recursive: true });
    
    // Launch browser
    this.browser = await puppeteer.launch({
      headless: 'new',
      args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--no-first-run',
        '--no-zygote',
        '--disable-gpu'
      ]
    });
    
    this.page = await this.browser.newPage();
    await this.page.setViewport(this.options.viewport);
    
    // Set up logging
    this.setupLogging();
  }

  setupLogging() {
    // Console logs
    this.page.on('console', (msg) => {
      this.logs.console.push({
        type: msg.type(),
        text: msg.text(),
        timestamp: new Date().toISOString()
      });
    });

    // Network errors
    this.page.on('requestfailed', (request) => {
      this.logs.network.push({
        type: 'failed',
        url: request.url(),
        method: request.method(),
        failure: request.failure()?.errorText,
        timestamp: new Date().toISOString()
      });
    });

    // JavaScript errors
    this.page.on('pageerror', (error) => {
      this.logs.errors.push({
        type: 'javascript',
        message: error.message,
        stack: error.stack,
        timestamp: new Date().toISOString()
      });
    });

    // Response errors
    this.page.on('response', (response) => {
      if (response.status() >= 400) {
        this.logs.network.push({
          type: 'error_response',
          url: response.url(),
          status: response.status(),
          statusText: response.statusText(),
          timestamp: new Date().toISOString()
        });
      }
    });
  }

  async navigateAndCapture(url) {
    const startTime = Date.now();
    
    try {
      // Navigate to URL
      console.log(`Navigating to: ${url}`);
      await this.page.goto(url, { 
        waitUntil: 'networkidle2', 
        timeout: this.options.timeout 
      });

      // Wait for specific element if specified
      if (this.options.waitFor) {
        console.log(`Waiting for element: ${this.options.waitFor}`);
        await this.page.waitForSelector(this.options.waitFor, { 
          timeout: this.options.timeout 
        });
      }

      // Perform interactions if specified
      if (this.options.interactions) {
        await this.performInteractions();
      }

      // Capture performance metrics
      const performanceMetrics = await this.page.metrics();
      this.logs.performance = {
        ...performanceMetrics,
        loadTime: Date.now() - startTime,
        timestamp: new Date().toISOString()
      };

      // Take screenshot
      const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
      const screenshotPath = path.join(
        this.options.outputDir, 
        `${this.options.name}-${timestamp}.png`
      );
      
      await this.page.screenshot({ 
        path: screenshotPath, 
        fullPage: true 
      });
      
      console.log(`Screenshot saved: ${screenshotPath}`);
      
      return {
        success: true,
        screenshotPath,
        url,
        timestamp,
        logs: this.logs
      };

    } catch (error) {
      this.logs.errors.push({
        type: 'navigation',
        message: error.message,
        stack: error.stack,
        timestamp: new Date().toISOString()
      });
      
      return {
        success: false,
        error: error.message,
        url,
        timestamp: new Date().toISOString(),
        logs: this.logs
      };
    }
  }

  async performInteractions() {
    if (!this.options.interactions) return;
    
    let interactions;
    if (typeof this.options.interactions === 'string') {
      const interactionsData = await fs.readFile(this.options.interactions, 'utf8');
      interactions = JSON.parse(interactionsData);
    } else {
      interactions = this.options.interactions;
    }

    for (const interaction of interactions) {
      try {
        console.log(`Performing interaction: ${interaction.type}`);
        
        switch (interaction.type) {
          case 'click':
            await this.page.click(interaction.selector);
            break;
          case 'type':
            await this.page.type(interaction.selector, interaction.text);
            break;
          case 'wait':
            await this.page.waitForTimeout(interaction.duration);
            break;
          case 'waitForSelector':
            await this.page.waitForSelector(interaction.selector);
            break;
          case 'scroll':
            await this.page.evaluate((y) => window.scrollTo(0, y), interaction.y || 0);
            break;
        }
        
        // Wait a bit after each interaction
        await this.page.waitForTimeout(500);
        
      } catch (error) {
        this.logs.errors.push({
          type: 'interaction',
          interaction: interaction.type,
          message: error.message,
          timestamp: new Date().toISOString()
        });
      }
    }
  }

  async generateReport(result) {
    const reportPath = path.join(
      this.options.outputDir,
      `report-${result.timestamp}.json`
    );
    
    const report = {
      testRun: {
        name: this.options.name,
        url: result.url,
        timestamp: result.timestamp,
        success: result.success,
        error: result.error
      },
      screenshot: result.screenshotPath,
      logs: result.logs,
      summary: {
        consoleMessages: result.logs.console.length,
        networkErrors: result.logs.network.filter(n => n.type === 'failed').length,
        jsErrors: result.logs.errors.filter(e => e.type === 'javascript').length,
        httpErrors: result.logs.network.filter(n => n.type === 'error_response').length
      }
    };
    
    await fs.writeFile(reportPath, JSON.stringify(report, null, 2));
    console.log(`Report saved: ${reportPath}`);
    
    return report;
  }

  async close() {
    if (this.browser) {
      await this.browser.close();
    }
  }
}

// CLI Interface
async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.error('Usage: node visual-test.js <url> [options]');
    process.exit(1);
  }
  
  const url = args[0];
  const options = {};
  
  // Parse command line options
  for (let i = 1; i < args.length; i += 2) {
    const flag = args[i];
    const value = args[i + 1];
    
    switch (flag) {
      case '--output-dir':
        options.outputDir = value;
        break;
      case '--timeout':
        options.timeout = parseInt(value);
        break;
      case '--viewport':
        const [width, height] = value.split('x').map(Number);
        options.viewport = { width, height };
        break;
      case '--wait-for':
        options.waitFor = value;
        break;
      case '--interactions':
        options.interactions = value;
        break;
      case '--name':
        options.name = value;
        break;
    }
  }
  
  const tester = new VisualTester(options);
  
  try {
    await tester.init();
    const result = await tester.navigateAndCapture(url);
    const report = await tester.generateReport(result);
    
    // Print summary
    console.log('\n=== Test Summary ===');
    console.log(`Success: ${result.success}`);
    console.log(`Console Messages: ${report.summary.consoleMessages}`);
    console.log(`Network Errors: ${report.summary.networkErrors}`);
    console.log(`JavaScript Errors: ${report.summary.jsErrors}`);
    console.log(`HTTP Errors: ${report.summary.httpErrors}`);
    
    if (!result.success) {
      console.error(`Error: ${result.error}`);
      process.exit(1);
    }
    
  } catch (error) {
    console.error('Test failed:', error.message);
    process.exit(1);
  } finally {
    await tester.close();
  }
}

// Export for programmatic use
module.exports = VisualTester;

// Run if called directly
if (require.main === module) {
  main().catch(console.error);
}
