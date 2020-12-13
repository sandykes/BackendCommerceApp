from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "Chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "IE":
        driver = webdriver.Ie()
    else:
        driver = webdriver.firefox()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


#######Pytest HTML report#########

def pytest_configure(config):
    config._metadata['Project Name'] = 'BackedCommerceApp'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Automation Tester'] = 'Sandya K'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
