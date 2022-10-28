import time

from selenium.webdriver.common.by import By


class New_Employee_Detail:
    # list element for every dropdown
    list_dropdown_xpath = "//div[@role='listbox']/div/span"  # use exact visible text

    # Personal Details elements
    txt_nickname_xpath = "//form[@class='oxd-form']/div[1]//input[@class='oxd-input oxd-input--active']"
    txt_otherid_xpath = "//form[@class='oxd-form']/div[2]/div[1]/div[2]//input[@class='oxd-input oxd-input--active']"
    txt_drivinglicens_xpath = "//form[@class='oxd-form']/div[2]/div[2]/div[1]//input[@class='oxd-input " \
                              "oxd-input--active']"
    txt_expdate_xpath = "//form[@class='oxd-form']/div[2]/div[2]/div[2]//input[@class='oxd-input oxd-input--active']"
    txt_ssnnumber_xpath = "//form[@class='oxd-form']/div[2]/div[3]/div[1]//input[@class='oxd-input oxd-input--active']"
    txt_sinnumber_xpath = "//form[@class='oxd-form']/div[2]/div[3]/div[2]//input[@class='oxd-input oxd-input--active']"
    btn_nationality_xpath = "//form[@class='oxd-form']/div[3]/div[1]/div[1]//i"
    btn_maritalstatus_xpath = "//form[@class='oxd-form']/div[3]/div[1]/div[2]//i"
    txt_dob_xpath = "//form[@class='oxd-form']/div[3]/div[2]/div[1]//input[@class='oxd-input oxd-input--active']"
    btn_male_xpath = "//label/input[@value='1']"
    btn_female_xpath = "//label/input[@value='2']"
    txt_militaryservice_xpath = "//form[@class='oxd-form']/div[4]/div[1]/div[1]//input[@class='oxd-input " \
                                "oxd-input--active']"
    chkbox_smokeryes_xpath = "//div[@class='oxd-input-group oxd-input-field-bottom-space']//input[@type='checkbox']"
    btn_save_xpath = "//form/div[5]//button[@type='submit']"  # its work only nickname present in page or DOM use div[4]
    btn_bloodtype_xpath = "//div[@class='orangehrm-custom-fields']//i"
    btn_customfieldsave_xpath = "//form/div[2]//button[@type='submit']"

    # Attachment elements
    btn_attachment_xpath = "//div[@class='orangehrm-action-header']/button[@type='button']"  # 1st position attachment add symbol
    txt_selectfile_xpath = "//input[@type='file']"
    txt_comment_tagname = "textarea"  # this for all comment element
    btn_attachmentsave_xpath = "//div[@class='oxd-form-actions']/button[2]"  # save element after cancel element

    # Contact Details elements
    link_contactdetails_linktext = "Contact Details"
    txt_street1_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_street2_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_city_xpath = "//form[@class='oxd-form']/div[1]/div/div[3]//input"
    txt_state_xpath = "//form[@class='oxd-form']/div[1]/div/div[4]//input"
    txt_pin_xpath = "//form[@class='oxd-form']/div[1]/div/div[5]//input"
    btn_country_xpath = "//form[@class='oxd-form']/div[1]/div/div[6]//i"
    txt_homenumber_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_mobile_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_work_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    txt_workemail_xpath = "//form[@class='oxd-form']/div[3]/div/div[1]//input"
    txt_othermail_xpath = "//form[@class='oxd-form']/div[3]/div/div[2]//input"
    btn_contactsave_xpath = "//form[@class='oxd-form']/div[4]//button"

    # add element
    btn_add_xpath = "//div[@class='orangehrm-edit-employee-content']/div[1]//button"  # 1st position add & save button

    # Emergency Contacts Elements
    link_emergencycontact_linktext = "Emergency Contacts"
    txt_name_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_relationship_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_hometelephon_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_mobilenumber_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_worktelephone_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    btn_emergencycontactsave_xpath = "//form[@class='oxd-form']/div//button[2]"
    btn_emergencyattachment_xpath = "//div[@class='orangehrm-edit-employee-content']/div[5]//button"

    # Dependent elements
    link_dependents_linktext = "Dependents"
    txt_dependentname_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    btn_relationshipbutton_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//i"
    tbl_dob_xpath = "//form[@class='oxd-form']/div[2]//input"
    btn_dependentsave_xpath = "//form/div//button[@type='submit']"
    btn_dependattach_xpath = "//div[@class='orangehrm-edit-employee-content']/div[5]//button"

    # immigration elements
    link_immigration_liinktext = "Immigration"
    radio_passport_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input[@value='1']"
    radio_visa_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input[@value='2']"
    txt_number_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_issueddate_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    txt_expiryddate_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    txt_eligiblestatus_xpath = "//form[@class='oxd-form']/div[2]/div/div[4]//input"
    btn_issusedby_xpath = "//form[@class='oxd-form']/div/div/div[5]//i"
    txt_eligiblereview_xpath = "//form[@class='oxd-form']/div[2]/div/div[6]//input"
    btn_immigrationattach_xpath = "//div[@class='orangehrm-attachment']//button[@type='button']"  # this for job,salary, Report to, qualification, membership also

    # Job elements
    link_job_linktext = "Job"
    txt_joineddate_xpath = "//div[@class='oxd-date-input']/input"
    btn_jobtitle_xpath = "//form[@class='oxd-form']/div/div/div[2]//i"
    btn_jobcategory_xpath = "//form[@class='oxd-form']/div/div/div[4]//i"
    btn_subunit_xpath = "//form[@class='oxd-form']/div/div/div[5]//i"
    btn_location_xpath = "//form[@class='oxd-form']/div/div/div[6]//i"
    btn_employmentstatus_xpath = "//form[@class='oxd-form']/div/div/div[7]//i"
    btn_jobsave_xpath = "//button[@type='submit']"  # For single save button on page
    btn_terminate_xpath = "//div[@class='orangehrm-action-header']/button[text()=' Terminate Employment ']"
    btn_jobattach_xpath = "//div[@class='orangehrm-action-header']/button[text()=' Add ']"
    txt_terminatedate_xpath = "//div[@role='document']//input[@placeholder='yyyy-mm-dd']"
    btn_terminatereason_xpath = "//div[@class='oxd-dialog-container-default']//i[@class='oxd-icon bi-caret-down-fill " \
                                "oxd-select-text--arrow']"
    txt_note_tagname = "textarea"

    # salary elements
    link_salary_linktext = "Salary"
    txt_salarycomponent_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    btn_paygrade_xpath = "//form[@class='oxd-form']/div/div/div[2]//i"
    btn_payfrequency_xpath = "//form[@class='oxd-form']/div/div/div[3]//i"
    btn_currency_xpath = "//form[@class='oxd-form']/div/div/div[4]//i"
    txt_amount_xpath = "//form[@class='oxd-form']/div[1]/div/div[5]//input"

    # Tax exemptions elements
    link_tax_linktext = "Tax Exemptions"
    btn_status_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//i"
    txt_exemptions_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    btn_state_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//i"
    btn_taxstatus_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//i"
    btn_stateexemption_xpath = "//form[@class='oxd-form']/div[2]/div/div[3]//input"
    btn_unemploymentstate_xpath = "//form[@class='oxd-form']/div[2]/div/div[4]//i"
    btn_workstate_xpath = "//form[@class='oxd-form']/div[2]/div/div[5]//i"

    # Report to elements
    link_reportto_linktext = "Report-to"
    btn_supervisoradd_xpath = "//div[@class='orangehrm-edit-employee-content']//div[2]//button"  # use work experience
    txt_reportname_xpath = '//input[@placeholder="Type for hints..."]'  # use subordinate name also
    list_reportname_xpath = "//div[@class='oxd-autocomplete-dropdown --positon-bottom']/div[1]/span"
    btn_reportingmethod_xpath = "//form[@class='oxd-form']/div[1]/div/div//i"  # use education level
    btn_subordinates_xpath = "//div[@class='orangehrm-edit-employee-content']//div[3]//div[" \
                             "@class='orangehrm-action-header']//button "

    # Qualifications elements
    link_qualification_linktext = "Qualifications"
    txt_company_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//input"
    txt_jobtitle_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_from_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_to_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    btn_educationadd_xpath = "//div[@class='orangehrm-edit-employee-content']//div[3]/" \
                             "div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button"
    txt_institute_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_major_xpath = "//form[@class='oxd-form']/div[1]/div/div[3]//input"
    txt_year_xpath = "//form[@class='oxd-form']/div[1]/div/div[4]//input"
    txt_gpa_xpath = "//form[@class='oxd-form']/div[1]/div/div[5]//input"
    txt_start_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_end_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    btn_addskill_xpath = "//div[@class='orangehrm-edit-employee-content']//div[4]/div[@class='orangehrm-horizontal-" \
                         "padding orangehrm-vertical-padding']//button"
    btn_skill_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//i"
    txt_yearofexperience_xpath = "//div[@class='']/input[@class='oxd-input oxd-input--active']"
    btn_addlanguage_xpath = "//div[@class='orangehrm-edit-employee-content']//div[5]/div[" \
                            "@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button "
    btn_language_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//i"
    btn_fluency_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//i"
    btn_competency_xpath = "//form[@class='oxd-form']/div[1]/div/div[3]//i"
    btn_addlicense_xpath = "//div[@class='orangehrm-edit-employee-content']//div[6]/div[" \
                           "@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button "
    btn_license_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//i"
    txt_licensenumber_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//input"
    txt_issuedate_xpath = "//form[@class='oxd-form']/div[2]/div/div[1]//input"
    txt_enddate_xpath = "//form[@class='oxd-form']/div[2]/div/div[2]//input"
    btn_languageattachment_xpath = "//div[@class='orangehrm-edit-employee-content']//div[6]/" \
                                   "div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button"

    # Membership elements
    link_membership_linktext = "Memberships"
    btn_membership_xpath = "//form[@class='oxd-form']/div[1]/div/div[1]//i"
    btn_subscription_xpath = "//form[@class='oxd-form']/div[1]/div/div[2]//i"
    txt_subscripamount_xpath = "//form[@class='oxd-form']/div[1]/div/div[3]//input"
    btn_membcurrency_xpath = "//form[@class='oxd-form']/div[1]/div/div[4]//i"
    txt_commencedate_xpath = "//form[@class='oxd-form']/div[1]/div/div[5]//input"
    txt_renewaldate_xpath = "//form[@class='oxd-form']/div[1]/div/div[6]//input"

    def __init__(self, driver):
        self.driver = driver

    def set_personal_details(self, otherid="123", licence="TN545664", date="2025-08-01", nationality="Indian",
                             status="Single", dob="1995-07-01", gender="Male"):
        self.driver.find_element(By.XPATH, self.txt_otherid_xpath).send_keys(otherid)
        self.driver.find_element(By.XPATH, self.txt_drivinglicens_xpath).send_keys(licence)
        self.driver.find_element(By.XPATH, self.txt_expdate_xpath).send_keys(date)
        self.driver.find_element(By.XPATH, self.btn_nationality_xpath).click()
        nationalities = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        try:
            for n in nationalities:
                if n.text == nationality:
                    n.click()
                    break
        except:
            print(" Personal - Nationality  is invalid")

        self.driver.find_element(By.XPATH, self.btn_maritalstatus_xpath).click()
        marital = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        try:
            for s in marital:
                if s.text == status:
                    s.click()
                    break
        except:
            print(" Personal - Marital_status  is invalid")

        self.driver.find_element(By.XPATH, self.txt_dob_xpath).send_keys(dob)
        if gender == "Male" or gender == "male":
            male = self.driver.find_element(By.XPATH, self.btn_male_xpath)
            self.driver.execute_script("arguments[0].click();", male)
        elif gender == "Female" or gender == "female":
            female = self.driver.find_element(By.XPATH, self.btn_female_xpath)
            self.driver.execute_script("arguments[0].click();", female)
        else:
            self.driver.find_element(By.XPATH, self.btn_male_xpath).click()

    def set_smoker(self, smoker=None):
        if smoker == "yes" or smoker == "Yes":
            yes = self.driver.find_element(By.XPATH, self.chkbox_smokeryes_xpath)
            self.driver.execute_script("arguments[0].click();", yes)
        else:
            pass

    def set_nickname(self, name="gogul"):
        self.driver.find_element(By.XPATH, self.txt_nickname_xpath).send_keys(name)

    def set_ssn_sin_number(self, ssn="545664", sin="123456"):
        self.driver.find_element(By.XPATH, self.txt_ssnnumber_xpath).send_keys(ssn)
        self.driver.find_element(By.XPATH, self.txt_sinnumber_xpath).send_keys(sin)

    def set_military(self, number="5"):
        self.driver.find_element(By.XPATH, self.txt_militaryservice_xpath).send_keys(number)

    def click_personal_save(self):
        save = self.driver.find_element(By.XPATH, self.btn_save_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_blood_type(self, group="AB+"):
        self.driver.find_element(By.XPATH, self.btn_bloodtype_xpath).click()
        bloods = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        for blood in bloods:
            if blood.text == group:
                blood.click()
                break
        save = self.driver.find_element(By.XPATH, self.btn_customfieldsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_personal_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_attachment_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath).click()

    def click_contact_details(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_contactdetails_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_address(self, street1="3/726 Greencity", street2="Kodangipalayam", city="Tirupur", state="Tamilnadu",
                    pin="641662", country="India"):
        self.driver.find_element(By.XPATH, self.txt_street1_xpath).send_keys(street1)
        self.driver.find_element(By.XPATH, self.txt_street2_xpath).send_keys(street2)
        self.driver.find_element(By.XPATH, self.txt_city_xpath).send_keys(city)
        self.driver.find_element(By.XPATH, self.txt_state_xpath).send_keys(state)
        self.driver.find_element(By.XPATH, self.txt_pin_xpath).send_keys(pin)
        self.driver.find_element(By.XPATH, self.btn_country_xpath).click()
        countries = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        for con in countries:
            if con.text == country:
                con.click()
                break

    def set_telephone(self, home="0422-278278", mobile="8012652521", work="0422-278278"):
        self.driver.find_element(By.XPATH, self.txt_homenumber_xpath).send_keys(home)
        self.driver.find_element(By.XPATH, self.txt_mobile_xpath).send_keys(mobile)
        self.driver.find_element(By.XPATH, self.txt_work_xpath).send_keys(work)

    def set_email(self, work="gogulanknp@gmail.com", other="gogulanmech@gmail.com"):
        self.driver.find_element(By.XPATH, self.txt_workemail_xpath).send_keys(work)
        self.driver.find_element(By.XPATH, self.txt_othermail_xpath).send_keys(other)

    def click_save_contact_details(self):
        save = self.driver.find_element(By.XPATH, self.btn_contactsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_contact_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_attachment_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_emergency_contact(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_emergencycontact_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_emergency_contact(self, name="Bala", relationship="Brother", home="0422-278278", mobile="+918012612626",
                              work="0422-278278"):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_name_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.txt_relationship_xpath).send_keys(relationship)
        self.driver.find_element(By.XPATH, self.txt_hometelephon_xpath).send_keys(home)
        self.driver.find_element(By.XPATH, self.txt_mobilenumber_xpath).send_keys(mobile)
        self.driver.find_element(By.XPATH, self.txt_worktelephone_xpath).send_keys(work)
        save = self.driver.find_element(By.XPATH, self.btn_emergencycontactsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_emergency_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_emergencyattachment_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath).click()

    def click_dependents(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_dependents_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_dependents(self, name="gogulan", relationship="Child", dob="1995-12-26"):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_dependentname_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.btn_relationshipbutton_xpath).click()
        try:
            relations = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for r in relations:
                if r.text == relationship:
                    r.click()
                    break
        except:
            print(" Dependents relationship  is invalid")
        self.driver.find_element(By.XPATH, self.tbl_dob_xpath).send_keys(dob)
        time.sleep(1)
        save = self.driver.find_element(By.XPATH, self.btn_dependentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_dependent_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_dependattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_immigration(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_immigration_liinktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_immigration_record(self, document="Passport", number="IN12456789", date1="2010-10-25", date2="2030-10-08",
                               status="current", country="India", date3="2019-05-07", comment="I am ready to fly"):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        if document == "passport" or document == "passport":
            click = self.driver.find_element(By.XPATH, self.radio_passport_xpath)
            self.driver.execute_script("arguments[0].click();", click)
        elif document == "visa" or document == "Visa":
            click = self.driver.find_element(By.XPATH, self.radio_visa_xpath)
            self.driver.execute_script("arguments[0].click();", click)
        else:
            click = self.driver.find_element(By.XPATH, self.radio_passport_xpath)
            self.driver.execute_script("arguments[0].click();", click)
        self.driver.find_element(By.XPATH, self.txt_number_xpath).send_keys(number)
        self.driver.find_element(By.XPATH, self.txt_issueddate_xpath).send_keys(date1)
        self.driver.find_element(By.XPATH, self.txt_expiryddate_xpath).send_keys(date2)
        self.driver.find_element(By.XPATH, self.txt_eligiblestatus_xpath).send_keys(status)
        self.driver.find_element(By.XPATH, self.btn_issusedby_xpath).click()
        listcoun = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
        for coun in listcoun:
            if coun.text == country:
                coun.click()
                break
        self.driver.find_element(By.XPATH, self.txt_eligiblereview_xpath).send_keys(date3)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_immigration_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_immigrationattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        time.sleep(3)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_job(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_job_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_job_details(self, date="2020-05-13", title="QA Engineer", category="Professionals",
                        subunit="Quality Assurance", location="Canadian Regional HQ", status="Full-Time Permanent"):
        self.driver.find_element(By.XPATH, self.txt_joineddate_xpath).send_keys(date)
        try:
            self.driver.find_element(By.XPATH, self.btn_jobtitle_xpath).click()
            lsttitle = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for t in lsttitle:
                if t.text == title:
                    t.click()
                    break
        except:
            print("Job title is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_jobcategory_xpath).click()
            job_category = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for c in job_category:
                if c.text == category:
                    c.click()
                    break
        except:
            print("Job Category is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_subunit_xpath).click()
            job_subunit = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for s in job_subunit:
                if s.text == subunit:
                    s.click()
                    break
        except:
            print("Job Sub Unit is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_location_xpath).click()
            locations = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for i in locations:
                if i.text == location:
                    i.click()
                    break
        except:
            print("Job location is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_employmentstatus_xpath).click()
            lst_status = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for st in lst_status:
                if st.text == status:
                    st.click()
                    break
        except:
            print("Job Status is invalid")
        save = self.driver.find_element(By.XPATH, self.btn_jobsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_job_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_immigrationattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        time.sleep(3)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_salary(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_salary_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_salary_components(self, component="Account pay", grade="Grade 1", frequency="Monthly",
                              currency="Indian Rupee", amount="50000", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_salarycomponent_xpath).send_keys(component)
        try:
            self.driver.find_element(By.XPATH, self.btn_paygrade_xpath).click()
            pays = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for pay in pays:
                if pay.text == grade:
                    pay.click()
                    break
        except:
            print("Salary Grade is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_payfrequency_xpath).click()
            frequencies = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for frq in frequencies:
                if frq.text == frequency:
                    frq.click()
                    break
        except:
            print("Salary Frequency is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_currency_xpath).click()
            money = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for mon in money:
                if mon.text == currency:
                    mon.click()
                    break
        except:
            print("Salary Currency is invalid")
        self.driver.find_element(By.XPATH, self.txt_amount_xpath).send_keys(amount)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_salary_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_immigrationattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_tax_exemption(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_tax_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_tax_exemption(self, status="Single", federalexeption="4", state="Alabama", statestatus="Single",
                          stateexeption="4", unemploymentstate="American Samoa", workstate="Arizona"):
        try:
            self.driver.find_element(By.XPATH, self.btn_status_xpath).click()
            li_status = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for st in li_status:
                if st.text == status:
                    st.click()
                    break
        except:
            print("Federal Income Tax Status is invalid")
        self.driver.find_element(By.XPATH, self.txt_exemptions_xpath).send_keys(federalexeption)
        try:
            self.driver.find_element(By.XPATH, self.btn_state_xpath).click()
            tax_state = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for sat in tax_state:
                if sat.text == state:
                    sat.click()
                    break
        except:
            print("Income Tax state is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_taxstatus_xpath).click()
            tax_status = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for sta in tax_status:
                if sta.text == statestatus:
                    sta.click()
                    break
        except:
            print("Income Tax status is invalid")
        self.driver.find_element(By.XPATH, self.btn_stateexemption_xpath).send_keys(stateexeption)
        try:
            self.driver.find_element(By.XPATH, self.btn_unemploymentstate_xpath).click()
            emp_state = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for emp in emp_state:
                if emp.text == unemploymentstate:
                    emp.click()
                    break
        except:
            print("Income Tax unemployment state is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_workstate_xpath).click()
            wrk_state = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for wrk in wrk_state:
                if wrk.text == workstate:
                    wrk.click()
                    break
        except:
            print("Income Tax work state is invalid")
        save = self.driver.find_element(By.XPATH, self.btn_add_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_tax_exemption_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_attachment_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_report_to(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_reportto_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_report_to(self, name="t", method="Direct", name2="t", method2="Direct"):
        self.driver.find_element(By.XPATH, self.btn_supervisoradd_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_reportname_xpath).send_keys(name)
        self.driver.find_element(By.XPATH, self.list_reportname_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_reportingmethod_xpath).click()
            reports = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for report in reports:
                if report.text == method:
                    report.click()
                    break
        except:
            print("Report Method is invalid")
        self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.btn_subordinates_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_reportname_xpath).send_keys(name2)
        self.driver.find_element(By.XPATH, self.list_reportname_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_reportingmethod_xpath).click()
            reports = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for report in reports:
                if report.text == method2:
                    report.click()
                    break
        except:
            print("Report  Method is invalid")
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_report_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_immigrationattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        click = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", click)

    def click_qualification(self):
        save = self.driver.find_element(By.LINK_TEXT, self.link_qualification_linktext)
        self.driver.execute_script("arguments[0].click();", save)

    def set_qualification_experience(self, company="xyz", title="xyz", from_date="2016-10-25", to_date="2022-02-16",
                                     comment="type something"):
        self.driver.find_element(By.XPATH, self.btn_supervisoradd_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_company_xpath).send_keys(company)
        self.driver.find_element(By.XPATH, self.txt_jobtitle_xpath).send_keys(title)
        self.driver.find_element(By.XPATH, self.txt_from_xpath).send_keys(from_date)
        self.driver.find_element(By.XPATH, self.txt_to_xpath).send_keys(to_date)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_qualification_education(self, level="Bachelor's Degree", clg_name="xyz", major="mech", year="4", gpa="10",
                                    start="2012-08-16", end="2016-02-23"):
        self.driver.find_element(By.XPATH, self.btn_educationadd_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_reportingmethod_xpath).click()
            course = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for cour in course:
                if cour.text == level:
                    cour.click()
                    break
        except:
            print("Education level is invalid")
        self.driver.find_element(By.XPATH, self.txt_institute_xpath).send_keys(clg_name)
        self.driver.find_element(By.XPATH, self.txt_major_xpath).send_keys(major)
        self.driver.find_element(By.XPATH, self.txt_year_xpath).send_keys(year)
        self.driver.find_element(By.XPATH, self.txt_gpa_xpath).send_keys(gpa)
        self.driver.find_element(By.XPATH, self.txt_start_xpath).send_keys(start)
        self.driver.find_element(By.XPATH, self.txt_end_xpath).send_keys(end)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_qualification_skill(self, skill="Python", year="5", comment="type something"):
        self.driver.find_element(By.XPATH, self.btn_addskill_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_skill_xpath).click()
            skills = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for skil in skills:
                if skil.text == skill:
                    skil.click()
                    break
        except:
            print("qualification skill is invalid")
        self.driver.find_element(By.XPATH, self.txt_yearofexperience_xpath).send_keys(year)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_qualification_language(self, language="English", fluency="Reading", competency="Good", comment="xyz"):
        self.driver.find_element(By.XPATH, self.btn_addlanguage_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_language_xpath).click()
            languages = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for lan in languages:
                if lan.text == language:
                    lan.click()
                    break
        except:
            print("language is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_fluency_xpath).click()
            fluencys = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for flu in fluencys:
                if flu.text == fluency:
                    flu.click()
                    break
        except:
            print("language-fluency is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_competency_xpath).click()
            compts = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for com in compts:
                if com.text == competency:
                    com.click()
                    break
        except:
            print("language-competency is invalid")
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_qualification_licence(self, type="Microsoft Certified Systems Engineer (MCSE)", number="123456",
                                  issueddate="2020-12-20", expirydate="2030-12-30"):
        self.driver.find_element(By.XPATH, self.btn_addlicense_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_license_xpath).click()
            types = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for typ in types:
                if typ.text == type:
                    typ.click()
                    break
        except:
            print("language-licence-type is invalid")
        self.driver.find_element(By.XPATH, self.txt_licensenumber_xpath).send_keys(number)
        self.driver.find_element(By.XPATH, self.txt_issuedate_xpath).send_keys(issueddate)
        self.driver.find_element(By.XPATH, self.txt_enddate_xpath).send_keys(expirydate)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_qualification_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_immigrationattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def click_membership(self):
        click = self.driver.find_element(By.LINK_TEXT, self.link_membership_linktext)
        self.driver.execute_script("arguments[0].click();", click)

    def set_membership(self, membership="Chartered Institute of Marketing (CIM)", paidby="Company", amount="123245",
                       currency="Indian Rupee", date1="2021-08-16", date2="2022-02-14"):
        self.driver.find_element(By.XPATH, self.btn_add_xpath).click()
        try:
            self.driver.find_element(By.XPATH, self.btn_membership_xpath).click()
            members = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for member in members:
                if member.text == membership:
                    member.click()
                    break
        except:
            print("Membership is invalid")
        try:
            self.driver.find_element(By.XPATH, self.btn_subscription_xpath).click()
            subs = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for sub in subs:
                if sub.text == paidby:
                    sub.click()
                    break
        except:
            print("Subscription Paid By is invalid")
        self.driver.find_element(By.XPATH, self.txt_subscripamount_xpath).send_keys(amount)
        try:
            self.driver.find_element(By.XPATH, self.btn_membcurrency_xpath).click()
            curncy = self.driver.find_elements(By.XPATH, self.list_dropdown_xpath)
            for cur in curncy:
                if cur.text == currency:
                    cur.click()
                    break
        except:
            print("Currency is invalid")
        self.driver.find_element(By.XPATH, self.txt_commencedate_xpath).send_keys(date1)
        self.driver.find_element(By.XPATH, self.txt_renewaldate_xpath).send_keys(date2)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)
        time.sleep(3)

    def set_membership_attachment(self, file="file path", comment="type comment"):
        self.driver.find_element(By.XPATH, self.btn_immigrationattach_xpath).click()
        self.driver.find_element(By.XPATH, self.txt_selectfile_xpath).send_keys(file)
        self.driver.find_element(By.TAG_NAME, self.txt_comment_tagname).send_keys(comment)
        save = self.driver.find_element(By.XPATH, self.btn_attachmentsave_xpath)
        self.driver.execute_script("arguments[0].click();", save)

    def set_validate(self):
        validate = self.driver.find_element(By.XPATH, "//div[@class='oxd-toast-container "
                                                      "oxd-toast-container--bottom']//p[text() = 'Success']").text
        return validate
