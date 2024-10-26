import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Locators.Xpaths import MyWishListFunctionality, LoginFunctionality

class myWishList:

    def __init__(self, driver):
        self.removeFromWishList = None
        self.productAvailabilityText = None
        self.addtocart = None
        self.logout = None
        self.driver = driver

    MyWishList = MyWishListFunctionality()
    login = LoginFunctionality()

    def Login(self, emailid, password):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.login.accountIconXpath).click()
        self.driver.find_element(By.XPATH, self.login.loginIconXpath).click()
        self.driver.find_element(By.XPATH, self.login.EmailXpath).send_keys(emailid)
        self.driver.find_element(By.XPATH, self.login.PasswordXpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.login.loginButtonXpath).click()

    def Website(self):
        self.driver.get(self.login.loginPageLink)

    def clickWishList(self):
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.MyWishList.myWishListXpath).click()

    def addToCardFromWishList(self):
        for i in range(1, 20):
            try:
                self.addtocart = self.driver.find_element(By.XPATH, "//div[@id='account-wishlist']//table/tbody/tr["+str(i)+"]/td[6]/button")
                self.addtocart.click()
            except NoSuchElementException:
                break
    def removeOutOfStock(self):
        for i in range(1, 20):
            try:
                self.productAvailabilityText = self.driver.find_element(By.XPATH, "//div[@id='account-wishlist']//table/tbody/tr["+str(i)+"]/td[2]/following-sibling::td[2]").text
                if self.productAvailabilityText in self.MyWishList.outOfStockExpected:
                    self.removeFromWishList = self.driver.find_element(By.XPATH, "//div[@id='account-wishlist']//table/tbody/tr["+str(i)+"]/td[6]/a")
                    self.removeFromWishList.click()
            except NoSuchElementException:
                break

    def clickContinueButton(self):
        self.driver.find_element(By.XPATH, self.MyWishList.continueButtonXpath).click()

    def clickLogout(self):
        self.logout = LoginFunctionality()
        self.driver.find_element(By.XPATH, self.logout.accountIconXpath).click()
        self.driver.find_element(By.XPATH, self.logout.logoutXpath).click()