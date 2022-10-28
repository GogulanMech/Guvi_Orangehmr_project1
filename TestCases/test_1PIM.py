import random
import string
import time

from selenium.webdriver.common.by import By
from PageObjects.New_employee_detail import New_Employee_Detail
from PageObjects.New_Employee import New_Employee
from Utilities.readproperties import ReadConfig
from Utilities.customlogger import logger


class Test_001_PIM:
    url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    newusername = ReadConfig.get_newusername()
    logger = logger.loggen()

    def test_addemploeedetails(self, setup):
        driver = setup
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        self.logger.info("*******************Test_001_PIM***********************")
        self.logger.info("*******************Verifying Login test ***********************")
        status = []
        emp = New_Employee(driver)
        pim = New_Employee_Detail(driver)
        email1 = random_generator(4) + "@gmail.com"
        email2 = random_generator(6) + "@gmail.com"

        # Code for Entering Login Detail
        emp.set_username(self.username)
        emp.set_password(self.password)
        emp.click_login()
        self.logger.info("******************Login is successful**************************")

        # Code for Entering New Employee Detail
        self.logger.info("******************PIM - Verifying New Employee Details**************************")
        emp.click_pim()
        emp.click_add()
        emp.set_firstname(self.newusername)
        emp.set_lastname("Murugesan")
        emp.set_employee_id(random_generator())
        emp.set_image("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work\\Guvi_Orangehmr_project1\\TestData"
                      "\\gogul_photo.jpg")
        emp.click_save()
        time.sleep(1)

        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Add employee is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Add employee is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_Add_employee.png")
            status.append(False)

        # Code for Entering personal Detail
        self.logger.info("******************PIM - Verifying Personal Details**************************")
        pim.set_personal_details(random_generator(3), "Tn5464654", "2040-09-14", "Indian", "Single", "1995-07-01",
                                 "Male")
        pim.set_nickname("gogul")   # Some time its not present in webpage
        pim.set_ssn_sin_number(random_generator(4), random_generator(3))  # Some time its not present in webpage
        pim.set_military(random_generator(3))  # Some time its not present in webpage
        pim.set_smoker("yes")  # Some time its not present in webpage
        pim.click_personal_save()  # If nickname is not present in the webpage its not work change in POM
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Personal Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Personal Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_personal_detail.png")
            status.append(False)

        pim.set_blood_type("AB+")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Personal Blood Group is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Personal Blood Group is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_personal_Blood_group.png")
            status.append(False)
        pim.set_personal_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                    "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Personal Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Personal Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_personal_Attachment.png")
            status.append(False)
        time.sleep(2)

        # Code for Entering Contact Detail
        self.logger.info("******************PIM - Verifying Contact Details**************************")
        pim.click_contact_details()
        pim.set_address("3/726 Green", "kodangipalayam", "Tirupur", "Tamilnadu", "641662", "India")
        pim.set_telephone("0422-278278", "1234567890", "0123752155")
        pim.set_email(email1, email2)
        time.sleep(2)
        pim.click_save_contact_details()
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Contact Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Contact Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_contact_detail.png")
            status.append(False)
        time.sleep(2)
        pim.set_contact_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                   "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Contact Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Contact Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_contact_attachment.png")
            status.append(False)
        time.sleep(5)

        # Code for Entering Emergency Details
        self.logger.info("******************PIM - Verifying Emergency Details**************************")
        pim.click_emergency_contact()
        pim.set_emergency_contact("Bala", "Brother", "54684652", "53466+5", "654985")
        pim.set_emergency_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                     "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Emergency Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Emergency Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_emergency_detail.png")
            status.append(False)
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Emergency Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Emergency Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_emergency_attachment.png")
            status.append(False)
        time.sleep(3)

        # Code for Entering Dependents Detail
        self.logger.info("******************PIM - Verifying Dependents Details**************************")
        pim.click_dependents()
        pim.set_dependents("hima", "Child", "2010-09-11")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Dependents Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Dependents Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_dependents_detail.png")
            status.append(False)

        pim.set_dependent_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                     "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Dependents Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Dependents Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_dependents_attachment.png")
            status.append(False)
        time.sleep(3)

        # Code for Entering Immigration Detail
        self.logger.info("******************PIM - Verifying Immigration Details**************************")
        pim.click_immigration()
        pim.set_immigration_record("Passport", "IND54545454", "2010-06-23", "2030-07-07", "current", "India",
                                   "2022-01-01", "I am ready to fly")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Immigration Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Immigration Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_immigration_detail.png")
            status.append(False)

        pim.set_immigration_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                       "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Immigration Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Immigration Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_immigration_attachment.png")
            status.append(False)
        time.sleep(5)

        # Code for Entering Job Detail
        self.logger.info("******************PIM - Verifying Job Details**************************")
        pim.click_job()
        time.sleep(1)
        pim.set_job_details("2020-05-03", "QA Engineer", "Professionals", "Quality Assurance", "Canadian Regional HQ",
                            "Full-Time Permanent")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Job Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Job Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_job_detail.png")
            status.append(False)
        time.sleep(5)

        # Code for Entering Salary Detail
        self.logger.info("******************PIM - Verifying Salary Details**************************")
        pim.click_salary()
        pim.set_salary_components("Account pay", "Grade 1", "Monthly", "United States Dollar", "55000",
                                  "type any comment")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Salary Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Salary Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_salary_detail.png")
            status.append(False)
        pim.set_salary_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                  "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Salary Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Salary Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_salary_attachment.png")
            status.append(False)
        time.sleep(3)

        # Code for Entering Tax Exemption Detail
        self.logger.info("******************PIM - Verifying Tax Exemption Details**************************")
        pim.click_tax_exemption()
        pim.set_tax_exemption("Single", "5", "Alabama", "Single", "3", "American Samoa", "Arizona")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Tax Exemption Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Tax Exemption Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_tax_detail.png")
            status.append(False)
        pim.set_tax_exemption_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                         "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Tax Exemption Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Tax Exemption Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_tax_attachment.png")
            status.append(False)
        time.sleep(3)

        # Code for Entering Report To Detail
        self.logger.info("******************PIM - Verifying Report To Details**************************")
        pim.click_report_to()
        pim.set_report_to("t", "Direct", "t", "Direct")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Report To Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Report To Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_tax_detail.png")
            status.append(False)
        time.sleep(3)
        pim.set_report_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                  "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")

        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Report To Attachment is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Report To Attachment is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_tax_attachment.png")
            status.append(False)
        time.sleep(5)

        # Code for Entering Qualification Detail
        self.logger.info("******************PIM - Verifying Qualification Details**************************")
        pim.click_qualification()
        pim.set_qualification_experience("Tata", "MD", "2016-10-03", "2022-01-06", "Something")

        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Experience Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Experience Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_experience_detail.png")
            status.append(False)

        pim.set_qualification_education("Bachelor's Degree", "PSG", "Mechanical", "4", "2012-07-03", "2016-05-28")

        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Education Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Education Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_education_detail.png")
            status.append(False)

        pim.set_qualification_skill("Python", "5", "I know python with selenium")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Skill Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Skill Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_skill_detail.png")
            driver.get_screenshot_as_png()
            status.append(False)

        pim.set_qualification_language("English", "Reading", "Good", "I Know Tamil Very well")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Language Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Language Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_language_detail.png")
            status.append(False)

        pim.set_qualification_licence("Microsoft Certified Systems Engineer (MCSE)", "ASD458521", "2019-05-30",
                                      "2040-12-29")
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Licence Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Licence Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_licence_detail.png")
            status.append(False)

        pim.set_qualification_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                         "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")
        time.sleep(1)
        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Q-Attachment Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Q-Attachment Details is failed**************************")
            self.logger.error("******************PIM - Qualification Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_q-attachment_detail.png")
            status.append(False)
        time.sleep(5)

        # Code for Entering Membership Detail
        self.logger.info("******************PIM - Verifying Membership Details**************************")
        pim.click_membership()
        pim.set_membership("Chartered Institute of Marketing (CIM)", "Company", "5000", "Indian Rupee", "2020-05-05",
                           "2022-12-30")

        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Membership Details is successful**************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Membership Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_membership_detail.png")
            status.append(False)

        pim.set_membership_attachment("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                      "\\Guvi_Orangehmr_project1\\TestData\\gogul_photo.jpg", "Hi this for testing")

        validate = pim.set_validate()
        if "Success" in validate:
            self.logger.info("******************PIM - Membership-attach Details is successful*************************")
            status.append(True)
        else:
            self.logger.error("******************PIM - Membership-attach Details is failed**************************")
            driver.save_screenshot("Screenshots/Test_001_membership-attachment.png")
            status.append(False)
        time.sleep(5)

        # Validation Of Total Employee Details
        if False not in status:
            assert True
            self.logger.info("*******************Test_001_PIM New Employee Detail Add Successfully********************")
        else:
            self.logger.error("****************** Test_001_PIM Add New Employee Detail  is failed*********************")
        self.logger.info("*******************Ending Test_001_PIM*******************")




def random_generator(size=4, chars=string.digits):
    return ''.join(random.choice(chars) for x in range(size))
