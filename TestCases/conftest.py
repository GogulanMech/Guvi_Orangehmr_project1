import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# HTML-Report
def pytest_configure(config):
    config._metadata["project Name"] = "Orange HRM"
    config._metadata["Module"] = "Add Employee"
    config._metadata["Tester"] = "Gogulan Murugesan"

