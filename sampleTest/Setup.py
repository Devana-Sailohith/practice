
def setup():
    from selenium import webdriver
    driver = webdriver.Chrome()
    return driver


def Loginlink():
    LoginPageLink = "https://tutorialsninja.com/demo/index.php?route=account/login"
    return LoginPageLink


def Registerlink():
    RegisterLink = "https://tutorialsninja.com/demo/index.php?route=account/register"
    return RegisterLink