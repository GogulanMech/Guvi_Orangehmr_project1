from Utilities.customlogger import logger
from PageObjects.New_Employee import New_Employee
from Utilities.readproperties import ReadConfig


class Test_002_Login:
    url = ReadConfig.get_url()
    username = ReadConfig.get_newusername()
    password = ReadConfig.get_newusername()
    logger = logger.loggen()

    def test_login(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.logger.info("*******************Test_002_Login***********************")
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