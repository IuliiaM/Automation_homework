from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def open_cart(self):
        cart_btn = self.driver.find_element_by_xpath("//div[@id='cart']").click()
        item_table = self.driver.find_element_by_css_selector('table[class="items table table-striped data-table"]')
        remove_btns = item_table.find_elements_by_css_selector('button[name="remove_cart_item"]')
        items_count = len(remove_btns)

    def remove_all(self):
        while items_count:
        remove_btns[0].click()
        WebDriverWait(driver, 3).until(ec.staleness_of(remove_btns[0]))
        remove_btns = driver.find_elements_by_css_selector('button[name="remove_cart_item"]')
        items_count -= 1