import time

from selenium.webdriver.common.by import By

from Locators.Xpaths import ChangeUserPasswordFunctionality


class changeUserPassword:
    def __init__(self, driver):
        self.newpasswordwarring = None
        self.conformpasswordwarringtext = None
        self.successText = None
        self.conformpassword = None
        self.newpassword = None
        self.driver = driver


    changePassword = ChangeUserPasswordFunctionality()

    def clickChangePassword(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.changePassword.ChangePasswordXpath).click()


    def enterPasswords(self, newpass, conformpass):
        self.newpassword = self.driver.find_element(By.XPATH, self.changePassword.newPasswordXpath)
        self.newpassword.click()
        self.newpassword.clear()
        self.newpassword.send_keys(newpass)
        self.conformpassword = self.driver.find_element(By.XPATH, self.changePassword.conformPasswordXpath)
        self.conformpassword.click()
        self.conformpassword.clear()
        self.conformpassword.send_keys(conformpass)


    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.changePassword.continueButtonXpath).click()


    def successMessageText(self):
        self.successText = self.driver.find_element(By.XPATH, self.changePassword.successMessageXpath).text
        assert self.successText in self.changePassword.successMessageExpectedText
    
    
    def clickBackButton(self):
        self.driver.find_element(By.XPATH, self.changePassword.backButtonXpath).click()
    
    def conformPasswordWarring(self):
        self.conformpasswordwarringtext = self.driver.find_element(By.XPATH, self.changePassword.conformPasswordErrorXpath).text
        assert self.conformpasswordwarringtext in self.changePassword.conformPasswordErrorText


    def newPasswordWarring(self):
        self.newpasswordwarring = self.driver.find_element(By.XPATH, self.changePassword.newPasswordXpath).text
        assert self.newpasswordwarring in self.changePassword.newPasswordErrorText