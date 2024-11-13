This project automates the process of uploading files to a web application using Selenium WebDriver, and validates the behavior of file uploads with Pytest.

The test suite includes:
Uploading valid PDF files and verifying the file count on the web page.
Uploading an invalid file format (JPEG) and verifying the error message (toast notification).

Prerequisites:

Before running the tests, make sure you have the following software installed:

Python (version 3.7 or above)
Google Chrome or Firefox or Microsoft Edge (depending on which browser you want to use for testing)
ChromeDriver, geckodriver, or EdgeDriver (depending on the browser) - This is necessary for Selenium to interact with the browser.


Install the required Python packages using pip/ pip3:
pip install -r requirements.txt   --- for pip
pip3 install -r requirements.txt  --- for pip3


Setting up the WebDriver
Selenium requires a WebDriver to interface with the browser. Ensure that you have the appropriate WebDriver installed and available in your system's PATH.

For Chrome: Download ChromeDriver
For Firefox: Download geckodriver




Running the Tests
1. Run Tests on a Specific Browser

To run the tests on Chrome:

    'pytest testCases/add_update_pdf_and_validate.py -v -s  --browser=chrome'                          ----- for pip
    'python3 -m pytest testCases/add_update_pdf_and_validate.py -v -s   --browser=chrome'              --- for pip3


To run the tests on Firefox:

    'pytest testCases/add_update_pdf_and_validate.py -v -s  --browser=firefox'                          ----- for pip
    'python3 -m pytest testCases/add_update_pdf_and_validate.py -v -s   --browser=firefox'              --- for pip3


Default it will run on chrome

    'pytest testCases/add_update_pdf_and_validate.py -v -s'                          ----- for pip
    'python3 -m pytest testCases/add_update_pdf_and_validate.py -v -s'              --- for pip3







File Upload Test Logic:

Test 1: Upload Two Valid PDF Files
    Objective: Upload two valid PDF files (test1.pdf and test2.pdf) and verify their visibility on the screen.
    Steps:
        Navigate to the website (https://www.ilovepdf.com/merge_pdf).
        Upload both PDF files.
        Verify that both files are displayed correctly and the count of uploaded files is 2.

Test 2: Upload an Invalid File Format
    Objective: Upload an invalid file format (JPEG) and verify the error message displayed (toast notification).
    Steps:
        Navigate to the website.
        Try uploading a .jpeg file.
        Verify that the toaster notification appears with the message: "Sorry, this extension is not allowed".


