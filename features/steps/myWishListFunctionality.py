from behave import *

from PageObjectModel.clickOnFeaturedProductPage import clickFeaturedProduct
from PageObjectModel.myWishListPage import myWishList


@when(u'go the the website')
def step_impl(context):
    context.website = clickFeaturedProduct(context.driver)
    context.website.lunchWebBrowser()

@then(u'Login to the application "{email}" "{password}"')
def step_impl(context, email, password):
    context.wishlist = myWishList(context.driver)
    context.wishlist.Login(email, password)

@then(u'click the wish list to modify')
def step_impl(context):
    context.wishlist.clickWishList()

@then(u'check the out of stock items and remove')
def step_impl(context):
    context.wishlist.removeOutOfStock()

@then(u'after entering into wish list then click continue button')
def step_impl(context):
    context.wishlist.clickContinueButton()

@then(u'after removing the items click continue button')
def step_impl(context):
    context.wishlist.clickContinueButton()

@then(u'logout from the application')
def step_impl(context):
    context.wishlist.clickLogout()

