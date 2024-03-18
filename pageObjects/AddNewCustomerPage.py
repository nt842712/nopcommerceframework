import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class AddNewCustomer:
    text_Email_ID="Email"
    text_Password_ID="Password"
    text_FirstName_ID="FirstName"
    text_LastName_ID="LastName"
    radio_Male_ID="Gender_Male"
    radio_Female_ID = "Gender_Female"
    text_CompanyName_ID="Company"
    check_TaxExempt_ID="IsTaxExempt"
    text_AdminComment_ID="AdminComment"
    select_Vendor_ID="VendorId"
    check_Active_ID="Active"
    button_Save_NAME="save"
    link_CustomersMenu_XPATH="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    link_CustomersSubMenu_XPATH = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a"
    link_AddNew_XPATH="/html/body/div[3]/div[1]/form[1]/div/div/a"
    text_CustomerRoles_XPATH="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    lstitme_Administrator_XPATH="//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    lstitme_ForumModerators_XPATH="//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    lstitme_Guest_XPATH="//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitme_vendor_XPATH = "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    input_DOB_ID="DateOfBirth"
    text_newsletter_XPATH="//*[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/.."
    successmsg_XPATH="//button[@data-dismiss='alert']/.."



    def __init__(self,driver):
        self.driver=driver;

    def click_On_CustomerMenu(self):
        self.driver.find_element(By.XPATH,self.link_CustomersMenu_XPATH).click()

    def click_On_CustomerSubMenu(self):
        self.driver.find_element(By.XPATH,self.link_CustomersSubMenu_XPATH).click()

    def click_On_AddNew(self):
        self.driver.find_element(By.XPATH,self.link_AddNew_XPATH).click()

    def enteremail(self,email):
        self.driver.find_element(By.ID,self.text_Email_ID).send_keys(email)

    def enterpassword(self,password):
        self.driver.find_element(By.ID,self.text_Password_ID).send_keys(password)

    def enterFirstName(self, firstname):
        self.driver.find_element(By.ID, self.text_FirstName_ID).send_keys(firstname)

    def enterLastName(self, lastname):
        self.driver.find_element(By.ID, self.text_LastName_ID).send_keys(lastname)

    def clickMaleGender(self):
        self.driver.find_element(By.ID, self.radio_Male_ID).click()

    def clickFemaleGender(self):
        self.driver.find_element(By.ID, self.radio_Female_ID).click()

    # def setCustomerRole(self,role):
    #     self.driver.findElement(By.XPATH, self.text_CustomerRoles_XPATH).click()
    #     time.sleep(3)
    #     if role == 'Administrators':
    #         self.lstItem=self.driver.findElement(By.XPATH,self.lstitme_Administrator_XPATH)
    #     elif role == 'Registered':
    #         self.lstItem=self.driver.findElement(By.XPTH,self.lst)

    def clickSaveButton(self):
        self.driver.find_element(By.NAME, self.button_Save_NAME).click()

    def enterDOB(self,dob):
        self.driver.find_element(By.ID,self.input_DOB_ID).send_keys(dob)

    def getsuccessmsg(self):
        successmsg=self.driver.find_element(By.XPATH,self.successmsg_XPATH).text
        return successmsg






