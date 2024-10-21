import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.clickOnFeaturedProductPage import clickFeaturedProduct

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")
clickPro = clickFeaturedProduct(driver)
clickPro.lunchWebBrowser()
clickPro.clickOnFirstFeaturedItem()
time.sleep(2)
clickPro.verifyProductTitle()
clickPro.enterQuantity(1)
time.sleep(2)
clickPro.clickAddToCart()
time.sleep(5)
# productText = driver.find_element(By.XPATH, "//div[@class='row']/div[1]/div[1]//div[@class='caption']/h4").text
# print(productText)
# featuredFirstProductXpath = "//div[@class='row']/div[1]/div[1]//div[@class='image'][1]"
# driver.find_element(By.XPATH, featuredFirstProductXpath).click()
# featureProductVerificationTextXpath = "//div[@class='btn-group']/following-sibling::h1"
# itemtext = driver.find_element(By.XPATH, featureProductVerificationTextXpath).text
# print(itemtext)
# if productText in itemtext:
#     print("y")
