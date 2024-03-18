import random
import string
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.AddNewCustomerPage import AddNewCustomer
from utilities.readProperties import ReadConfig
class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    #path = ""

    @pytest.mark.regression
    def test_addcustomer(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login = Login(self.driver)
        self.login.setUserName(self.username)
        self.login.setPassword(self.password)
        self.login.clickLogin()
        time.sleep(5)

        self.addcust = AddNewCustomer(self.driver)
        self.addcust.click_On_CustomerMenu()
        time.sleep(5)
        self.addcust.click_On_CustomerSubMenu()
        self.addcust.click_On_AddNew()
        self.email=random_generator()+"@gmail.com"
        self.addcust.enteremail(self.email)
        self.addcust.enterFirstName("Test")
        self.addcust.enterLastName("Testing")
        self.addcust.enterpassword("Pass@123")

        self.addcust.clickMaleGender()


        self.addcust.enterDOB("06/08/1993")

        self.addcust.clickSaveButton()
        #
        success=self.addcust.getsuccessmsg()
        print(success)
        print(type(success))

        assert "customer has been added successfully."  in self.addcust.getsuccessmsg()
        time.sleep(5)


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for  x in range(size))


#print(random_generator())

