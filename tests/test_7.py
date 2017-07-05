from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def test_page_oppening():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    for i in range(3):
        driver.get("http://localhost/litecart/en/")
        WebDriverWait(driver, 3).until(ec.title_is("My Store | Online Store"))
        quantity_of_items = int(driver.find_element_by_xpath("(//span[@class='quantity'])").text) + 1

        # find products
        campaign_products = driver.find_element_by_xpath("(//*[@id='box-campaign-products'])")
        # find all items in Campaign Products section
        products = campaign_products.find_elements_by_xpath("//a[@class='link']")
        # select first product in Campaigns section
        products[0].click()

        # go to the main page
        main_page_link = driver.find_element_by_link_text("View full page")
        main_page_link.click()
        WebDriverWait(driver, 3).until(ec.title_is("Yellow Duck | Subcategory | Rubber Ducks | My Store"))

        # select different items
        if i == 1:
            size = driver.find_element_by_css_selector('select[class ="form-control"] option[value="Medium"]')
        else:
            size = driver.find_element_by_css_selector('select[class ="form-control"] option[value="Large"]')
        size.click()
        add_to_cart_btn = driver.find_element_by_xpath("//button[@name='add_cart_product']")
        add_to_cart_btn.click()
        WebDriverWait(driver, 2).until(
            ec.text_to_be_present_in_element((By.CSS_SELECTOR, 'span[class="quantity"]'), str(quantity_of_items)))

    # open the Cart and remove products
    cart_btn = driver.find_element_by_xpath("//div[@id='cart']").click()
    item_table = driver.find_element_by_css_selector('table[class="items table table-striped data-table"]')
    remove_btns = item_table.find_elements_by_css_selector('button[name="remove_cart_item"]')
    items_count = len(remove_btns)
    while items_count:
        remove_btns[0].click()
        WebDriverWait(driver, 3).until(ec.staleness_of(remove_btns[0]))
        remove_btns = driver.find_elements_by_css_selector('button[name="remove_cart_item"]')
        items_count -= 1

    assert (driver.find_element_by_xpath("//em").text == "There are no items in your cart.")
    driver.quit()

    # Would you please explain how to use 'else' (or 'elif' if it is suitable) properly so three different products are present?