import time

from selenium.webdriver.common.by import By


class changeUserPassword:
    def __init__(self, driver):
        self.conformpasswordwarringtext = None
        self.backbutton = None
        self.conformpassword = None
        self.changepassword = None
        self.newpassword = None
        self.continuebutton = None
        self.successText = None
        self.driver = driver

    ChangePasswordLinkText = "Change your password"
    newPasswordXpath = "//input[@name='password']"
    conformPasswordXpath = "//input[@name='confirm']"
    continueButtonXpath = "//input[@value='Continue']"
    backButtonXpath = "//a[text()='Back']"
    successMessageExpectedText = "Success: Your password has been successfully updated."
    successMessageXpath = "//div[@class='alert alert-success alert-dismissible']"
    conformPasswordErrorText = "Password confirmation does not match password!"
    conformPasswordErrorXpath = "//div[text()='Password confirmation does not match password!']"
    newPasswordErrorText = "Password must be between 4 and 20 characters!"
    newPasswordWarringXpath = "//div[text()='Password must be between 4 and 20 characters!']"


    def clickChangePassword(self):
        self.changepassword = self.driver.find_element(By.LINK_TEXT, self.ChangePasswordLinkText)
        self.changepassword.click()


    def enterPasswords(self, newpass, conformpass):
        self.newpassword = self.driver.find_element(By.XPATH, self.newPasswordXpath)
        self.newpassword.click()
        self.newpassword.clear()
        self.newpassword.send_keys(newpass)
        time.sleep(2)
        self.conformpassword = self.driver.find_element(By.XPATH, self.conformPasswordXpath)
        self.conformpassword.click()
        self.conformpassword.clear()
        self.conformpassword.send_keys(conformpass)


    def clickContinue(self):
        self.continuebutton = self.driver.find_element(By.XPATH, self.continueButtonXpath)
        self.continuebutton.click()


    def successMessageText(self):
        self.successText = self.driver.find_element(By.XPATH, self.successMessageXpath).text
        assert self.successText in self.successMessageExpectedText
    
    
    def clickBackButton(self):
        self.backbutton = self.driver.find_element(By.XPATH, self.backButtonXpath)
        self.backbutton.click()
    
    def conformPasswordWarring(self):
        self.conformpasswordwarringtext = self.driver.find_element(By.XPATH, self.conformPasswordErrorXpath).text
        assert self.conformpasswordwarringtext in self.conformPasswordErrorText


    def newPasswordWarring(self):
        self.newpasswordwarring = self.driver.find_element(By.XPATH, self.newPasswordXpath).text
        assert self.newpasswordwarring in self.newPasswordErrorText