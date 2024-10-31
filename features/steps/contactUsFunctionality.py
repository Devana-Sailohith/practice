from behave import *

from PageObjectModel.clickOnFeaturedProductPage import clickFeaturedProduct
from PageObjectModel.contactUsPage import contactUs
from PageObjectModel.firstNameLastName import details


@when(u'go to the website and login "{email}" "{password}"')
def step_impl(context, email, password):
    context.login = clickFeaturedProduct(context.driver)
    context.login.lunchWebBrowser()
    context.login.clickLoginThroughHomePage(email, password)

@then(u'click the contact us option')
def step_impl(context):
    context.contact = contactUs(context.driver)
    context.contact.clickContactUs()

@then(u'enter the name, email, and the enquiry')
def step_impl(context):
    context.detail = details(context.driver)
    context.contact.enterDetails(context.detail.firstname(), context.detail.lastname()+"@gmail.com", context.detail.firstname()+context.detail.lastname())

@then(u'click the submit button')
def step_impl(context):
    context.contact.clickSubmitButton()

@then(u'last click the continue buttton')
def step_impl(context):
    context.contact.clickContinueButton()