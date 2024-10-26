from selenium import webdriver
from Locators.Xpaths import LoginFunctionality
from selenium.webdriver.common.by import By

class loginpage:

    def __init__(self, driver):
        self.actual_W = None
        self.driver = driver

    login = LoginFunctionality()

    def lunchBrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def navigateToLoginPage(self):
        self.driver.get(self.login.loginPageLink)
        self.driver.find_element(By.XPATH, self.login.accountIconXpath).click()
        self.driver.find_element(By.XPATH, self.login.loginIconXpath).click()

    def Email(self, email):
        self.driver.find_element(By.XPATH, self.login.EmailXpath).send_keys(email)

    def Password(self, password):
        self.driver.find_element(By.XPATH, self.login.PasswordXpath).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.login.loginButtonXpath).click()

    def Warring(self):
        self.actual_W = self.driver.find_element(By.XPATH, self.login.actual_warringXpath).text
        if self.actual_W == self.login.firstWarring:
            assert True
        elif self.actual_W == self.login.secondWarring:
            assert True
        else:
            assert False