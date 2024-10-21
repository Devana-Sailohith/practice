from behave import *
from selenium import webdriver
from PageObjectModel.myAccountPage import myAccountEditInfoPage


@given(u'lunch browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()

@when(u'navigate to login page "{emailid}" "{loginpassword}"')
def step_impl(context, emailid, loginpassword):
    context.ei = myAccountEditInfoPage(context.driver)
    context.ei.lunchAndNavigate(emailid, loginpassword)


@then(u'click edit account info text')
def step_impl(context):
    context.ei.clickEditAccInfo()

@then(u'enter the first name, last name, email id, telephone num "{firstname}" "{lastname}" "{emailId}" "{telephone}"')
def step_impl(context, firstname, lastname, emailId, telephone):
    context.ei.enterDetails(firstname, lastname, emailId, telephone)

@then(u'do not enter first name,enter the last name, email id, telephone num "{last}" "{emailaddress}" "{no}"')
def step_impl(context, last, emailaddress, no):
    context.ei.firstNameMissing("", last, emailaddress, no)

@then(u'click continue button to update the details')
def step_impl(context):
    context.ei.clickContinue()

@then(u'a message should come as success')
def step_impl(context):
    context.ei.successWarring()

@then(u'a warring message should come')
def step_impl(context):
    context.ei.firstNameWarring()
