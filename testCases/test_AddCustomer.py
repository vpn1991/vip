import random
import string
import time

import allure
import pytest
from selenium import webdriver

from pageObjects.AddCustomerPage import AddCustomerClass
from pageObjects.LoginPage import LoginClass
from utilities.Logger import LoggenClass
from utilities.readconfigfile import Readconfig


class Test_Add_Customer:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    @allure.story("Customer")
    @allure.title("Add Customer TestCase")
    @allure.link("https://admin-demo.nopcommerce.com/")
    @allure.severity("Low")
    def test_addCustomer_003(self, setup):
        self.log.info("Test_case test_addCustomer_003 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email - " + self.Email)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Password - " + self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Click on login button")
        self.lp.Click_Login()
        self.ac = AddCustomerClass(self.driver)
        self.log.info("Click on Customer Menu")
        self.ac.Click_Customers_Menu()
        self.log.info("Click on Customer Sub Menu")
        self.ac.Click_Customers_SubMenu()
        self.log.info("Click on Add Customer")
        self.ac.Click_AddNewCustomer()
        email = Generate_Email()
        self.log.info("Email-->" + email)
        self.log.info("Enter Email")
        self.ac.Enter_Email(email)
        self.log.info("Enter Password")
        self.ac.Enter_Password("Credence@101")
        self.log.info("Enter First Name")
        self.ac.Enter_FirstName("Tushar")
        self.log.info("Enter Last Name")
        self.ac.Enter_LastName("Kathalkar")
        self.log.info("Select Gender")
        self.ac.Select_Gender("Male")
        self.log.info("Enter Date Of Birth")
        self.ac.Enter_DOB("12/02/1990")
        self.log.info("Enter Company Name")
        self.ac.Enter_CompanyName("Credence")
        self.log.info("Click on is tax exempt CheckBox")
        self.ac.CheckBox_Tax()
        self.log.info("Click on NewsLetter")
        self.ac.Click_NewsLetter()
        self.log.info("Click on NewsLetter List")
        self.ac.Click_NewsLetter_list()
        self.log.info("Select Value for Manager of vendor")
        self.ac.DropDown_Manager_of_vendor("Vendor 1")
        self.log.info("Click on Active Checkbox")
        self.ac.Click_CheckBox_Active()
        self.log.info("Enter Comment")
        self.ac.Enter_Comment("Credence is Best")
        self.log.info("Click Save Button")
        self.ac.Click_SaveButton()
        # time.sleep(5)
        if self.ac.Validate_Success_Message() == "pass":
            self.log.info("Test_case test_addCustomer_003 is passed")
            self.driver.save_screenshot("..\\Screenshots\\test_addCustomer_003_pass.png")
            assert True
        else:
            self.driver.save_screenshot("..\\Screenshots\\test_addCustomer_003_fail.png")
            self.log.info("Test_case test_addCustomer_003 is Failed")
            assert False



def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))  # random 4 char lower case e.g gfhd
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])  #
    return f"{username}@{domain}"  # random 4 char + domain