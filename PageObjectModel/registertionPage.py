import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from Locators.Xpaths import LoginFunctionality, RegisterFunctionality


class register:

    def __init__(self, driver):
        self.policy = None
        self.subscribeNo = None
        self.warringMessage = None
        self.driver = driver

    # registerXpath = "//a[text()='Register']"
    # firstNameXpath = "//input[@id='input-firstname']"
    # lastNameXpath = "//input[@id='input-lastname']"
    # emailIdXpath = "//input[@id='input-email']"
    # telePhoneNUmberXpath = "//input[@id='input-telephone']"
    # passwordXpath = "//input[@id='input-password']"
    # conformPasswordXpath = "//input[@id='input-confirm']"
    # subscribeNoXpath = "//div/label[2]/input[@name='newsletter']"
    # privacyPolicyXpath = "//input[@name='agree']"
    # ContinueButtonXpath = "//input[@value='Continue']"
    # NextContinueButtonXpath = "//a[@class='btn btn-primary']"
    # expected_warringMessage = "Warning: E-Mail Address is already registered!"
    # actual_warringMessageXpath = "//div[@id='account-register']/div[1]"
    websitelink = LoginFunctionality()
    registerLocators = RegisterFunctionality()

    def LunchBrowser(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(7)

    def NavigateToWebSite(self):
        self.driver.get(self.websitelink.loginPageLink)
        self.driver.maximize_window()

    def clickRegistration(self, first, last, email, telephone):
        self.driver.find_element(By.XPATH, self.websitelink.accountIconXpath).click()
        self.driver.find_element(By.XPATH, self.registerLocators.registerXpath).click()
        self.driver.find_element(By.XPATH, self.registerLocators.firstNameXpath).send_keys(first)
        self.driver.find_element(By.XPATH, self.registerLocators.lastNameXpath).send_keys(last)
        self.driver.find_element(By.XPATH, self.registerLocators.emailIdXpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.registerLocators.telePhoneNUmberXpath).send_keys(telephone)

    def enterPasswords(self, password, conformPassword):
        self.driver.find_element(By.XPATH, self.registerLocators.passwordXpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.registerLocators.conformPasswordXpath).send_keys(conformPassword)

    def clickSubscribe(self):
        self.subscribeNo = self.driver.find_element(By.XPATH, self.registerLocators.subscribeNoXpath)
        if self.subscribeNo.is_selected():
            print("No option is selected")
        else:
            self.subscribeNo.click()

    def clickPrivacyPolicy(self):
        self.policy = self.driver.find_element(By.XPATH, self.registerLocators.privacyPolicyXpath)
        if self.policy.is_selected():
            var = None
        else:
            self.policy.click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH, self.registerLocators.conformPasswordXpath).click()

    def clickContinueNext(self):
        try:
            self.driver.find_element(By.XPATH, self.registerLocators.NextContinueButtonXpath).click()
        except NoSuchElementException:
            print(False)

    def EmailWarringMessage(self):
        time.sleep(6)
        self.warringMessage = self.driver.find_element(By.XPATH, self.registerLocators.actual_warringMessageXpath).text
        if self.warringMessage in self.registerLocators.expected_warringMessage:
            assert True