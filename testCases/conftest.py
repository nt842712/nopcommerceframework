from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == "firefox":
        driver =  webdriver.Firefox()
    elif browser == "safari":
        driver =  webdriver.Safari()
        driver.maximize_window()
    return driver
    #yield
    #driver.close()


def pytest_addoption(parser):    #  This will get the value from CLI/Hook
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):    #  this will retunr the browser value to setup method
    return request.config.getoption("--browser")


#########Generate HTML report  #################
#
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop commerce'
#     config.metadata['Module Name'] = 'Customers'
#     config.metadata['Tester'] = 'Naresh'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins",None)


# @pytest.fixture()
# def setup(request):
#     browser_name = request.config.getoption("browser_name")
#     if browser_name == "chrome":
#         #chrom_options = webdriver.ChromeOptions()
#         #chrom_options.add_argument("--start-maximized")
#         #options = chrom_options
#         driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         driver = webdriver.Firefox()
#     #driver.get("https://rahulshettyacademy.com/angularpractice")
#     #request.cls.driver = driver
#     return driver
#     #yield
#     #driver.close()
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )