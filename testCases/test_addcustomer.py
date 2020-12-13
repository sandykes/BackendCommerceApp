import random
import string
import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from pageObjects.AddCustomersPage import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


class Test_002_AddCustomer:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.logGen()

    def test_addCustomer(self, setup):
        self.logger.info("******Test_002_AddCustomer ******")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****Login Successful******")
        self.logger.info("**** Starting add customer test********")
        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomersMenu()
        time.sleep(2)
        self.addCust.clickOnCustomersmenuitem()
        self.addCust.clickOnAddnew()
        self.logger.info("****providing Customer info******")
        self.email = random_generator() + "@gmail.com"
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("Test123")
        self.addCust.setFirstname("samy")
        self.addCust.setLastName("John")
        self.addCust.setGender("Male")
        self.addCust.setDob("12/13/1987")
        self.addCust.setCompanyName("Apple")
        self.addCust.setIsTaxexmpt()
        self.addCust.setCustomerRoles("")
        self.addCust.selectMangerofVendor("vendor 1")
        self.addCust.setIsActive()
        self.addCust.setAdminContent("Thi sis my comments")
        self.addCust.Clicksave()

        self.logger.info("****** saving Customer Info**********")
        self.logger.info("*******Add Customer validation started**************")

        self.msg = self.driver.find_element_by_tag_name("body").text
        print(self.msg)
        if "customer has been added successfully" in self.msg:
            assert True == True
            self.logger.info("***** Add customer test passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("***** Add Customer Test Failed********")
            assert True == False
        self.driver.close()
        self.logger.info("****** Ending add customer Test*********")
