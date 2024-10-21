from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PageObjectModel.loginpage import loginpage


@given(u'I navigated to login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.lp = loginpage(context.driver)
    context.lp.navigateToLoginPage()

@when(u'i enter valid email address "{email}" and valid password "{password}"')
def step_impl(context, email, password):
    context.lp.Email(email)
    context.lp.Password(password)

@when(u'i enter valid email address "{email}" and in_valid password "{password}"')
def step_impl(context, email, password):
    context.lp.Email(email)
    context.lp.Password(password)


@when(u'i enter invalid email address "{email}" and invalid password "{password}"')
def step_impl(context, email, password):
    context.lp.Email(email)
    context.lp.Password(password)


@when(u'i wont enter the email id "{email}" and password "{password}"')
def step_impl(context, email, password):
    context.lp.Email(email)
    context.lp.Password(password)


@when(u'i click on Login button')
def step_impl(context):
    context.Login_button = context.driver.find_element(By.XPATH, "//input[@value='Login']")
    context.Login_button.click()


@then(u'i should get exit')
def step_impl(context):
    time.sleep(4)
    context.driver.close()


@then(u'i should get warring message as')
def step_impl(context):
    time.sleep(3)
    context.lp.Warring()