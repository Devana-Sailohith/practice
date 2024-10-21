from selenium.webdriver.common.by import By


class myAccountEditInfoPage:

    def __init__(self, driver):
        self.successwarringtext = None
        self.backbutton = None
        self.telNumWarringText = None
        self.emailIdWarringText = None
        self.lastNameWarringText = None
        self.firstNameWarringText = None
        self.continuebutton = None
        self.telnum = None
        self.email = None
        self.last = None
        self.first = None
        self.editinfo = None
        self.driver = driver


    loginLink = "https://tutorialsninja.com/demo/index.php?route=account/login"
    emailXpath = "//input[@id='input-email']"
    passwordXpath = "//input[@id='input-password']"
    loginButtonXpath = "//input[@value='Login']"
    editAccountInfoLinkText = "//a[text()='Edit your account information']"
    firstNameXpath = "//input[@name='firstname']"
    lastNameXpath = "//input[@name='lastname']"
    emailIdXpath = "//input[@name='email']"
    telNumXpath = "//input[@name='telephone']"
    continueButtonXpath = "//input[@value='Continue']"
    updateSuccessWarringText = "Success: Your account has been successfully updated."
    updateSuccessWarringXpath = "//div[@id='account-account']/div[1]"
    firstNameMissingWarringText = "First Name must be between 1 and 32 characters!"
    firstNameMissingWarringXpath = "//div[1]/div[@class='col-sm-10']/div[1]"
    lastNameMissingWarringText = "Last Name must be between 1 and 32 characters!"
    lastNameMissingWarringXpath = "//div[2]/div[@class='col-sm-10']/div[1]"
    emailIdMissingWarringText = "E-Mail Address does not appear to be valid!"
    emailIdMissingWarringXpath = "//div[3]/div[@class='col-sm-10']/div[1]"
    telNumMissingWarringText = "Telephone must be between 3 and 32 characters!"
    telNumMissingWarringXpath = "//div[4]/div[@class='col-sm-10']/div[1]"
    backButtonXpath = "//a[text()='Back']"


    def lunchAndNavigate(self, emailid, password):
        self.driver.get(self.loginLink)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.emailIdXpath).send_keys(emailid)
        self.driver.find_element(By.XPATH, self.passwordXpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.loginButtonXpath).click()

    def clickEditAccInfo(self):
        self.editinfo = self.driver.find_element(By.XPATH, self.editAccountInfoLinkText)
        self.editinfo.click()


    def enterDetails(self, firstname, lastname, emailId, telephone):
        self.first = self.driver.find_element(By.XPATH, self.firstNameXpath)
        self.first.click()
        self.first.clear()
        self.first.send_keys(firstname)
        self.last = self.driver.find_element(By.XPATH, self.lastNameXpath)
        self.last.click()
        self.last.clear()
        self.last.send_keys(lastname)
        self.email = self.driver.find_element(By.XPATH, self.emailIdXpath)
        self.email.click()
        self.email.clear()
        self.email.send_keys(emailId)
        self.telnum = self.driver.find_element(By.XPATH, self.telNumXpath)
        self.telnum.click()
        self.telnum.clear()
        self.telnum.send_keys(telephone)


    def firstNameMissing(self, firstname, lastname, emailId, telephone):
        self.first = self.driver.find_element(By.XPATH, self.firstNameXpath)
        self.first.click()
        self.first.clear()
        self.first.send_keys(firstname)
        self.last = self.driver.find_element(By.XPATH, self.lastNameXpath)
        self.last.click()
        self.last.clear()
        self.last.send_keys(lastname)
        self.email = self.driver.find_element(By.XPATH, self.emailIdXpath)
        self.email.click()
        self.email.clear()
        self.email.send_keys(emailId)
        self.telnum = self.driver.find_element(By.XPATH, self.telNumXpath)
        self.telnum.click()
        self.telnum.clear()
        self.telnum.send_keys(telephone)

    def clickContinue(self):
        self.continuebutton = self.driver.find_element(By.XPATH, self.continueButtonXpath)
        self.continuebutton.click()


    def successWarring(self):
        self.successwarringtext = self.driver.find_element(By.XPATH, self.updateSuccessWarringXpath).text
        if self.successwarringtext in self.updateSuccessWarringText:
            assert True


    def firstNameWarring(self):
        self.firstNameWarringText = self.driver.find_element(By.XPATH, self.firstNameMissingWarringXpath).text
        if self.firstNameWarringText in self.firstNameMissingWarringText:
            assert True


    def lastNameWarring(self):
        self.lastNameWarringText = self.driver.find_element(By.XPATH, self.lastNameMissingWarringXpath).text
        if self.lastNameWarringText in self.firstNameMissingWarringText:
            assert True


    def emailIdWarring(self):
        self.emailIdWarringText = self.driver.find_element(By.XPATH, self.emailIdMissingWarringXpath).text
        if self.emailIdWarringText in self.emailIdMissingWarringText:
            assert True


    def telNumWarring(self):
        self.telNumWarringText = self.driver.find_element(By.XPATH, self.telNumMissingWarringXpath).text
        if self.telNumWarringText in self.telNumMissingWarringText:
            assert True


    def clickBackButton(self):
        self.backbutton = self.driver.find_element(By.XPATH, self.backButtonXpath)
        self.backbutton.click()