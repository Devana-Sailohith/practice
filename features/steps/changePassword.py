from behave import *

from PageObjectModel.changeUserPasswordPage import changeUserPassword
from PageObjectModel.myAccountPage import myAccountEditInfoPage


@then(u'navigate to login page and enter the login details "{email}" "{password}"')
def step_impl(context, email, password):
    context.li = myAccountEditInfoPage(context.driver)
    context.li.lunchAndNavigate(email, password)


@then(u'click on change your password')
def step_impl(context):
    context.cp = changeUserPassword(context.driver)
    context.cp.clickChangePassword()


@then(u'enter the new password "{newpass}" and conform password "{conformpass}"')
def step_impl(context, newpass, conformpass):
    context.cp.enterPasswords(newpass, conformpass)


@then(u'click on continue button')
def step_impl(context):
    context.cp.clickContinue()


@then(u'i should get a success message in page')
def step_impl(context):
    context.cp.successMessageText()


@then(u'click on back button')
def set_impl(context):
    context.cp.clickBackButton()


@then(u'i should get a conform password not match message in page')
def step_impl(context):
    context.cp.conformPasswordWarring()


@then(u'i should get a new password warring message and conform password warring message in page')
def step_impl(context):
    context.cp.newPasswordWarring()
    context.cp.conformPasswordWarring()


@then(u'i should get a new password warring message in page')
def step_impl(context):
    context.cp.newPasswordWarring()


@then(u'enter the new password and conform password')
def step_impl(context):
    context.cp.enterPasswords("", "")


@then(u'i should get a warring message in page')
def step_impl(context):
    context.cp.newPasswordWarring()