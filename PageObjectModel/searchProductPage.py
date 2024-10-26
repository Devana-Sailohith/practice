from selenium.webdriver.common.by import By

from Locators.Xpaths import LoginFunctionality, SearchProductFunctionality


class searchProduct:

    def __init__(self, driver):
        self.invalidwarringtext = None
        self.weblink = None
        self.textofproduct = None
        self.searchforproduct = None
        self.searchbar = None
        self.driver = driver


    # websiteLink = "https://tutorialsninja.com/demo/index.php?route=common/home"
    # searchBoxXpath = "//input[@name='search']"
    # searchButtonXpath = "//div[@id='search']//button[@type='button']"
    # invalidProductWarringTextMessage = "There is no product that matches the search criteria."
    # invalidProductWarringMessageXpath = "//input[@id='button-search']/following-sibling::p"
    webLink = LoginFunctionality()
    search = SearchProductFunctionality()

    def clickForSearchProduct(self, product):
        self.weblink = self.driver.get(self.webLink.loginPageLink)
        self.searchbar = self.driver.find_element(By.XPATH, self.search.searchBoxXpath)
        self.searchbar.click()
        self.searchbar.clear()
        self.searchbar.send_keys(product)


    def clickSearchButton(self):
        self.searchforproduct = self.driver.find_element(By.XPATH, self.search.searchButtonXpath)
        self.searchforproduct.click()


    def checkForTitle(self, product):
        self.textofproduct = self.driver.find_element(By.XPATH, "//a[text()='"+str(product)+"']").text
        if product in self.textofproduct:
            assert True
        else:
            assert False


    def invalidWarringMessage(self):
        self.invalidwarringtext = self.driver.find_element(By.XPATH, self.search.invalidProductWarringMessageXpath).text
        if self.invalidwarringtext == self.search.invalidProductWarringTextMessage:
            assert True
        else:
            assert False