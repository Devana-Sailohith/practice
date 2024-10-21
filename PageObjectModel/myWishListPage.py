from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from PageObjectModel.clickOnFeaturedProductPage import clickFeaturedProduct
from PageObjectModel.loginpage import loginpage


class myWishList:

    def __init__(self, driver):
        self.addtocart = None
        self.removeFromWishList = None
        self.productAvailabilityText = None
        self.wishList = None
        self.loginDetails = None
        self.driver = driver


    myWishListXpath = "//a[@id='wishlist-total']"
    outOfStockExpected = "Out Of Stock"
    continueButtonXpath = "//a[text()='Continue']"


    def Login(self, emailid, password):
        self.loginDetails = clickFeaturedProduct(self.driver)
        self.loginDetails.clickLoginThroughHomePage(emailid, password)

    def clickWishList(self):
        self.wishList = self.driver.find_element(By.XPATH, self.myWishListXpath)
        self.wishList.click()

    def addToCardFromWishList(self):
        for i in range(1, 20):
            try:
                self.addtocart = self.driver.find_element(By.XPATH, "//div[@id='account-wishlist']//table/tbody/tr["+str(i)+"]/td[6]/button")
                self.addtocart.click()
            except NoSuchElementException as Exception:
                break
    def removeOutOfStock(self):
        for i in range(1, 20):
            try:
                self.productAvailabilityText = self.driver.find_element(By.XPATH, "//div[@id='account-wishlist']//table/tbody/tr["+str(i)+"]/td[2]/following-sibling::td[2]").text
                if self.productAvailabilityText in self.outOfStockExpected:
                    self.removeFromWishList = self.driver.find_element(By.XPATH, "//div[@id='account-wishlist']//table/tbody/tr["+str(i)+"]/td[6]/a")
                    self.removeFromWishList.click()
            except NoSuchElementException as Exception:
                break

    def clickContinueButton(self):
        self.countinebutton = self.driver.find_element(By.XPATH, self.continueButtonXpath)
        self.countinebutton.click()

    def clickLogout(self):
        self.logout = loginpage(self.driver)
        self.clickAccountIcon = self.driver.find_element(By.XPATH, self.logout.accountIconXpath)
        self.clickAccountIcon.click()
        self.clickLogoutButton = self.driver.find_element(By.XPATH, self.logout.logoutXpath)
        self.clickLogoutButton.click()