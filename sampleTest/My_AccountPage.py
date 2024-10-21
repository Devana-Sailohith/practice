import time

from selenium.webdriver.common.by import By

from Setup import setup

driver = setup()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/account")
time.sleep(5)
# for login
emailbox = driver.find_element(By.XPATH, "//input[@id='input-email']")
emailbox.send_keys("xasal82798@heweek.com")

passwordbox = driver.find_element(By.XPATH, "//input[@id='input-password']")
passwordbox.send_keys("lohi")

loginbutton = driver.find_element(By.XPATH, "//input[@value='Login']")
loginbutton.click()

time.sleep(4)

# edit the Account Information in the page

EditInfo = driver.find_element(By.LINK_TEXT, "Edit your account information")
EditInfo.click()

time.sleep(3)
driver.back()

# change your password

ChangePassword = driver.find_element(By.LINK_TEXT, "Change your password")
ChangePassword.click()
time.sleep(2)
driver.back()

# Modify your address book

ModifyAddressBook = driver.find_element(By.LINK_TEXT, "Modify your address book entries")
ModifyAddressBook.click()
time.sleep(2)
driver.back()

# Modify your wish list

ModifyWishList = driver.find_element(By.LINK_TEXT, "Modify your wish list")
ModifyWishList.click()
time.sleep(2)
driver.back()