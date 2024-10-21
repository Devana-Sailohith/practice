from selenium import webdriver
from selenium.webdriver.common.by import By


class loginpage:

    def __init__(self, driver):
        self.actual_W = None
        self.password = None
        self.email = None
        self.driver = driver


    loginPageLink = "https://tutorialsninja.com/demo/index.php?route=account/login"
    EmailXpath = "//input[@id='input-email']"
    PasswordXpath = "//input[@id='input-password']"
    loginButtonXpath = "//input[@value='Login']"
    firstWarring = "Warning: No match for E-Mail Address and/or Password."
    secondWarring = "Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour."
    actual_warringXpath = "//div[@id='account-login']/div[1]"
    accountIconXpath = "//li[@class='dropdown']/a/i"
    logoutXpath = "//li/a[text()='Logout']"


    def lunchBrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def navigateToLoginPage(self):
        self.driver.get(self.loginPageLink)


    def Email(self, email):
        self.email = self.driver.find_element(By.XPATH, self.EmailXpath)
        self.email.send_keys(email)


    def Password(self, password):
        self.password = self.driver.find_element(By.XPATH, self.PasswordXpath)
        self.password.send_keys(password)


    def clickLoginButton(self):
        self.driver.find_element(By.XPATH, self.loginButtonXpath).click()


    def Warring(self):
        self.actual_W = self.driver.find_element(By.XPATH, self.actual_warringXpath).text
        if self.firstWarring == self.actual_W:
            assert True
        elif self.secondWarring == self.actual_W:
            assert True
        else:
            assert False