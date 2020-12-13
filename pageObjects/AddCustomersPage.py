import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    lnk_Customers_menu_xpath = "//a[@href='#']//span[text()='Customers']"
    lnk_Customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//span[text()='Customers']"
    btn_Addnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txt_Email_id = "Email"
    txt_Password_id = "Password"
    txt_FirstName_xpath = "//input[@id='FirstName']"
    txt_LastName_xpath = "//input[@id='LastName']"
    rd_MaleGender_id = "Gender_Male"
    rd_FemaleGender_id = "Gender_Female"
    txt_Dateofbirth_xpath = "//input[@id='DateOfBirth']"
    txt_CompanyName_xpath = "//input[@id='Company']"
    chk_TaxExempt_id = "IsTaxExempt"
    txt_AdminComment_id = "AdminComment"
    txt_Customersroles_xpath = "//*[text()='Customer roles']"
    lstitem_Registered_xpath = "//li[contains(text(),'Registered')]"
    lstitem_guest_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    lstitem_vendors_xpath = "//li[text()='Vendors']"
    lstitem_Adminstators_xpath = "//li[contains(text(),'Administrators')]"
    dr_vebdormanger_xpath = "//*[@id='VendorId']"
    chk_active_xpath = "//*[@id='Active']"
    btn_Save_xpath = "//button[@name='save']"
    txt_Newsletter_xpath="//*[text()='Newsletter']"
    lstnewsitem_xpath="//li[contains(text(),'Your store name']"


    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_menu_xpath).click()

    def clickOnCustomersmenuitem(self):
        self.driver.find_element_by_xpath(self.lnk_Customers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btn_Addnew_xpath).click()
    def setNewsletter(self,value):
        self.driver.find_element_by_xpath(self.txt_Newsletter_xpath).click()


    def setEmail(self, email):
        self.driver.find_element_by_id(self.txt_Email_id).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.txt_Password_id).send_keys(password)

    def setFirstname(self, FirstName):
        self.driver.find_element_by_xpath(self.txt_FirstName_xpath).send_keys(FirstName)

    def setLastName(self, LastName):
        self.driver.find_element_by_xpath(self.txt_LastName_xpath).send_keys(LastName)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txt_Customersroles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_guest_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_Registered_xpath)

        elif role == "Vendors":
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_vendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitem_guest_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def selectMangerofVendor(self, value):
        dr = Select(self.driver.find_element_by_xpath(self.dr_vebdormanger_xpath))
        dr.select_by_visible_text(value)

    def setGender(self, Gender):
        if Gender == 'Male':
            self.driver.find_element_by_id(self.rd_MaleGender_id).click()
        elif Gender == "Female":
            self.driver.find_element_by_id(self.rd_FemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rd_MaleGender_id).click()

    def setDob(self, dob):
        self.driver.find_element_by_xpath(self.txt_Dateofbirth_xpath).send_keys(dob)

    def setCompanyName(self, Cname):
        self.driver.find_element_by_xpath(self.txt_CompanyName_xpath).send_keys(Cname)

    def setAdminContent(self, content):
        self.driver.find_element_by_id(self.txt_AdminComment_id).send_keys(content)

    def setIsTaxexmpt(self):
        self.driver.find_element_by_id(self.chk_TaxExempt_id).click()

    def setIsActive(self):
        self.driver.find_element_by_xpath(self.chk_active_xpath).click()

    def Clicksave(self):
        self.driver.find_element_by_xpath(self.btn_Save_xpath).click()
