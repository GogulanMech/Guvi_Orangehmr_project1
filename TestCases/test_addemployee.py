import time
from Utilities.customlogger import logger
from PageObjects.New_Employee import New_Employee
from Utilities.readproperties import ReadConfig


class Test_001_AddEmployee:
    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    newusername = ReadConfig.get_newusername()
    newpassword = ReadConfig.get_newpassword()
    logger = logger.loggen()

    def test_login(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.logger.info("*******************Test_001_AddEmployee***********************")
        self.logger.info("*******************Verifying Login test ***********************")
        emp = New_Employee(driver)
        emp.set_username(self.username)
        emp.set_password(self.password)
        emp.click_login()
        exp_title = "OrangeHRM"
        if driver.title == exp_title:
            assert True
            self.logger.info("*****************Home page test is passed*************************")
        else:
            self.logger.error("*****************Home page test is failed*************************")
            driver.save_screenshot("Screenshots/Test_001_logintest.png")
            assert False

    def test_addemployee(self, setup):
        self.logger.info("*******************Verifying Addemployee***********************")
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        emp = New_Employee(driver)
        emp.set_username(self.username)
        emp.set_password(self.password)
        emp.click_login()
        self.logger.info("******************Login is successful**************************")
        emp.click_pim()
        emp.click_add()
        emp.set_firstname(self.newusername)
        emp.set_lastname("Murugesan")
        emp.set_image("TestData/gogul_photo.jpg")
        emp.click_save()
        self.logger.info("******************PIM - Add employee is successful**************************")
        emp.click_admin()
        emp.click_add()
        emp.click_userrole()
        emp.click_adminrole()
        time.sleep(2)
        emp.click_status()
        time.sleep(2)
        emp.click_enable()
        emp.set_employeename(self.newusername)
        time.sleep(2)
        emp.set_newusername(self.newusername)
        emp.set_newpassword(self.newpassword)
        emp.set_confirmpassword(self.newpassword)
        time.sleep(2)
        emp.click_save2()
        time.sleep(5)
        self.logger.info("******************Admin Add employee login detail is successful**************************")
        self.logger.info("******************Admin Add employee login detail is successful**************************")
        emp.set_newusername(self.newusername)
        emp.click_search()
        time.sleep(2)
        if emp.tbl_username() == self.newusername:
            self.logger.info("******************Search employee  detail is successful**************************")
            assert True
        else:
            self.logger.error("******************Search employee  detail is successful**************************")
            driver.save_screenshot("Screenshots/Test_001_search_employee.png")
            assert False

































