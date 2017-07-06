from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open(self,url):
        self.driver.get(url)

    def select_product(self):
        campaign_products = self.driver.find_element_by_xpath("(//*[@id='box-campaign-products'])")
        # find all items in Campaign Products section
        products = campaign_products.find_elements_by_xpath("//a[@class='link']")
        # select first product in Campaigns section
        products[0].click()

