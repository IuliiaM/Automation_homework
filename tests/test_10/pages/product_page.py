from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class ProductPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def add_products(self):
        for i in range(3):
            self.driver.get("http://localhost/litecart/en/")
            self.WebDriverWait(self.driver, 3).until(ec.title_is("My Store | Online Store"))
            quantity_of_items = int(self.driver.find_element_by_xpath("(//span[@class='quantity'])").text) + 1

            campaign_products = self.driver.find_element_by_xpath("(//*[@id='box-campaign-products'])")
            products = campaign_products.find_elements_by_xpath("//a[@class='link']")
            products[0].click()

            main_page_link = self.driver.find_element_by_link_text("View full page")
            main_page_link.click()
            WebDriverWait(self.driver, 3).until(ec.title_is("Yellow Duck | Subcategory | Rubber Ducks | My Store"))

            if i == 1:
                size = self.driver.find_element_by_css_selector('select[class ="form-control"] option[value="Medium"]')
            else:
                size = self.driver.find_element_by_css_selector('select[class ="form-control"] option[value="Large"]')
            size.click()

            add_to_cart_btn = self.driver.find_element_by_xpath("//button[@name='add_cart_product']")
            add_to_cart_btn.click()

            WebDriverWait(self.driver, 2).until(
                ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[class="quantity"]'), str(quantity_of_items)))
