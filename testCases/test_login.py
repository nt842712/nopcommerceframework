import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LoginGen


class Test_001_Login:
    baseURL =ReadConfig.getApplicationURL()
    username=ReadConfig.getUserName()
    password=ReadConfig.getPassword()

    logg=LoginGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self,setup):
        self.logg.info("*********Test_001_Login*********")
        self.driver=setup
        print(self.baseURL)
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.save_screenshot("/Users/nareshntalesha/PycharmProjects/nopcommerceframework/Screenshots/test_homePageTitle.png")
        assert act_title == "Your store. Login"
        self.driver.close()

    @pytest.mark.sanity
    def test_Login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login=Login(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        self.driver.save_screenshot(
            "/Users/nareshntalesha/PycharmProjects/nopcommerceframework/Screenshots/test_Login.png")
        assert act_title == "Dashboard / nopCommerce administration"
        self.driver.close()


