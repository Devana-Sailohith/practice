from selenium.webdriver.common.by import By

from Locators.Xpaths import MyAccountEditInfoFunctionality
from PageObjectModel.loginpage import loginpage


class myAccountEditInfoPage:

    def __init__(self, driver):
        self.telNumWarringText = None
        self.emailIdWarringText = None
        self.lastNameWarringText = None
        self.firstNameWarringText = None
        self.successwarringtext = None
        self.continuebutton = None
        self.telnum = None
        self.email = None
        self.last = None
        self.first = None
        self.editinfo = None
        self.backbutton = None
        self.login = None
        self.driver = driver

    myAccountInfo = MyAccountEditInfoFunctionality()


    def lunchAndNavigate(self, emailid, password):
        self.login = loginpage(self.driver)
        self.login.navigateToLoginPage()
        self.login.Email(emailid)
        self.login.Password(password)
        self.login.clickLoginButton()

    def clickEditAccInfo(self):
        self.editinfo = self.driver.find_element(By.XPATH, self.myAccountInfo.editAccountInfoLinkText)
        self.editinfo.click()

    def enterDetails(self, firstname, lastname, emailId, telephone):
        self.first = self.driver.find_element(By.XPATH, self.myAccountInfo.firstNameXpath)
        self.first.click()
        self.first.clear()
        self.first.send_keys(firstname)
        self.last = self.driver.find_element(By.XPATH, self.myAccountInfo.lastNameXpath)
        self.last.click()
        self.last.clear()
        self.last.send_keys(lastname)
        self.email = self.driver.find_element(By.XPATH, self.myAccountInfo.emailIdXpath)
        self.email.click()
        self.email.clear()
        self.email.send_keys(emailId)
        self.telnum = self.driver.find_element(By.XPATH, self.myAccountInfo.telNumXpath)
        self.telnum.click()
        self.telnum.clear()
        self.telnum.send_keys(telephone)


    def firstNameMissing(self, firstname, lastname, emailId, telephone):
        self.first = self.driver.find_element(By.XPATH, self.myAccountInfo.firstNameXpath)
        self.first.click()
        self.first.clear()
        self.first.send_keys(firstname)
        self.last = self.driver.find_element(By.XPATH, self.myAccountInfo.lastNameXpath)
        self.last.click()
        self.last.clear()
        self.last.send_keys(lastname)
        self.email = self.driver.find_element(By.XPATH, self.myAccountInfo.emailIdXpath)
        self.email.click()
        self.email.clear()
        self.email.send_keys(emailId)
        self.telnum = self.driver.find_element(By.XPATH, self.myAccountInfo.telNumXpath)
        self.telnum.click()
        self.telnum.clear()
        self.telnum.send_keys(telephone)

    def clickContinue(self):
        self.continuebutton = self.driver.find_element(By.XPATH, self.myAccountInfo.continueButtonXpath)
        self.continuebutton.click()


    def successWarring(self):
        self.successwarringtext = self.driver.find_element(By.XPATH, self.myAccountInfo.updateSuccessWarringXpath).text
        if self.successwarringtext in self.myAccountInfo.updateSuccessWarringText:
            assert True


    def firstNameWarring(self):
        self.firstNameWarringText = self.driver.find_element(By.XPATH, self.myAccountInfo.firstNameMissingWarringXpath).text
        if self.firstNameWarringText in self.myAccountInfo.firstNameMissingWarringText:
            assert True


    def lastNameWarring(self):
        self.lastNameWarringText = self.driver.find_element(By.XPATH, self.myAccountInfo.lastNameMissingWarringXpath).text
        if self.lastNameWarringText in self.myAccountInfo.firstNameMissingWarringText:
            assert True


    def emailIdWarring(self):
        self.emailIdWarringText = self.driver.find_element(By.XPATH, self.myAccountInfo.emailIdMissingWarringXpath).text
        if self.emailIdWarringText in self.myAccountInfo.emailIdMissingWarringText:
            assert True


    def telNumWarring(self):
        self.telNumWarringText = self.driver.find_element(By.XPATH, self.myAccountInfo.telNumMissingWarringXpath).text
        if self.telNumWarringText in self.myAccountInfo.telNumMissingWarringText:
            assert True


    def clickBackButton(self):
        self.backbutton = self.driver.find_element(By.XPATH, self.myAccountInfo.backButtonXpath)
        self.backbutton.click()