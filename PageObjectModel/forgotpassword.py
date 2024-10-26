from selenium.webdriver.common.by import By
from Locators.Xpaths import ForgotPasswordFunctionality

class forgotpassword:

    def __init__(self, driver):
        self.actual_warring = None
        self.driver = driver

    forgetPassword = ForgotPasswordFunctionality()

    def clickForgotEmail(self):
        self.driver.find_element(By.LINK_TEXT, self.forgetPassword.forgotpasswordLINK_TEXT).click()


    def enterEmailId(self, email):
        self.driver.find_element(By.XPATH, self.forgetPassword.emailboxXPATH).send_keys(email)


    def enterInvalidEmail(self, email):
        self.driver.find_element(By.XPATH, self.forgetPassword.emailboxXPATH).send_keys(email)


    def validEmailWarring(self):
        self.actual_warring = self.driver.find_element(By.XPATH, self.forgetPassword.validWarringXpath).text
        assert self.actual_warring in self.forgetPassword.validWarring


    def invalidEmailWarring(self):
        self.actual_warring = self.driver.find_element(By.XPATH, self.forgetPassword.invalidWarringXpath).text
        assert self.actual_warring in self.forgetPassword.invalidWarring