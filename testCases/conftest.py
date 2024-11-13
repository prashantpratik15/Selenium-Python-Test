import pytest
from selenium import webdriver

@pytest.fixture()
def driver(browser):  # Use 'driver' as the fixture name
    option= webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    if browser == 'chrome':
        driver = webdriver.Chrome(options=option)
        print("Launching Chrome browser...........")
        #driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser..........")
    elif browser == 'edge':
        driver = webdriver.Edge()  # Correct Edge initialization
        print("Launching Edge browser..........")
    else:
        driver = webdriver.Chrome()  # Default to Chrome if no valid browser is specified
    return driver
    #yield driver  # Yield the driver instance for use in tests
    #driver.quit()  # Quit the driver after the test is done
    

def pytest_addoption(parser):
    parser.addoption("--browser", default='chrome', help="Choose browser: chrome, firefox, edge")

@pytest.fixture()
def browser(request):  
    return request.config.getoption("--browser")


#scope='function'
#scope='session'