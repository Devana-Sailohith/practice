from selenium.webdriver.common.by import By
from Locators.Xpaths import ContactUsFunctionality

class contactUs:

    def __init__(self, driver):
        self.emailaddress = None
        self.yourname = None
        self.driver = driver

    contact = ContactUsFunctionality()

    def clickContactUs(self):
        self.driver.find_element(By.XPATH, self.contact.contactUsXpath).click()

    def enterDetails(self, name, email, enquiry):
        self.yourname = self.driver.find_element(By.XPATH, self.contact.yourNameXpath)
        self.yourname.click()
        self.yourname.clear()
        self.yourname.send_keys(name)
        self.emailaddress = self.driver.find_element(By.XPATH, self.contact.emailAddressXpath)
        self.emailaddress.click()
        self.emailaddress.clear()
        self.emailaddress.send_keys(email)
        self.driver.find_element(By.XPATH, self.contact.enquiryXpath).send_keys(enquiry)

    def clickSubmitButton(self):
        self.driver.find_element(By.XPATH, self.contact.submitButtonXpath).click()

    def clickContinueButton(self):
        self.driver.find_element(By.XPATH, self.contact.continueButtonXpath).click()