from selenium import webdriver
from behave import *

@given(u'lunch the browser')
def before_scenario(context):
    context.driver = webdriver.Chrome()  # Replace with your desired browser
    context.driver.maximize_window()

def after_scenario(context):
    context.driver.quit()