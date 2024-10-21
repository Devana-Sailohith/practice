import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjectModel.myAccountPage import myAccountEditInfoPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("lohiloki@gmail.com")
driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("loki")
driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//a[text()='Edit your account information']").click()
time.sleep(2)
# driver.find_element(By.XPATH, "//input[@name='firstname']").click()
# driver.find_element(By.XPATH, "//input[@name='firstname']").clear()
# driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@name='lastname']").click()
# driver.find_element(By.XPATH, "//input[@name='lastname']").clear()
# driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("loki")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@name='email']").click()
# driver.find_element(By.XPATH, "//input[@name='email']").clear()
# driver.find_element(By.XPATH, "//input[@name='email']").send_keys("lohiloki@gmail.com")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@name='telephone']").click()
# driver.find_element(By.XPATH, "//input[@name='telephone']").clear()
# driver.find_element(By.XPATH, "//input[@name='telephone']").send_keys("1234567890123")
# time.sleep(2)
# driver.find_element(By.XPATH, "//input[@value='Continue']").click()
# time.sleep(4)
ai = myAccountEditInfoPage(driver)
ai.firstNameMissing("", "loki", "lohiloki@gmail.com", "1234567890")