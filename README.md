# API Automation Testing: Online Bookstore

## Prerequisites
- Python 3.9+ (ensure `python3` is installed)
- Git
- Allure

## Setup (MacOS/Linux)
```bash
# Create a virtual environment
python3 -m venv .venv
# Activate it
source .venv/bin/activate
# Install project dependencies
pip3 install -r requirements.txt

## Running tests
```bash
pytest --alluredir=reports/
```

## Generating report

Temporery report:
```bash
allure serve reports/
```

Permanent report:
```bash
allure generate reports/ -o reports/html --clean
allure open reports/html
```

## CI/CD

GitHub Actions runs tests on push/PR, generates a permanent Allure HTML report, and uploads it as an artifact.