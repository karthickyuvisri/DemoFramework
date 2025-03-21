from selenium import webdriver
import pytest
from selenium.webdriver.support.events import EventFiringWebDriver
from utilities.listeners import Listener


@pytest.fixture(scope="class")
def init_driver(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver=EventFiringWebDriver(driver,Listener())
    request.cls.driver=driver
    yield
    driver.close()