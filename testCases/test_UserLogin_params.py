import time
# test_funtionalityname_subfuntionalityname_number
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from pageObjects.LoginPage import LoginClass
from utilities.Logger import LoggenClass
from utilities.readconfigfile import Readconfig


class Test_Login_Params:
    log = LoggenClass.log_generator()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_user_login_params_004(self, setup, DataForLogin):
        self.log.info("Test_case test_user_login_params_004 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email - " + DataForLogin[0])
        self.lp.Enter_Email(DataForLogin[0])
        self.log.info("Entering Password - " + DataForLogin[1])
        self.lp.Enter_Password(DataForLogin[1])
        self.log.info("Click on login button")
        self.lp.Click_Login()
        TestCase_Status_List = []
        if self.lp.Verify_Login_Stauts() == "Login Pass":  # actual Result # login hogaya
            self.log.info("Login Pass")
            if DataForLogin[2] == "Pass":  # expected result
                self.log.info("Expected Pass")
                TestCase_Status_List.append("Pass")  # updating the Status List
                self.log.info("Taking screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_login_params_004_pass.png")
                self.log.info("Click on Logout button")
                self.lp.Click_Logout()
            elif DataForLogin[2] == "Fail":
                self.log.info("Expected Fail")
                TestCase_Status_List.append("Fail")
                self.log.info("Taking screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Pass",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_login_params_004_pass.png")
                self.log.info("Click on Logout button")
                self.lp.Click_Logout()
        elif self.lp.Verify_Login_Stauts() == "Login Fail":  # login nhi hua
            self.log.info("Login Fail")
            if DataForLogin[2] == "Fail":
                self.log.info("Expected Fail")
                TestCase_Status_List.append("Pass")
            elif DataForLogin[2] == "Pass":
                self.log.info("Expected Pass")
                TestCase_Status_List.append("Fail")
                self.log.info("Taking screenshot")
                allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_params_004-Fail",
                              attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("..\\Screenshots\\test_user_login_params_004_fail.png")
        print(TestCase_Status_List)
        if "Pass" in TestCase_Status_List:
            self.log.info("Test_case test_user_login_params_004 is Passed")
            assert True
        else:
            self.log.info("Test_case test_user_login_params_004 is Failed")
            assert False
        self.log.info("Test_case test_user_login_params_004 is Completed")

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
