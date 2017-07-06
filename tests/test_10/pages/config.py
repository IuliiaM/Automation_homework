from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from test_10.pages.main_page import MainPage

class Config:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.mainpage = MainPage(self.driver)
        self.url = "http://localhost/litecart/en/"

    def open_main(self):
       self.mainpage.open_page(self.url)
       return self

    def quit(self):
        self.driver.quit()