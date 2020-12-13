import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseUrl = ReadConfig.getBaseUrl()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger1 = LogGen.logGen()

    def test_HomePageTitle(self, setup):
        self.logger1.info("*********Verify Home page title**************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":

            self.driver.close()
            assert True
            self.logger1.info("*****Home page title test is pass******")




        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_HomePageTitle.png")
            self.driver.close()
            self.logger1.info("****Home page title is failed*****")
            assert False

    def test_Login(self, setup):
        self.logger1.info("***** verify Login *****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = Loginpage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger1.info("****Login test is pass***")
            self.driver.close()

        else:
            assert False
            self.logger1.error("***Login Test is failed*****")
            self.driver.close()
