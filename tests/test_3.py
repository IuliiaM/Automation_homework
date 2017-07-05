from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_google_using_chrome():
    pageAddr = "http://localhost/litecart/admin"
    username = "admin"
    password = "admin"

    chrome_driver = webdriver.Chrome()
    chrome_driver.get(pageAddr)
    chrome_driver.find_element_by_name("username").send_keys(username)
    chrome_driver.find_element_by_name("password").send_keys(password)
    chrome_driver.find_element_by_name("login").submit()
    WebDriverWait(chrome_driver, 3).until(ec.title_is("My Store"))
    sleep(5)
    chrome_driver.quit()