from selenium import webdriver
from selenium.webdriver.common.by import By

from Locators.Xpaths import LoginFunctionality, FeaturedProductFunctionality, MyWishListFunctionality

driver = webdriver.Chrome()
driver.implicitly_wait(7)
loginlink = LoginFunctionality()
wish = MyWishListFunctionality()
driver.get(loginlink.loginPageLink)
driver.find_element(By.XPATH, loginlink.accountIconXpath).click()
driver.find_element(By.XPATH, loginlink.loginIconXpath).click()
driver.find_element(By.XPATH, loginlink.EmailXpath).send_keys("saisai@gmail.com")
driver.find_element(By.XPATH, loginlink.PasswordXpath).send_keys("saisai")
driver.find_element(By.XPATH, loginlink.loginButtonXpath).click()


driver.find_element(By.XPATH, wish.myWishListXpath).click()
print(True)
driver.find_element(By.XPATH, wish.continueButtonXpath).click()
driver.find_element(By.XPATH, loginlink.accountIconXpath).click()
driver.find_element(By.XPATH, loginlink.logoutXpath).click()