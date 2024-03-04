import time
# test_funtionalityname_subfuntionalityname_number
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from pageObjects.LoginPage import LoginClass
from utilities.Logger import LoggenClass
from utilities.readconfigfile import Readconfig


class Test_Login:
    Email = Readconfig.getEmail()
    Password = Readconfig.getPassword()
    log = LoggenClass.log_generator()

    @allure.feature('page_title')
    @allure.story('Verifying the page title')
    @allure.issue('ABC-123')
    @allure.link(' https://admin-demo.nopcommerce.com/',name='Orange HRM Website')
    @allure.title('NonCom - Test page_title')
    @allure.description('My test description')
    @allure.link('https://www.example.com')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.sanity
    def test_verify_url_001(self, setup):
        self.log.info("Test_case test_verify_url_001 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.log.info("Page Title is --> " + self.driver.title)
        #print(self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("Test_Case test_verify_url_001 is passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_url_001-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_pass.png")
            assert True
        else:
            self.log.info("Test_Case test_verify_url_001 is failed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_verify_url_001-Fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_fail.png")
            assert False
        self.log.info("Test_case test_verify_url_001 is Completed")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_user_login_002(self, setup):
        self.log.info("Test_case test_user_login_002 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email - " + self.Email)
        self.lp.Enter_Email(self.Email)
        self.log.info("Entering Password - " + self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Click on login button")
        self.lp.Click_Login()
        if self.lp.Verify_Login_Stauts() == "Login Pass":
            self.log.info("Test_case test_user_login_002 is passed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Pass",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_pass.png")
            self.log.info("Click on Logout button")
            self.lp.Click_Logout()
            assert True
        else:
            self.log.info("Test_case test_user_login_002 is Failed")
            self.log.info("Taking screenshot")
            allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Fail",
                          attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_fail.png")
            assert False
        self.log.info("Test_case test_user_login_002 is Completed")

# pytest -v -n=2 --html=HtmlReports/myreport.html
# pytest -v -n=2 --html=HtmlReports/myreport.html -m sanity -p
# pytest -v -n=2 -m sanity --html=HtmlReports/myreport.html --alluredir="D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jan 24\nopcom_Pytest\AllureReports" --browser firefox  -p no:warnings
# pytest -v -n=2 -m sanity --alluredir="D:\Credence Class Notes\CredenceBatches\Credence_Automation_Jan 24\nopcom_Pytest\AllureReports" --browser firefox  -p no:warnings
# allure serve "allure_report_folder_path" # To generate report

# test_emp_add
# test_emp_edit
# test_emp_search
#
# -k test_emp
