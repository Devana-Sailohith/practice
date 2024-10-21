from behave import *

from PageObjectModel.searchProductPage import searchProduct


@when(u'browser has lunched enter the product "{product}"')
def step_impl(context, product):
    context.searching = searchProduct(context.driver)
    context.searching.clickForSearchProduct(product)

@when(u'browser has lunched enter the product')
def step_impl(context):
    context.searching = searchProduct(context.driver)
    context.searching.clickForSearchProduct("")

@then(u'click search button')
def step_impl(context):
    context.searching.clickSearchButton()

@then(u'get the product title name "{product}"')
def step_impl(context, product):
    context.searching.checkForTitle(product)

@then(u'i should get a product missing warring')
def step_impl(context):
    context.searching.invalidWarringMessage()