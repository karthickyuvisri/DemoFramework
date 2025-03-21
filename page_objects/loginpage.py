from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from base_pages.base import Base
from utilities.config_reader import ConfigReader


class LoginPage(Base):
    __USERNAME_LOCATOR = (By.ID, "user-name")
    __PASSWORD_LOCATOR = (By.ID, "password")
    __LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    __LOGIN_CONFIG="baseconfig.ini"

    def __init__(self, driver):
        super().__init__(driver)
        self.config_reader=ConfigReader(self.__LOGIN_CONFIG)


    def enter_username(self,username):
        self.enter_text(self.__USERNAME_LOCATOR,username)

    def enter_password(self,password):
        self.enter_text(self.__PASSWORD_LOCATOR,password)

    def click_login_button(self):
        self.click_element(self.__LOGIN_BUTTON_LOCATOR)

    def login_user(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()