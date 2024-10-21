from behave import *

from PageObjectModel.clickOnFeaturedProductPage import clickFeaturedProduct


@when(u'browser has lunched give the weblink to open')
def step_impl(context):
    context.clickPro = clickFeaturedProduct(context.driver)
    context.clickPro.lunchWebBrowser()

@then(u'click the featured first product')
def step_impl(context):
    context.clickPro.clickOnFirstFeaturedItem()

@then(u'enter the quantity "{quantity}"')
def step_impl(context, quantity):
    context.clickPro.enterQuantity(int(quantity))

@then(u'verify the featured first product title and the actual product title')
def step_impl(context):
    context.clickPro.verifyProductTitle()

@then(u'Add it to the cart')
def step_impl(context):
    context.clickPro.clickAddToCart()

@then(u'click the featured second product')
def step_impl(context):
    context.clickPro.clickOnSecondFeaturedItem()

@then(u'verify the featured second product title and the actual product title')
def step_impl(context):
    context.clickPro.verifyProductTitle()

@then(u'click the featured third product')
def step_impl(context):
    context.clickPro.clickOnThirdFeaturedItem()

@then(u'verify the featured third product title and the actual product title')
def step_impl(context):
    context.clickPro.verifyProductTitle()

@then(u'Add it to the wish list')
def step_impl(context):
    context.clickPro.clickAddToWishList()

@then(u'login into the application "{email}" "{password}"')
def step_impl(context, email, password):
    context.clickPro.clickLoginThroughHomePage(email, password)

