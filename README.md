# Test Reporting with Allure

This project supports **Allure Report** for rich and user-friendly test reporting, including:

- passed / failed test statistics
- execution details
- test steps
- a clean HTML report interface

---

## Local Setup

### Prerequisites

Before running Allure locally, make sure the following tools are installed:

- **Java 8 or higher**
- **Scoop**
- **Allure CLI**

---

## Installation

### 1. Install Java

Make sure Java is installed and available in `PATH`.

```bash

java --version
```

### 2. Install Scoop

Run the following commands in PowerShell:

```bash

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
```

### 3. Install Allure CLI

```bash

scoop install allure
```

### 4. Verify installation

```bash

allure --version
```

---
## Generate Allure Report Locally
### Step 1: Run tests and save results

```bash

pytest --alluredir=allure-results
```

### Step 2: Open the report

```bash

allure serve allure-results
```
This command will generate the report and automatically open it in your browser.

---

### View Allure Report from GitHub Actions
The project also generates an Allure HTML report in GitHub Actions.


## How to open it

1. Open the required workflow run in GitHub Actions
2. Find the step called Upload Allure HTML report
3. Download the generated artifact
4. Extract it to any folder on your machine
5. Open PowerShell inside the extracted folder
6. Run:
```bash

allure open
```

---

### Troubleshooting

`allure` is not recognized

Restart your terminal or IDE and check again:
```bash

allure --version
```

### Blank or gray report page
Do not open `index.html` directly from the archive.
Extract the full report folder first, then run:
```bash

allure open
```
