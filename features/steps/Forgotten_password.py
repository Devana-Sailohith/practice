import time
from behave import *
from PageObjectModel.forgotpassword import forgotpassword
from PageObjectModel.loginpage import loginpage



@then(u'navigate to loginpage')
def step_impl(context):
    context.lp = loginpage(context.driver)
    context.lp.navigateToLoginPage()

@then(u'click on forgotten password option')
def step_impl(context):
    context.fp = forgotpassword(context.driver)
    context.fp.clickForgotEmail()


@then(u'enter registered email id')
def step_impl(context):
    context.fp.enterEmailId("lohi@gmail.com")


@then(u'enter invalid email id')
def step_impl(context):
    context.fp.enterInvalidEmail("lohii@gmail.com")


@then(u'a message will be displayed as An email with a confirmation link has been sent your email address.')
def step_impl(context):
    context.fp.validEmailWarring()


@then(u'a message will be displayed as Warning: The E-Mail Address was not found in our records, please try again!')
def step_impl(context):
    time.sleep(3)
    context.fp.invalidEmailWarring()