import time
from sampleTest.Setup import setup, Registerlink

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
E_mail = driver.find_element(By.XPATH, "//input[@id='input-email']")
E_mail.send_keys("xasal82798@heweek.com")
# password box
Password = driver.find_element(By.XPATH, "//input[@id='input-password']")
Password.send_keys("lohi1")
# Login button
Login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
Login_button.click()
time.sleep(4)

expected_warring = "Warning: No match for E-Mail Address and/or Password."
actual_warring = driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]")
actual_warring = actual_warring.text
if expected_warring == actual_warring:
    print("yes")

# register page


driver = setup()
# The Register page link
driver.get(Registerlink())
# Your Personal Details
# first name
firstName = driver.find_element(By.XPATH, "//input[@id='input-firstname']")
firstName.send_keys("Lo")
# last name
lastName = driver.find_element(By.XPATH, "//input[@id='input-lastname']")
lastName.send_keys("Loki")
# E-mail
Email = driver.find_element(By.XPATH, "//input[@id='input-email']")
Email.send_keys("loki@gmail.com")
# telephone number
TelephoneNumber = driver.find_element(By.XPATH, "//input[@id='input-telephone']")
TelephoneNumber.send_keys("1234567891")
# your password
#  box
passwordBox = driver.find_element(By.XPATH, "//input[@id='input-password']")
passwordBox.send_keys("Loki789")
# CONFORM password
ConformPassword = driver.find_element(By.XPATH, "//input[@id='input-confirm']")
ConformPassword.send_keys("Loki789")
# newsletter
SubscribeNo = driver.find_element(By.XPATH, "//div/label[2]/input[@name='newsletter']")
if SubscribeNo.is_selected():
    print("No option is selected")
else:
    SubscribeNo.click()
time.sleep(3)
# privacy policy
privacyPolicy = driver.find_element(By.XPATH, "//input[@name='agree']")
if privacyPolicy.is_selected():
    var = None
else:
    privacyPolicy.click()

# Continue
ContinueButton = driver.find_element(By.XPATH, "//input[@value='Continue']")
ContinueButton.click()

# after entering the details
# next step
NextContinueButton = driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
NextContinueButton.click()