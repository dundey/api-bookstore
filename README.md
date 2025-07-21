# API Automation Testing: Online Bookstore

## Prerequisites

- Brew (optional for MacOs)
- Python 3.9+ (ensure python3 is in your PATH)
- Git

## Setup

### Install Allure CLI (optional for local reports)

```bash
brew install allure
```

### Clone the repo
```bash
git clone https://github.com/dundey/api-bookstore
cd api-bookstore
```

### Create & activate virtualenv
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Running tests

```bash
pytest --alluredir=reports/
```

## Generating and opening Allure report
```bash
allure generate reports/ -o reports/html --clean && allure open reports/html
```

## CI/CD

The project includes GitHub Actions in .github/workflows/ci.yml, which will:

1. Run tests on push/PR
2. Generate Allure HTML report
3. Publish to GitHub Pages
4. Attach a ZIP of the report as a build artifact

For this demo/task the latest pipeline report will always be available at: https://dundey.github.io/api-bookstore/

