import random
import string
from selenium import webdriver

class details:

    def __init__(self, driver):
        self.time = None
        self.driver = driver

    def website(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")


    def telNum(self):
        self.random_num = random.randint(1000000000, 9999999999)
        return self.random_num

    def firstname(self):
        self.randomFirstName = random.randint(5, 8)
        self.random_str = ''.join(random.choices(string.ascii_letters,k=self.randomFirstName))
        return self.random_str

    def lastname(self):
        self.randomLastName = random.randint(5, 8)
        self.random_str = ''.join(random.choices(string.ascii_letters,k=self.randomLastName))
        return self.random_str