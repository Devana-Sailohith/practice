from selenium import webdriver
from selenium.webdriver.common.by import By

from Locators.Xpaths import LoginFunctionality, RegisterFunctionality

driver = webdriver.Chrome()
driver.implicitly_wait(7)
loginlink = LoginFunctionality()
wish = RegisterFunctionality()
driver.get(loginlink.loginPageLink)
driver.find_element(By.XPATH, loginlink.accountIconXpath).click()
driver.find_element(By.XPATH, wish.registerXpath).click()
driver.find_element(By.XPATH, wish.firstNameXpath).send_keys("sailohi")
driver.find_element(By.XPATH, wish.lastNameXpath).send_keys("sailohi")
driver.find_element(By.XPATH, wish.emailIdXpath).send_keys("sailohi@gmail.com")
driver.find_element(By.XPATH, wish.telePhoneNUmberXpath).send_keys(int("123456789012"))
driver.find_element(By.XPATH, wish.passwordXpath).send_keys("saisai")
driver.find_element(By.XPATH, wish.conformPasswordXpath).send_keys("saisai")
driver.find_element(By.XPATH, wish.privacyPolicyXpath).click()
driver.find_element(By.XPATH, wish.ContinueButtonXpath).click()
textof = driver.find_element(By.XPATH, wish.actual_warringMessageXpath).text
print(textof)
if textof in wish.expected_warringMessage:
    assert True
else:
    print(False)