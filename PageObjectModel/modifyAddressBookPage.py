import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.Xpaths import ModifyAddressBookFunctionality


class modifyAddressBook:

    def __init__(self, driver):
        self.deletewarringtext = None
        self.successwarringtext = None
        self.logoutcontinue = None
        self.logoutbutton = None
        self.count = None
        self.addressTexts = None
        self.address = None
        self.newaddress = None
        self.delete = None
        self.backbutton = None
        self.continuebutton = None
        self.yesradiobutton = None
        self.noradiobutton = None
        self.state = None
        self.countryoption = None
        self.postal_code = None
        self.cityField = None
        self.address_2 = None
        self.address_1 = None
        self.company = None
        self.lastname = None
        self.firsrname = None
        self.modify = None
        self.editbutton = None
        self.driver = driver

    modifyAddress = ModifyAddressBookFunctionality()

    def clickModifyAddress(self):
        self.modify = self.driver.find_element(By.XPATH, self.modifyAddress.modifyAddressBookXpath)
        self.modify.click()

    def enterAddressDetails(self, firstname, lastname, company, address1, address2, city, postalcode, country, state):
        self.newaddress = self.driver.find_element(By.XPATH, self.modifyAddress.newAddressButtonXpath)
        self.newaddress.click()
        self.firsrname = self.driver.find_element(By.XPATH, self.modifyAddress.firstNameXpath)
        self.lastname = self.driver.find_element(By.XPATH, self.modifyAddress.lastNameXpath)
        self.company = self.driver.find_element(By.XPATH, self.modifyAddress.companyXpath)
        self.address_1 = self.driver.find_element(By.XPATH, self.modifyAddress.address1Xpath)
        self.address_2 = self.driver.find_element(By.XPATH, self.modifyAddress.address2Xpath)
        self.cityField = self.driver.find_element(By.XPATH, self.modifyAddress.cityXpath)
        self.postal_code = self.driver.find_element(By.XPATH, self.modifyAddress.postalCode)
        self.firsrname.send_keys(firstname)
        self.lastname.send_keys(lastname)
        self.company.send_keys(company)
        self.address_1.send_keys(address1)
        self.address_2.send_keys(address2)
        self.cityField.send_keys(city)
        self.postal_code.send_keys(postalcode)
        self.countryoption = Select(self.driver.find_element(By.XPATH, self.modifyAddress.countryXpath))
        self.countryoption.select_by_visible_text(country)
        time.sleep(4)
        self.state = Select(self.driver.find_element(By.XPATH, self.modifyAddress.region_StateXpath))
        self.state.select_by_visible_text(state)


    def enterAddressDetailsRequired(self, firstname, lastname, address1, city, country, state):
        self.newaddress = self.driver.find_element(By.XPATH, self.modifyAddress.newAddressButtonXpath)
        self.newaddress.click()
        self.firsrname = self.driver.find_element(By.XPATH, self.modifyAddress.firstNameXpath)
        self.lastname = self.driver.find_element(By.XPATH, self.modifyAddress.lastNameXpath)
        self.address_1 = self.driver.find_element(By.XPATH, self.modifyAddress.address1Xpath)
        self.cityField = self.driver.find_element(By.XPATH, self.modifyAddress.cityXpath)
        self.postal_code = self.driver.find_element(By.XPATH, self.modifyAddress.postalCode)
        self.firsrname.send_keys(firstname)
        self.lastname.send_keys(lastname)
        self.address_1.send_keys(address1)
        self.cityField.send_keys(city)
        self.countryoption = Select(self.driver.find_element(By.XPATH, self.modifyAddress.countryXpath))
        self.countryoption.select_by_visible_text(country)
        time.sleep(4)
        self.state = Select(self.driver.find_element(By.XPATH, self.modifyAddress.region_StateXpath))
        self.state.select_by_visible_text(state)



    def clickDefaultYes(self):
        self.noradiobutton = self.driver.find_element(By.XPATH, self.modifyAddress.defaultAddressNoXpath)
        self.yesradiobutton = self.driver.find_element(By.XPATH, self.modifyAddress.defaultAddressYesXpath)
        if self.noradiobutton.is_selected:
            self.yesradiobutton.click()


    def clickDefaultNo(self):
        self.noradiobutton = self.driver.find_element(By.XPATH, self.modifyAddress.defaultAddressNoXpath)
        self.yesradiobutton = self.driver.find_element(By.XPATH, self.modifyAddress.defaultAddressYesXpath)
        if self.yesradiobutton.is_selected:
            self.noradiobutton.click()


    def clickContinueButton(self):
        self.continuebutton = self.driver.find_element(By.XPATH, self.modifyAddress.continueButtonXpath)
        self.continuebutton.click()
        self.successwarringtext = self.driver.find_element(By.XPATH, self.modifyAddress.successfullyAddedAddressOrDeletedWarringXpath).text
        assert self.successwarringtext in self.modifyAddress.successfullyAddedAddressWarringExpected


    def clickBackButton(self):
        self.backbutton = self.driver.find_element(By.XPATH, self.modifyAddress.backButtonXpath)
        self.backbutton.click()


    def clickDeleteButton(self, stateName):
        self.address = []
        for i in range(1, 10):
            try:
                self.addressTexts = self.driver.find_elements(By.XPATH, "//div[@id='content']//table/tbody/tr[" + str(i) + "]/td[1]")
                for k in self.addressTexts:
                    self.address.append(k.text)
            except NoSuchElementException:
                break

        self.count = 1
        for j in self.address:
            if stateName in j:
                self.driver.find_element(By.XPATH, "//table/tbody/tr[" + str(self.count) + "]/td[2]/a[text()='Delete']").click()
            self.count += 1
        self.deletewarringtext = self.driver.find_element(By.XPATH, self.modifyAddress.successfullyAddedAddressOrDeletedWarringXpath).text
        assert self.deletewarringtext in self.modifyAddress.deletedSuccessfullyWarringExpected

    def clickEditButton(self):
        self.editbutton = self.driver.find_element(By.XPATH, self.modifyAddress.editButtonXpath)
        self.editbutton.click()


    def clickLogoutButton(self):
        self.logoutbutton = self.driver.find_element(By.XPATH, self.modifyAddress.logoutXpath)
        self.logoutbutton.click()


    def clickLogoutContinueButton(self):
        self.logoutcontinue = self.driver.find_element(By.XPATH, self.modifyAddress.logoutContinueButtonXpath)
        self.logoutcontinue.click()