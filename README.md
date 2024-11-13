**This project automates the process of uploading files to a web application using Selenium WebDriver, and validates the behavior of file uploads with Pytest.**

The test suite includes:
1. Uploading valid PDF files and verifying the file count on the web page.
2. Uploading an invalid file format (JPEG) and verifying the error message (toast notification).

## Sample Python Selenium Pytest Framework

The tech stack used in this project are:
1. **Python** as the programming language for writing test code
2. **Pytest** as the framework
3. **PIP3** as the build tool
4. **VSCode** as the preferred IDE for writing python code.

#### Getting Started
Setup your machine.
1. Python > 3.7 
2. Install VSCode & open the repo
3. On Terminal, navigate to repo and run following commands
    a. Create Virtual Env ```python3 -m venv behavex-env```
    b. Activate Virtual Env ```source behavex-env/bin/activate```
    c. Install Packages ```pip3 install -r requirements.txt```

#### Running tests
* Run tests in chrome: ```python3 -m pytest testCases/add_update_pdf_and_validate.py -v -s   --browser=chrome```
* Run tests in firefox: ```python3 -m pytest testCases/add_update_pdf_and_validate.py -v -s   --browser=firefox```
* Run without browser parameter , default is chrome: ```python3 -m pytest testCases/add_update_pdf_and_validate.py -v -s ```

#### Report
* Report will be found here: ```/output/report.html```
---

### Tests
1. **[TestCase-1]:** Upload Two PDF Files and validate count
2. **[TestCase-2]:** Upload an Invalid File Format and validate error message
