from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def test_navigation_using_chrome():
    pageAddr = "http://localhost/litecart/en/"

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(pageAddr)

    #   finding duck title
    duck1_name = driver.find_element_by_css_selector('div.name').text

    # taking price values
    duck1_regular_price = driver.find_element_by_css_selector ("s.regular-price").text
    duck1_regular_price_decor = driver.find_element_by_css_selector ("s.regular-price").value_of_css_property('text-decoration-line')
    duck1_regular_price_color = driver.find_element_by_css_selector ("s.regular-price").value_of_css_property('color')


    duck1_campaign_price = driver.find_element_by_css_selector('strong.campaign-price').text
    duck1_campaign_price_decor = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
    duck1_campaign_price_color = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')

    # new window opening
    new_window_opening = driver.find_element_by_css_selector("img.image.img-responsive").click()

    # taking values from the new window

    duck2_name = driver.find_element_by_css_selector('h1.title').text
    duck2_regular_price = driver.find_element_by_css_selector ("del.regular-price").text
    duck2_regular_price_decor = driver.find_element_by_css_selector ("del.regular-price").value_of_css_property('text-decoration-line')
    duck2_regular_price_color = driver.find_element_by_css_selector ("del.regular-price").value_of_css_property('color')

    duck2_campaign_price = driver.find_element_by_css_selector('strong.campaign-price').text
    duck2_campaign_price_decor = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('font-weight')
    duck2_campaign_price_color = driver.find_element_by_css_selector('strong.campaign-price').value_of_css_property('color')

    #compare and print

    print('Product Name is equal on Main page and Item Page - ', duck1_name == duck2_name)
    assert (duck1_name == duck2_name), "Product Title doesn't match"

    print('Product RegPrice is equal on Main page and Item Page - ', duck1_regular_price == duck2_regular_price)
    assert (duck1_regular_price == duck2_regular_price), "Product Price doesn't match"

    print('Product RegPrice decor (Line) is equal on Main page and Item Page - ', duck1_regular_price_decor == duck2_regular_price_decor)
    assert (duck1_regular_price_decor == duck2_regular_price_decor), "Product RegPrice decor (Line) doesn't match"

    print('Product RegPrice color is equal on Main page and Item Page - ', duck1_regular_price_color == duck2_regular_price_color)
    assert (duck1_regular_price_color == duck2_regular_price_color), "Product RegPrice color doesn't match"

 # need to check this line
    print('Product Campaign Price is equal on Main page and Item Page - ', duck1_campaign_price == duck2_campaign_price)
    assert (duck1_campaign_price == duck2_campaign_price), "Product Campaign Price doesn't match"

    print('Product Campaign Price font weight is equal on Main page and Item Page - ', duck1_campaign_price_decor == duck2_campaign_price_decor)
    assert (duck1_campaign_price_decor == duck2_campaign_price_decor), "Product Campaign Price font weight doesn't match"

    print('Product Campaign Price font color is equal on Main page and Item Page - ', duck1_campaign_price_color == duck2_campaign_price_color)
    assert (duck1_campaign_price_color == duck2_campaign_price_color), "Product Campaign Price color doesn't match"