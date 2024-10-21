import time

from behave import *

from PageObjectModel.modifyAddressBookPage import modifyAddressBook
from PageObjectModel.myAccountPage import myAccountEditInfoPage


@then(u'navigate tot the login page "{email}" "{password}"')
def step_impl(context, email, password):
    context.li = myAccountEditInfoPage(context.driver)
    context.li.lunchAndNavigate(email, password)


@then(u'click modify user address details')
def step_impl(context):
    context.mab = modifyAddressBook(context.driver)
    context.mab.clickModifyAddress()

@then(u'enter the details "{first}", "{last}", "{company}", "{address1}", "{address2}", "{city}", "{postalcode}", "{country}", "{state}"')
def step_impl(context, first, last, company, address1, address2, city, postalcode, country, state):
    context.mab.enterAddressDetails(first, last, company, address1, address2, city, postalcode, country, state)


@then(u'enter the details "{first}", "{last}", "{address1}", "{city}", "{country}", "{state}"')
def step_impl(context, first, last, address1, city, country, state):
    context.mab.enterAddressDetailsRequired(first, last, address1, city, country, state)


@then(u'click make it a non-default address')
def step_impl(context):
    context.mab.clickDefaultNo()


@then(u'click make it a default address')
def step_impl(context):
    context.mab.clickDefaultYes()


@then(u'click continue button')
def step_impl(context):
    context.mab.clickContinueButton()
    time.sleep(5)


@then(u'enter the state name "{stateName}" to delete the address')
def step_impl(context, stateName):
    context.mab.clickDeleteButton(stateName)


@then(u'logout')
def step_impl(context):
    context.mab.clickLogoutButton()


@then(u'click on continue button to logout')
def step_impl(context):
    context.mab.clickLogoutContinueButton()