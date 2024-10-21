from selenium import webdriver


def before_scenario(context):
    context.driver = webdriver.Chrome()  # Replace with your desired browser

def after_scenario(context):
    context.driver.quit()