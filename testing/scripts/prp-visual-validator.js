#!/usr/bin/env node

/**
 * PRP Visual Validator
 * 
 * This script provides a higher-level interface for validating PRP implementations
 * with visual testing, log analysis, and iterative validation.
 * 
 * Usage: node prp-visual-validator.js <config-file>
 */

const VisualTester = require('./visual-test');
const fs = require('fs').promises;
const path = require('path');

class PRPVisualValidator {
  constructor(configPath) {
    this.configPath = configPath;
    this.config = null;
    this.results = [];
  }

  async loadConfig() {
    try {
      const configData = await fs.readFile(this.configPath, 'utf8');
      this.config = JSON.parse(configData);
      console.log(`Loaded config: ${this.configPath}`);
    } catch (error) {
      throw new Error(`Failed to load config: ${error.message}`);
    }
  }

  async validateImplementation() {
    if (!this.config) {
      throw new Error('Config not loaded. Call loadConfig() first.');
    }

    console.log('\n=== Starting PRP Visual Validation ===');
    console.log(`Feature: ${this.config.feature}`);
    console.log(`Tests: ${this.config.tests.length}`);

    for (const test of this.config.tests) {
      console.log(`\n--- Running test: ${test.name} ---`);
      
      const result = await this.runSingleTest(test);
      this.results.push(result);
      
      if (!result.success) {
        console.log(`❌ Test failed: ${test.name}`);
        if (this.config.stopOnFailure) {
          break;
        }
      } else {
        console.log(`✅ Test passed: ${test.name}`);
      }
    }

    return this.generateValidationReport();
  }

  async runSingleTest(test) {
    const tester = new VisualTester({
      name: test.name,
      viewport: test.viewport || this.config.defaultViewport,
      timeout: test.timeout || this.config.defaultTimeout,
      waitFor: test.waitFor,
      interactions: test.interactions,
      outputDir: this.config.outputDir || path.join(process.cwd(), 'testing/screenshots')
    });

    try {
      await tester.init();
      const result = await tester.navigateAndCapture(test.url);
      const report = await tester.generateReport(result);
      
      // Analyze the result
      const analysis = await this.analyzeTestResult(test, report);
      
      return {
        testName: test.name,
        success: result.success && analysis.passed,
        result,
        report,
        analysis,
        timestamp: new Date().toISOString()
      };
      
    } catch (error) {
      return {
        testName: test.name,
        success: false,
        error: error.message,
        timestamp: new Date().toISOString()
      };
    } finally {
      await tester.close();
    }
  }

  async analyzeTestResult(test, report) {
    const analysis = {
      passed: true,
      issues: [],
      warnings: []
    };

    // Check for JavaScript errors
    const jsErrors = report.logs.errors.filter(e => e.type === 'javascript');
    if (jsErrors.length > 0) {
      analysis.issues.push(`JavaScript errors detected: ${jsErrors.length}`);
      if (test.validation?.allowJSErrors !== true) {
        analysis.passed = false;
      }
    }

    // Check for network errors
    const networkErrors = report.logs.network.filter(n => n.type === 'failed');
    if (networkErrors.length > 0) {
      analysis.issues.push(`Network errors detected: ${networkErrors.length}`);
      if (test.validation?.allowNetworkErrors !== true) {
        analysis.passed = false;
      }
    }

    // Check for HTTP errors
    const httpErrors = report.logs.network.filter(n => n.type === 'error_response');
    if (httpErrors.length > 0) {
      analysis.issues.push(`HTTP errors detected: ${httpErrors.length}`);
      if (test.validation?.allowHTTPErrors !== true) {
        analysis.passed = false;
      }
    }

    // Check console warnings
    const consoleWarnings = report.logs.console.filter(c => c.type === 'warning');
    if (consoleWarnings.length > 0) {
      analysis.warnings.push(`Console warnings: ${consoleWarnings.length}`);
    }

    // Performance checks
    if (test.validation?.maxLoadTime && report.logs.performance.loadTime > test.validation.maxLoadTime) {
      analysis.issues.push(`Load time exceeded: ${report.logs.performance.loadTime}ms > ${test.validation.maxLoadTime}ms`);
      analysis.passed = false;
    }

    // Custom validation rules
    if (test.validation?.customRules) {
      for (const rule of test.validation.customRules) {
        const ruleResult = await this.evaluateCustomRule(rule, report);
        if (!ruleResult.passed) {
          analysis.issues.push(`Custom rule failed: ${rule.name} - ${ruleResult.message}`);
          analysis.passed = false;
        }
      }
    }

    return analysis;
  }

  async evaluateCustomRule(rule, report) {
    // This is a placeholder for custom validation logic
    // In a real implementation, you might evaluate JavaScript expressions
    // against the report data or perform other custom checks
    
    switch (rule.type) {
      case 'console_contains':
        const found = report.logs.console.some(log => 
          log.text.includes(rule.value)
        );
        return {
          passed: rule.shouldExist ? found : !found,
          message: `Console ${rule.shouldExist ? 'should' : 'should not'} contain: ${rule.value}`
        };
      
      case 'no_errors_containing':
        const hasError = report.logs.errors.some(error => 
          error.message.includes(rule.value)
        );
        return {
          passed: !hasError,
          message: `Should not have errors containing: ${rule.value}`
        };
      
      default:
        return { passed: true, message: 'Unknown rule type' };
    }
  }

  async generateValidationReport() {
    const summary = {
      totalTests: this.results.length,
      passedTests: this.results.filter(r => r.success).length,
      failedTests: this.results.filter(r => !r.success).length,
      timestamp: new Date().toISOString()
    };

    const fullReport = {
      config: this.config,
      summary,
      results: this.results
    };

    // Save report
    const reportPath = path.join(
      this.config.outputDir || path.join(process.cwd(), 'testing/screenshots'),
      `prp-validation-report-${new Date().toISOString().replace(/[:.]/g, '-')}.json`
    );

    await fs.writeFile(reportPath, JSON.stringify(fullReport, null, 2));
    console.log(`\n=== Validation Report ===`);
    console.log(`Total Tests: ${summary.totalTests}`);
    console.log(`Passed: ${summary.passedTests}`);
    console.log(`Failed: ${summary.failedTests}`);
    console.log(`Report saved: ${reportPath}`);

    return fullReport;
  }
}

// CLI Interface
async function main() {
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    console.error('Usage: node prp-visual-validator.js <config-file>');
    console.error('\nExample config file:');
    console.error(JSON.stringify({
      feature: "User Authentication",
      outputDir: "../screenshots",
      defaultViewport: { width: 1920, height: 1080 },
      defaultTimeout: 30000,
      stopOnFailure: false,
      tests: [
        {
          name: "login-page",
          url: "http://localhost:3000/login",
          waitFor: "#login-form",
          validation: {
            allowJSErrors: false,
            maxLoadTime: 5000
          }
        }
      ]
    }, null, 2));
    process.exit(1);
  }
  
  const configPath = args[0];
  const validator = new PRPVisualValidator(configPath);
  
  try {
    await validator.loadConfig();
    const report = await validator.validateImplementation();
    
    if (report.summary.failedTests > 0) {
      console.error(`\n❌ Validation failed: ${report.summary.failedTests} test(s) failed`);
      process.exit(1);
    } else {
      console.log(`\n✅ All tests passed!`);
    }
    
  } catch (error) {
    console.error('Validation failed:', error.message);
    process.exit(1);
  }
}

// Export for programmatic use
module.exports = PRPVisualValidator;

// Run if called directly
if (require.main === module) {
  main().catch(console.error);
}
