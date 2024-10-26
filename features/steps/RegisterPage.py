from behave import *
from selenium import webdriver
from PageObjectModel.registertionPage import register
from PageObjectModel.firstNameLastName import details

@given(u'lunch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.details = details(context.driver)

@then(u'navigate to register web page')
def step_impl(context):
    context.reg = register(context.driver)
    context.reg.NavigateToWebSite()

@then(u'give first,last name and telephone')
def step_impl(context):
    context.first = context.details.firstname()
    # last name
    context.last = context.details.lastname()
    # E-mail
    context.emailid = context.first+context.last+"@gmail.com"
    # telephone number
    context.num = context.details.telNum()
    context.reg.clickRegistration(context.first, context.last, context.emailid, context.num)

@then(u'give password and conform password')
def step_impl(context):
    context.reg.enterPasswords("Loki78", "Loki78")

@then(u'give first,last name and telephone of existing customer')
def step_impl(context):
    context.firstName = "sailohi"
    # last name
    context.lastName = "sailohi"
    # E-mail
    context.Email = "sailohi@gmail.com"
    # telephone number
    context.num = 123456789012
    context.reg.clickRegistration(context.firstName, context.lastName, context.Email, context.num)

@then(u'give password and conform password of existing customer')
def step_impl(context):
    context.reg.enterPasswords("saisai", "saisai")

@then(u'subscribe and privacy policy')
def step_impl(context):
    context.reg.clickSubscribe()
    context.reg.clickPrivacyPolicy()

@then(u'click on continue')
def step_impl(context):
    context.reg.clickContinue()

@then(u'click continue to complete register')
def step_impl(context):
    context.reg.clickContinueNext()

@then(u'i should get an error as Warning: E-Mail Address is already registered!')
def step_impl(context):
    context.reg.EmailWarringMessage()
