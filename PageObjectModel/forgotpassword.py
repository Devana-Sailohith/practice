from selenium.webdriver.common.by import By


class forgotpassword:

    def __init__(self, driver):
        self.actual_warring = None
        self.invalidEmail = None
        self.emailBox = None
        self.clickForget = None
        self.driver = driver


    forgotpasswordLINK_TEXT = "Forgotten Password"
    emailboxXPATH = "//input[@id='input-email']"
    validWarring = "An email with a confirmation link has been sent your email address."
    validWarringXpath = "//div[@id='account-login']/div[1]"
    invalidWarring = "Warning: The E-Mail Address was not found in our records, please try again!"
    invalidWarringXpath = "//div[@id='account-forgotten']/div[1]"


    def clickForgotEmail(self):
        self.clickForget = self.driver.find_element(By.LINK_TEXT, self.forgotpasswordLINK_TEXT)
        self.clickForget.click()


    def enterEmailId(self, email):
        self.emailBox = self.driver.find_element(By.XPATH, self.emailboxXPATH)
        self.emailBox.send_keys(email)


    def enterInvalidEmail(self, email):
        self.invalidEmail = self.driver.find_element(By.XPATH, self.emailboxXPATH)
        self.invalidEmail.send_keys(email)


    def validEmailWarring(self):
        self.actual_warring = self.driver.find_element(By.XPATH, self.validWarringXpath).text
        assert self.actual_warring in self.validWarring


    def invalidEmailWarring(self):
        self.actual_warring = self.driver.find_element(By.XPATH, self.invalidWarringXpath).text
        assert self.actual_warring in self.invalidWarring