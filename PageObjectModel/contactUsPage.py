from selenium.webdriver.common.by import By


class contactUs:

    def __init__(self, driver):
        self.driver = driver


    contactUsXpath = "//ul[@class='list-inline']/li[1]"
    yourNameXpath = "//input[@id='input-name']"
    emailAddressXpath = "//input[@id='input-email']"
    enquiryXpath = "//textarea[@id='input-enquiry']"
    submitButtonXpath = "//input[@type='submit']"
    continueButtonXpath = "//a[text()='Continue']"
    nameExpectedWarringMessage = "Name must be between 3 and 32 characters!"
    nameWarringXpath = "//input[@name='name']/following-sibling::div"
    emailExpectedWarringMessage = "E-Mail Address does not appear to be valid!"
    emailWarringXpath = "//input[@name='email']/following-sibling::div"
    enquiryExpectedWarringMessage = "Enquiry must be between 10 and 3000 characters!"
    enquiryWarringXpath = "//textarea[@name='enquiry']/following-sibling::div"

    def clickContactUs(self):
        self.clickcontactus = self.driver.find_element(By.XPATH, self.contactUsXpath)
        self.clickcontactus.click()

    def enterDetails(self, name, email, enquiry):
        self.yourname = self.driver.find_element(By.XPATH, self.yourNameXpath)
        self.yourname.click()
        self.yourname.clear()
        self.yourname.send_keys(name)
        self.emailaddress = self.driver.find_element(By.XPATH, self.emailAddressXpath)
        self.emailaddress.click()
        self.emailaddress.clear()
        self.emailaddress.send_keys(email)
        self.clickenquiry = self.driver.find_element(By.XPATH, self.enquiryXpath)
        self.clickenquiry.send_keys(enquiry)

    def clickSubmitButton(self):
        self.clicksubmit = self.driver.find_element(By.XPATH, self.submitButtonXpath)
        self.clicksubmit.click()

    def clickContinueButton(self):
        self.clickcontinue = self.driver.find_element(By.XPATH, self.continueButtonXpath)
        self.clickcontinue.click()
        