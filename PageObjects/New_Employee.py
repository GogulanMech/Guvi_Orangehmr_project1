from selenium.webdriver.common.by import By


class New_Employee:
    # Login page
    txt_username_name = 'username'
    txt_password_name = 'password'
    btn_login_tagname = "button"
    # PIM
    list_pim_xpath = "//a[@class='oxd-main-menu-item active']"
    # create new employee
    btn_add_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]'
    txt_firstname_name = "firstName"
    txt_middlename_name = "middleName"
    txt_lastname_name = "lastName"
    txt_employeeid_xpath = "//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input[@class='oxd-input " \
                           "oxd-input--active'] "
    btn_addimage_xpath = "//input[@type='file']"
    # Admin page
    list_admin_xpath = '//a[@href="/web/index.php/admin/viewAdminModule"]'
    # create employee username and password#####
    btn_userroll_xpath = "//div[@class='oxd-grid-2 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//" \
                         "div[1]//div[2]//i[1]"
    list_adminroll_xpath = "//div[@role='listbox']/div[2]"
    list_essroll_xpath = "//div[@role='listbox']/div[3]"
    btn_status_xpath = "//div[@class='oxd-form-row']//div[3]//i"
    list_enablestatus_xpath = "//div[@role='listbox']/div[2]"
    list_disablestatus_xpath = "//div[@role='listbox']/div[3]"
    txt_employeename_xpath = "//div[@class='oxd-autocomplete-wrapper']//input"
    list_emploeename_xpath = "//div[@class='oxd-autocomplete-dropdown --positon-bottom']/div[1]" \
                             "/span[text()='Gogulan  Murugesan']"
    txt_username2_xpath = "//div[@class='oxd-form-row']//input[@class='oxd-input oxd-input--active']"
    txt_password2_xpath = "//div[@class='oxd-form-row user-password-row']/div[@class='oxd-grid-2 orangehrm-full-width-" \
                          "grid']/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//input"
    txt_confirmpassword_xpath = "//div[@class='oxd-grid-item oxd-grid-item--gutters']//div/input[@type='password']"
    btn_save_xpath = "//button[@type='submit']"
    # Search Employee
    btn_search_xpath = "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']"
    tbl_username_xpath = "//div[@class='oxd-table-body']/div[1]//div[2]"

    # list element for every dropdown
    list_dropdown_xpath = "//div[@role='listbox']/div/span"  # use exact visible text

    def __init__(self, driver):
        self.driver = driver

    # login page module####
    def set_username(self, username):
        self.driver.find_element(By.NAME, self.txt_username_name).clear()
        self.driver.find_element(By.NAME, self.txt_username_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.NAME, self.txt_password_name).clear()
        self.driver.find_element(By.NAME, self.txt_password_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.TAG_NAME, self.btn_login_tagname).click()

    # Navigate to PIM######
    def click_pim(self):
        self.driver.find_element(By.XPATH, self.list_pim_xpath).click()

    # Creat new employee####
    def click_add(self):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()

    def set_firstname(self, firstname):
        self.driver.find_element(By.NAME, self.txt_firstname_name).send_keys(firstname)

    def set_middlenmae(self, middlename):
        self.driver.find_element(By.NAME, self.txt_middlename_name).send_keys(middlename)

    def set_lastname(self, lastname):
        self.driver.find_element(By.NAME, self.txt_lastname_name).send_keys(lastname)

    def set_employee_id(self, id):
        self.driver.find_element(By.XPATH, self.txt_employeeid_xpath).send_keys(id)

    def set_image(self, image):
        self.driver.find_element(By.XPATH, self.btn_addimage_xpath).send_keys(image)

    def click_save(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    # Navigate to admin######
    def click_admin(self):
        self.driver.find_element(By.XPATH, self.list_admin_xpath).click()

    # create new username and password####
    def set_userrole(self, role="Admin"):
        self.driver.find_element(By.XPATH, self.btn_userroll_xpath).click()
        users = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        try:
            for user in users:
                if user.text == role:
                    user.click()
                    break
        except:
            print(" User Role  is invalid")

    def set_status(self, status="Enabled"):
        self.driver.find_element(By.XPATH, self.btn_status_xpath).click()
        users = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        try:
            for user in users:
                if user.text == status:
                    user.click()
                    break
        except:
            print(" User Status is invalid")

    def set_employeename(self, employeename):
        self.driver.find_element(By.XPATH, self.txt_employeename_xpath).send_keys(employeename)
        self.driver.find_element(By.XPATH, self.list_emploeename_xpath).click()

    def set_newusername(self, newusername):
        self.driver.find_element(By.XPATH, self.txt_username2_xpath).send_keys(newusername)

    def set_newpassword(self, newpassword):
        self.driver.find_element(By.XPATH, self.txt_password2_xpath).send_keys(newpassword)

    def set_confirmpassword(self, confrimpassword):
        self.driver.find_element(By.XPATH, self.txt_confirmpassword_xpath).send_keys(confrimpassword)

    def click_save2(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    # search employee
    def click_search(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    def tbl_username(self):
        username = self.driver.find_element(By.XPATH, self.tbl_username_xpath).text
        return username
