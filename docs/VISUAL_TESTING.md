# Visual Testing Documentation

This document describes the visual testing system integrated into the PRP (Product Requirements and Planning) workflow.

## Overview

The visual testing system provides automated screenshot capture, console log monitoring, network error detection, and performance analysis for validating PRP implementations. All dependencies are managed from the root `package.json`.

## Setup

### Prerequisites
- Node.js 16+ 
- npm or yarn

### Installation
```bash
# From project root
npm install

# Or install only visual testing dependencies
npm run setup-testing
```

This installs Puppeteer and other testing dependencies defined in the root `package.json`.

## Usage

All commands should be run from the **project root directory**.

### Quick Start

```bash
# Basic screenshot test
npm run visual-test http://localhost:3000

# PRP validation with config
npm run prp-validate testing/example-validation-config.json
```

### Direct Script Usage

#### Basic Screenshot Test
```bash
node testing/scripts/visual-test.js http://localhost:3000
```

#### Advanced Options
```bash
node testing/scripts/visual-test.js http://localhost:3000 \
  --name "homepage-test" \
  --viewport 1920x1080 \
  --wait-for ".main-content" \
  --timeout 30000 \
  --output-dir testing/screenshots
```

#### With User Interactions
Create an interactions file (e.g., `testing/interactions/login-flow.json`):
```json
[
  { "type": "click", "selector": "#login-button" },
  { "type": "type", "selector": "#username", "text": "testuser" },
  { "type": "type", "selector": "#password", "text": "testpass" },
  { "type": "click", "selector": "#submit" },
  { "type": "waitForSelector", "selector": ".dashboard" }
]
```

Then run:
```bash
node testing/scripts/visual-test.js http://localhost:3000 \
  --interactions testing/interactions/login-flow.json \
  --name "login-flow"
```

### PRP Validation

For comprehensive PRP validation, use the validator script:

```bash
node testing/scripts/prp-visual-validator.js testing/validation-configs/my-feature.json
```

#### Validation Configuration

Create a validation config file (see `testing/example-validation-config.json`):

```json
{
  "feature": "User Authentication Feature",
  "outputDir": "testing/screenshots",
  "defaultViewport": { "width": 1920, "height": 1080 },
  "defaultTimeout": 30000,
  "stopOnFailure": false,
  "tests": [
    {
      "name": "login-page-load",
      "url": "http://localhost:3000/login",
      "waitFor": "#login-form",
      "validation": {
        "allowJSErrors": false,
        "allowNetworkErrors": false,
        "maxLoadTime": 5000,
        "customRules": [
          {
            "type": "console_contains",
            "value": "Login form initialized",
            "shouldExist": true,
            "name": "Login initialization message"
          }
        ]
      }
    },
    {
      "name": "login-flow",
      "url": "http://localhost:3000/login",
      "interactions": [
        { "type": "type", "selector": "#username", "text": "testuser" },
        { "type": "type", "selector": "#password", "text": "testpass" },
        { "type": "click", "selector": "#login-btn" },
        { "type": "waitForSelector", "selector": ".dashboard" }
      ],
      "validation": {
        "allowJSErrors": false,
        "maxLoadTime": 3000
      }
    }
  ]
}
```

## Integration with PRP Workflow

### In PRP Generation (`generate-prp.md`)

Visual testing is integrated into the validation gates:

```bash
# Visual Testing (if web interface)
cd testing/scripts && npm install
node visual-test.js http://localhost:3000 --name "feature-validation"
```

**Note:** Since all dependencies are now in the root, the actual command becomes:
```bash
# Visual Testing (if web interface)  
npm run visual-test http://localhost:3000 --name "feature-validation"
```

### In PRP Execution (`execute-prp.md`)

Visual testing occurs in **Step 5** of the execution process:

1. Run visual testing script to capture screenshots and logs
2. Analyze screenshot for visual correctness
3. Review console logs and network errors
4. Compare against expected behavior
5. Make adjustments if visual validation fails
6. Re-test until visual validation passes

## Output and Reports

### File Structure
```
testing/
├── screenshots/           # Generated screenshots
├── scripts/              # Testing scripts
├── interactions/         # Interaction definitions
├── validation-configs/   # Validation configurations
└── example-validation-config.json
```

### Generated Files

- **Screenshots**: `testing/screenshots/{name}-{timestamp}.png`
- **Reports**: `testing/screenshots/report-{timestamp}.json`
- **Validation Reports**: `testing/screenshots/prp-validation-report-{timestamp}.json`

### Report Contents

Each report includes:
- Test execution summary
- Screenshot paths
- Console logs (info, warn, error)
- Network requests/failures
- JavaScript errors
- Performance metrics
- Custom validation results

## Available Scripts (from root)

| Script | Command | Description |
|--------|---------|-------------|
| `npm run visual-test` | `node testing/scripts/visual-test.js` | Basic visual testing |
| `npm run prp-validate` | `node testing/scripts/prp-visual-validator.js` | PRP validation |
| `npm run setup-testing` | `npm install` | Install testing dependencies |
| `npm run test:visual` | Alias for `visual-test` | Visual testing alias |
| `npm run test:prp` | Alias for `prp-validate` | PRP validation alias |

## Interaction Types

| Type | Parameters | Description |
|------|------------|-------------|
| `click` | `selector` | Click an element |
| `type` | `selector`, `text` | Type text into input |
| `wait` | `duration` | Wait for specified milliseconds |
| `waitForSelector` | `selector` | Wait for element to appear |
| `scroll` | `y` | Scroll to Y position |

## Validation Rules

### Built-in Rules
- `allowJSErrors`: Allow JavaScript errors (default: false)
- `allowNetworkErrors`: Allow network failures (default: false)
- `allowHTTPErrors`: Allow HTTP error responses (default: false)
- `maxLoadTime`: Maximum page load time in ms

### Custom Rules
- `console_contains`: Check if console contains specific text
- `no_errors_containing`: Ensure no errors contain specific text

## Troubleshooting

### Common Issues

1. **Puppeteer installation fails**
   ```bash
   # Try installing with specific flags
   npm install puppeteer --unsafe-perm=true --allow-root
   ```

2. **Screenshots not saving**
   - Ensure `testing/screenshots` directory exists
   - Check file permissions
   - Verify output path in config

3. **Timeout errors**
   - Increase timeout values in config
   - Check if target URL is accessible
   - Verify waitFor selectors exist

4. **Network errors in tests**
   - Check if local server is running
   - Verify URL accessibility
   - Review network logs in report

### Debug Mode

Add debug logging to visual tests:
```bash
DEBUG=puppeteer:* node testing/scripts/visual-test.js http://localhost:3000
```

## Best Practices

1. **Always run from project root** - All paths are relative to root
2. **Use descriptive test names** - Helps identify screenshots and reports
3. **Set appropriate timeouts** - Balance between reliability and speed
4. **Validate incrementally** - Test individual components before full flows
5. **Review reports** - Don't just check pass/fail, examine logs
6. **Version control configs** - Keep validation configs in git
7. **Clean up old screenshots** - Implement cleanup strategy for CI/CD

## CI/CD Integration

Example GitHub Actions workflow:
```yaml
- name: Install dependencies
  run: npm install

- name: Start application
  run: npm start &
  
- name: Wait for server
  run: sleep 10

- name: Run visual tests
  run: npm run prp-validate testing/validation-configs/ci.json
```

## Contributing

When adding new visual testing features:
1. Update this documentation
2. Add example configurations
3. Include tests for new functionality
4. Update PRP command references
