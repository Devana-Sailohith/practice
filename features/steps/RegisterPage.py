import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from environment import details


@given(u'lunch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.details = details(context.driver)

@then(u'navigate to register web page')
def step_impl(context):
    context.driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

@then(u'give first,last name and telephone')
def step_impl(context):
    context.firstName = context.driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    context.first = context.details.firstname()
    context.firstName.send_keys(context.first)
    # last name
    context.lastName = context.driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    context.last = context.details.lastname()
    context.lastName.send_keys(context.last)
    # E-mail
    context.Email = context.driver.find_element(By.XPATH, "//input[@id='input-email']")
    context.Email.send_keys(context.first+context.last+"@gmail.com")
    # telephone number
    context.TelephoneNumber = context.driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    context.num = context.details.telNum()
    context.TelephoneNumber.send_keys(context.num)


@then(u'give password and conform password')
def step_impl(context):
    context.passwordBox = context.driver.find_element(By.XPATH, "//input[@id='input-password']")
    context.passwordBox.send_keys("loki78")
    # CONFORM password
    context.ConformPassword = context.driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    context.ConformPassword.send_keys("loki78")

@then(u'give first,last name and telephone of existing customer')
def step_impl(context):
    context.firstName = context.driver.find_element(By.XPATH, "//input[@id='input-firstname']")
    context.firstName.send_keys("lohi")
    # last name
    context.lastName = context.driver.find_element(By.XPATH, "//input[@id='input-lastname']")
    context.lastName.send_keys("lohi")
    # E-mail
    context.Email = context.driver.find_element(By.XPATH, "//input[@id='input-email']")
    context.Email.send_keys("lohi@gmail.com")
    # telephone number
    context.TelephoneNumber = context.driver.find_element(By.XPATH, "//input[@id='input-telephone']")
    context.num = context.details.telNum()
    context.TelephoneNumber.send_keys(context.num)


@then(u'give password and conform password of existing customer')
def step_impl(context):
    context.passwordBox = context.driver.find_element(By.XPATH, "//input[@id='input-password']")
    context.passwordBox.send_keys("lohi")
    # CONFORM password
    context.ConformPassword = context.driver.find_element(By.XPATH, "//input[@id='input-confirm']")
    context.ConformPassword.send_keys("lohi")

@then(u'subscribe and privacy policy')
def step_impl(context):
    context.SubscribeNo = context.driver.find_element(By.XPATH, "//div/label[2]/input[@name='newsletter']")
    if context.SubscribeNo.is_selected():
        print("No option is selected")
    else:
        context.SubscribeNo.click()
    time.sleep(3)
    # privacy policy
    context.privacyPolicy = context.driver.find_element(By.XPATH, "//input[@name='agree']")
    if context.privacyPolicy.is_selected():
        var = None
    else:
        context.privacyPolicy.click()


@then(u'click on continue')
def step_impl(context):
    context.ContinueButton = context.driver.find_element(By.XPATH, "//input[@value='Continue']")
    context.ContinueButton.click()


@then(u'click continue to complete register')
def step_impl(context):
    context.NextContinueButton = context.driver.find_element(By.XPATH, "//a[@class='btn btn-primary']")
    context.NextContinueButton.click()


@then(u'i should get an error as Warning: E-Mail Address is already registered!')
def step_impl(context):
    context.expected_warring = "Warning: E-Mail Address is already registered!"
    context.actual_warring = context.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text
    assert context.expected_warring in context.actual_warring