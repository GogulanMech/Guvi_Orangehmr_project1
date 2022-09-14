import time
from Utilities.customlogger import logger
from PageObjects.New_Employee import New_Employee
from PageObjects.New_employee_detail import New_Employee_Detail
from Utilities.readproperties import ReadConfig


class Test_002_Admin:
    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    newusername = ReadConfig.get_newusername()
    newpassword = ReadConfig.get_newpassword()
    logger = logger.loggen()


    def test_admin(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        emp = New_Employee(driver)
        pim = New_Employee_Detail(driver)
        self.logger.info("*******************Test_002_Admin***********************")
        self.logger.info("*******************Verifying Login test ***********************")
        emp.set_username(self.username)
        emp.set_password(self.password)
        emp.click_login()
        self.logger.info("******************Login is successful**************************")

        # Code for Entering Admin To Detail
        self.logger.info("*******************Verifying Admin test ***********************")
        emp.click_admin()
        emp.click_add()
        emp.set_userrole("Admin")
        time.sleep(2)
        emp.set_status("Enabled")
        time.sleep(2)
        emp.set_employeename(self.newusername)
        time.sleep(2)
        emp.set_newusername(self.newusername)
        emp.set_newpassword(self.newpassword)
        emp.set_confirmpassword(self.newpassword)
        time.sleep(2)
        emp.click_save2()
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************Admin Add employee login detail is successful**************************")
        else:
            self.logger.error("******************Admin Add employee login detail is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_Admin_logindetail.png")
        time.sleep(3)

        # Code for Verifying User To Detail
        self.logger.info("******************Verifying Admin Add employee login detail**************************")
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

        self.logger.info("*******************Ending Test_002_Admin*******************")
































