from selenium.webdriver.common.by import By

from Locators.Xpaths import LoginFunctionality, FeaturedProductFunctionality
from PageObjectModel.loginpage import loginpage


class clickFeaturedProduct:

    def __init__(self, driver):
        self.featureProduct = None
        self.qafox = None
        self.loginbutton = None
        self.passw = None
        self.email = None
        self.login = None
        self.clicklogin = None
        self.thirdfeatureditemtext = None
        self.secondfeatureditemtext = None
        self.accounticon = None
        self.fistfeatureditemtext = None
        self.addtocardtext = None
        self.wishlist = None
        self.addtocart = None
        self.quantityno = None
        self.iteamtext = None
        self.producttext = None
        self.fourthfeatureditem = None
        self.thirdfeatureditem = None
        self.secondfeatureditem = None
        self.firstfeatureditem = None
        self.driver = driver


    def lunchWebBrowser(self):
        self.login = LoginFunctionality()
        self.driver.get(self.login.loginPageLink)
        self.driver.implicitly_wait(5)

    def clickLoginThroughHomePage(self, emailid, password):
        self.featureProduct = FeaturedProductFunctionality()
        self.accounticon = self.driver.find_element(By.XPATH, self.login.accountIconXpath)
        self.accounticon.click()
        self.clicklogin = self.driver.find_element(By.XPATH, self.login.loginIconXpath)
        self.clicklogin.click()
        self.email = self.driver.find_element(By.XPATH, self.login.EmailXpath)
        self.email.send_keys(emailid)
        self.passw = self.driver.find_element(By.XPATH, self.login.PasswordXpath)
        self.passw.send_keys(password)
        self.loginbutton = self.driver.find_element(By.XPATH, self.login.loginButtonXpath)
        self.loginbutton.click()
        self.qafox = self.driver.find_element(By.XPATH, self.featureProduct.qafoxTitleXpath)
        self.qafox.click()

    def clickOnFirstFeaturedItem(self):
        self.featureProduct = FeaturedProductFunctionality()
        self.fistfeatureditemtext = self.driver.find_element(By.XPATH, self.featureProduct.featuredFirstProductTitleNamesXpath).text
        self.featureProduct.tempText = self.fistfeatureditemtext
        self.firstfeatureditem = self.driver.find_element(By.XPATH, self.featureProduct.featuredFirstProductXpath)
        self.firstfeatureditem.click()


    def clickOnSecondFeaturedItem(self):
        self.featureProduct = FeaturedProductFunctionality()
        self.secondfeatureditemtext = self.driver.find_element(By.XPATH, self.featureProduct.featuredSecondProductTitleNamesXpath).text
        self.featureProduct.tempText = self.secondfeatureditemtext
        self.secondfeatureditem = self.driver.find_element(By.XPATH, self.featureProduct.featuredSecondProductXpath)
        self.secondfeatureditem.click()

    def clickOnThirdFeaturedItem(self):
        self.featureProduct = FeaturedProductFunctionality()
        self.thirdfeatureditemtext = self.driver.find_element(By.XPATH, self.featureProduct.featuredThirdProductTitleNamesXpath).text
        self.featureProduct.tempText = self.thirdfeatureditemtext
        self.thirdfeatureditem = self.driver.find_element(By.XPATH, self.featureProduct.featuredThirdProductXpath)
        self.thirdfeatureditem.click()

    def clickOnFourthFeaturedItem(self):
        self.featureProduct = FeaturedProductFunctionality()
        self.fourthfeatureditem = self.driver.find_element(By.XPATH, self.featureProduct.featuredFourthProductXpath)
        self.fourthfeatureditem.click()

    def verifyProductTitle(self):
        self.producttext = self.driver.find_element(By.XPATH, self.featureProduct.featureProductVerificationTextXpath).text
        if self.producttext == self.featureProduct.tempText:
            assert True
        else:
            assert False

    def enterQuantity(self, quantity):
        if quantity > 1:
            self.quantityno = self.driver.find_element(By.XPATH, self.featureProduct.enterNoOfQuantity)
            self.quantityno.click()
            self.quantityno.clear()
            self.quantityno.send_keys(quantity)

    def clickAddToCart(self):
        self.featureProduct = FeaturedProductFunctionality()
        self.addtocart = self.driver.find_element(By.XPATH, self.featureProduct.addToCartButtonXpath)
        self.addtocart.click()

    def clickAddToWishList(self):
        self.wishlist = self.driver.find_element(By.XPATH, self.featureProduct.addToWishListXpath)
        self.wishlist.click()

    def verifyAddCardMessage(self):
        self.addtocardtext = self.driver.find_element(By.XPATH, self.featureProduct.successfullyAddToCardMessageXpath).text
        if self.addtocardtext in self.featureProduct.successfullyAddToCardMessageExpected:
            print("yes")
            assert True
        print(self.addtocardtext)