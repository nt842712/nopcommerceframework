


import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LoginGen

class Test_002_DDT_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    path=""

    def test_Login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        self.driver.save_screenshot(
            "/Users/nareshntalesha/PycharmProjects/nopcommerceframework/Screenshots/test_Login.png")
        assert act_title == "Dashboard / nopCommerce administration"
        self.driver.close()


