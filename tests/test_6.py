from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

def test_navigation_using_chrome():
    pageAddr = "http://localhost/litecart/admin/"
    username = "admin"
    password = "admin"

    driver = webdriver.Chrome()
    driver.get(pageAddr)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").submit()

    driver.implicitly_wait(5)

    #openning tab
    driver.find_element_by_xpath("//a[contains(., 'Catalog')]").click()
    driver.find_element_by_xpath("//a[contains(., ' New Product')]").click()

    #filling out fields
    driver.find_element_by_xpath("//label[contains(., ' Enabled')]").click()
    driver.find_element_by_xpath("//label[contains(., ' Unisex')]").click()

    driver.find_element_by_xpath("//input[@name='date_valid_from']").send_keys("2017-03-07")
    driver.find_element_by_xpath("//input[@name='date_valid_to']").send_keys("2020-03-07")
    driver.find_element_by_xpath("//input[@name='code']").send_keys("11111")
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys("Plush Raccoon")
    driver.find_element_by_xpath("//input[@name='sku']").send_keys("100")
    driver.find_element_by_xpath("//input[@name='gtin']").send_keys("100")
    driver.find_element_by_xpath("//input[@name='taric']").send_keys("100")
    driver.find_element_by_xpath("//input[@name='quantity']").clear()
    driver.find_element_by_xpath("//input[@name='quantity']").send_keys("10")
    driver.find_element_by_xpath("//input[@name='weight']").clear()
    driver.find_element_by_xpath("//input[@name='weight']").send_keys("2")
    driver.find_element_by_xpath("//input[@name='dim_x']").clear()
    driver.find_element_by_xpath("//input[@name='dim_x']").send_keys("100")
    driver.find_element_by_xpath("//input[@name='dim_y']").clear()
    driver.find_element_by_xpath("//input[@name='dim_y']").send_keys("50")
    driver.find_element_by_xpath("//input[@name='dim_z']").clear()
    driver.find_element_by_xpath("//input[@name='dim_z']").send_keys("30")

    # add image
    driver.find_element_by_xpath("//input[@name='new_images[]']").send_keys("C:\\Users\\iuliia.marutyak\\PySelenium\\test_6\\Raccoon.jpg")
    driver.find_element_by_xpath("//button[@value='Save']").click()

    WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, ("//./a[contains(.,'Raccoon')]"))))
    driver.quit()