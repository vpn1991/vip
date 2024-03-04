import time
# test_funtionalityname_subfuntionalityname_number
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from pageObjects.LoginPage import LoginClass
from utilities import ExcelMethods
from utilities.Logger import LoggenClass
from utilities.readconfigfile import Readconfig


class Test_Login_DDT:
    log = LoggenClass.log_generator()
    Excel_File_Path = "C:\\Users\\vipin\\Desktop\\Automation (tushar sir)\\nopcom_Pytest\\testCases\\Test_Data\\Test_Data.xlsx"

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_user_login_DDT_005(self, setup):
        self.log.info("Test_case test_user_login_DDT_005 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo_nop_com")
        self.lp = LoginClass(self.driver)
        self.rows = ExcelMethods.numRows(self.Excel_File_Path, 'LoginData')  # 5
        print("Number of rows in excel sheet-->" + str(self.rows))
        TestCase_Status_List = []
        for r in range(2, self.rows + 1):  # iteration r = 2
            self.username = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 2)
            self.password = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 3)
            self.Expected_Result = ExcelMethods.readData(self.Excel_File_Path, 'LoginData', r, 4)
            # print("iteration-->" +str(r))
            # print("username-->" + self.username)
            # print("password-->" + self.password)
            # print("Expected_Result-->" + self.Expected_Result)
            self.log.info("Entering email - " + self.username)
            self.lp.Enter_Email(self.username)
            self.log.info("Entering Password - " + self.password)
            self.lp.Enter_Password(self.password)
            self.log.info("Click on login button")
            self.lp.Click_Login()

            if self.lp.Verify_Login_Stauts() == "Login Pass":  # actual Result # login hogaya
                self.log.info("Login Pass")
                ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")
                if self.Expected_Result == "Pass":  # expected result
                    self.log.info("Expected Pass")
                    TestCase_Status_List.append("Pass")  # updating the Status List
                    self.log.info("Taking screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Pass",
                                  attachment_type=AttachmentType.PNG)
                    self.driver.save_screenshot("..\\Screenshots\\test_user_login_params_004_pass.png")
                    self.log.info("Click on Logout button")
                    self.lp.Click_Logout()
                elif self.Expected_Result == "Fail":
                    self.log.info("Expected Fail")
                    TestCase_Status_List.append("Fail")
                    ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Pass")
                    self.log.info("Taking screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_002-Pass",
                                  attachment_type=AttachmentType.PNG)
                    self.driver.save_screenshot("..\\Screenshots\\test_user_login_params_004_pass.png")
                    self.log.info("Click on Logout button")
                    self.lp.Click_Logout()
            elif self.lp.Verify_Login_Stauts() == "Login Fail":  # login nhi hua
                ExcelMethods.writeData(self.Excel_File_Path, 'LoginData', r, 5, "Fail")
                self.log.info("Login Fail")
                if self.Expected_Result == "Fail":
                    self.log.info("Expected Fail")
                    TestCase_Status_List.append("Pass")
                elif self.Expected_Result == "Pass":
                    self.log.info("Expected Pass")
                    TestCase_Status_List.append("Fail")
                    self.log.info("Taking screenshot")
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_user_login_params_004-Fail",
                                  attachment_type=AttachmentType.PNG)
                    self.driver.save_screenshot("..\\Screenshots\\test_user_login_params_004_fail.png")
        print(TestCase_Status_List)  # ['Pass','Fail','Pass','Pass']

        if "Fail" in TestCase_Status_List:
            self.log.info("Test_case test_user_login_DDT_005 is Failed")
            assert False
        else:
            self.log.info("Test_case test_user_login_DDT_005 is Passed ")
            assert True
        self.log.info("Test_case test_user_login_DDT_005 is Completed")

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
