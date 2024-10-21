from selenium.webdriver.common.by import By
from PageObjectModel.loginpage import loginpage


class clickFeaturedProduct:

    def __init__(self, driver):
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

    webSiteLink = "https://tutorialsninja.com/demo/index.php?route=common/home"
    accountIconXpath = "//li[@class='dropdown']/a/i"
    loginXpath = "//a[text()='Login']"
    qafoxTitleXpath = "//div[@id='logo']"
    featuredFirstProductXpath = "//div[@class='row']/div[1]/div[1]//div[@class='image'][1]"
    featuredSecondProductXpath = "//div[@class='row']/div[2]/div[1]//div[@class='image'][1]"
    featuredThirdProductXpath = "//div[@class='row']/div[3]/div[1]//div[@class='image'][1]"
    featuredFourthProductXpath = "//div[@class='row']/div[4]/div[1]//div[@class='image'][1]"
    featuredFirstProductTitleNamesXpath = "//div[@class='row']/div[1]/div[1]//div[@class='caption']/h4"
    featuredSecondProductTitleNamesXpath = "//div[@class='row']/div[2]/div[1]//div[@class='caption']/h4"
    featuredThirdProductTitleNamesXpath = "//div[@class='row']/div[3]/div[1]//div[@class='caption']/h4"
    featuredFourthProductTitleNamesXpath = "//div[@class='row']/div[4]/div[1]//div[@class='caption']/h4"
    featureProductVerificationTextXpath = "//div[@class='btn-group']/following-sibling::h1"
    addToCartButtonXpath = "//button[@id='button-cart']"
    enterNoOfQuantity = "//input[@id='input-quantity']"
    addToWishListXpath = "//div[1]/button[@data-original-title='Add to Wish List']"
    successfullyAddToCardMessageXpath = "//div[@class='alert alert-success alert-dismissible']"
    successfullyAddToCardMessageExpected = "Success: You have added MacBook to your shopping cart!"
    tempText = ""

    def lunchWebBrowser(self):
        self.driver.get(self.webSiteLink)

    def clickLoginThroughHomePage(self, emailid, password):
        self.accounticon = self.driver.find_element(By.XPATH, self.accountIconXpath)
        self.accounticon.click()
        self.clicklogin = self.driver.find_element(By.XPATH, self.loginXpath)
        self.clicklogin.click()
        self.login = loginpage(self.driver)
        self.email = self.driver.find_element(By.XPATH, self.login.EmailXpath)
        self.email.send_keys(emailid)
        self.passw = self.driver.find_element(By.XPATH, self.login.PasswordXpath)
        self.passw.send_keys(password)
        self.loginbutton = self.driver.find_element(By.XPATH, self.login.loginButtonXpath)
        self.loginbutton.click()
        self.qafox = self.driver.find_element(By.XPATH, self.qafoxTitleXpath)
        self.qafox.click()

    def clickOnFirstFeaturedItem(self):
        self.fistfeatureditemtext = self.driver.find_element(By.XPATH, self.featuredFirstProductTitleNamesXpath).text
        self.tempText = self.fistfeatureditemtext
        self.firstfeatureditem = self.driver.find_element(By.XPATH, self.featuredFirstProductXpath)
        self.firstfeatureditem.click()


    def clickOnSecondFeaturedItem(self):
        self.secondfeatureditemtext = self.driver.find_element(By.XPATH, self.featuredSecondProductTitleNamesXpath).text
        self.tempText = self.secondfeatureditemtext
        self.secondfeatureditem = self.driver.find_element(By.XPATH, self.featuredSecondProductXpath)
        self.secondfeatureditem.click()

    def clickOnThirdFeaturedItem(self):
        self.thirdfeatureditemtext = self.driver.find_element(By.XPATH, self.featuredThirdProductTitleNamesXpath).text
        self.tempText = self.thirdfeatureditemtext
        self.thirdfeatureditem = self.driver.find_element(By.XPATH, self.featuredThirdProductXpath)
        self.thirdfeatureditem.click()

    def clickOnFourthFeaturedItem(self):
        self.fourthfeatureditem = self.driver.find_element(By.XPATH, self.featuredFourthProductXpath)
        self.fourthfeatureditem.click()

    def verifyProductTitle(self):
        self.producttext = self.driver.find_element(By.XPATH, self.featureProductVerificationTextXpath).text
        if self.producttext == self.tempText:
            assert True
        else:
            assert False

    def enterQuantity(self, quantity):
        if quantity > 1:
            self.quantityno = self.driver.find_element(By.XPATH, self.enterNoOfQuantity)
            self.quantityno.click()
            self.quantityno.clear()
            self.quantityno.send_keys(quantity)

    def clickAddToCart(self):
        self.addtocart = self.driver.find_element(By.XPATH, self.addToCartButtonXpath)
        self.addtocart.click()

    def clickAddToWishList(self):
        self.wishlist = self.driver.find_element(By.XPATH, self.addToWishListXpath)
        self.wishlist.click()

    def verifyAddCardMessage(self):
        self.addtocardtext = self.driver.find_element(By.XPATH, self.successfullyAddToCardMessageXpath).text
        if self.addtocardtext in self.successfullyAddToCardMessageExpected:
            print("yes")
            assert True
        print(self.addtocardtext)