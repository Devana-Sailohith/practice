from selenium.webdriver.common.by import By


class searchProduct:

    def __init__(self, driver):
        self.invalidwarringtext = None
        self.weblink = None
        self.textofproduct = None
        self.searchforproduct = None
        self.searchbar = None
        self.driver = driver


    websiteLink = "https://tutorialsninja.com/demo/index.php?route=common/home"
    searchBoxXpath = "//input[@name='search']"
    searchButtonXpath = "//div[@id='search']//button[@type='button']"
    invalidProductWarringTextMessage = "There is no product that matches the search criteria."
    invalidProductWarringMessageXpath = "//input[@id='button-search']/following-sibling::p"


    def clickForSearchProduct(self, product):
        self.weblink = self.driver.get(self.websiteLink)
        self.searchbar = self.driver.find_element(By.XPATH, self.searchBoxXpath)
        self.searchbar.click()
        self.searchbar.clear()
        self.searchbar.send_keys(product)


    def clickSearchButton(self):
        self.searchforproduct = self.driver.find_element(By.XPATH, self.searchButtonXpath)
        self.searchforproduct.click()


    def checkForTitle(self, product):
        self.textofproduct = self.driver.find_element(By.XPATH, "//a[text()='"+str(product)+"']").text
        if product in self.textofproduct:
            assert True
        else:
            assert False


    def invalidWarringMessage(self):
        self.invalidwarringtext = self.driver.find_element(By.XPATH, self.invalidProductWarringMessageXpath).text
        if self.invalidwarringtext == self.invalidProductWarringTextMessage:
            assert True
        else:
            assert False