from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from test_10.pages.main_page import MainPage
from test_10.pages.product_page import ProductPage
from test_10.pages.checkout_page import CheckoutPage
from test_10.pages.config import Config

def __init__(self, driver):
    self.driver = driver
    self.wait = WebDriverWait(driver, 5)

 def test_10(self):
     driver = webdriver.Chrome()
     wait = WebDriverWait(driver, 5)

     Config.open_main(self)
     MainPage.select_product(self)
     ProductPage.add_products(self)
     CheckoutPage.open_cart(self)
     CheckoutPage.remove_all(self):

    assert (self.driver.find_element_by_xpath("//em").text == "There are no items in your cart.")
quit(self)