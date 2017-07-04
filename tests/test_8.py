from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

def test_login_Chrome():
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button[name=login]").click()
    driver.implicitly_wait(3)

def test_new_windows():

    catalog = driver.find_elements_by_xpath('//*[@id="app-"]/a')
    catalog[2].click()

    driver.find_element_by_css_selector("td:nth-child(5) a").click()

    link = driver.find_elements_by_class_name('fa-external-link')
    for i in link:
        i.click()

    for x in driver.window_handles:
        driver.switch_to.window(x)
        driver.close()

    driver.quit()