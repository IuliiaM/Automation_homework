#Hi! Would you please clarify where to put 'is_element_not_present' for implicitly_wait? Thanks in advance!

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

    links = driver.find_elements_by_xpath('//*[@id="app-"]')
    for cycle in range(1, len(links) + 1):
        outer_links = '//*[@id="box-apps-menu"]/li[' + str(cycle) + ']'
        driver.find_element_by_xpath(outer_links).click()
        inside = driver.find_elements_by_xpath(outer_links + '/ul/li')
        if inside:
            for cycle_next in range(1, len(inside) + 1):
                inner_links = outer_links + '/ul/li[' + str(cycle_next) + ']'
                driver.find_element_by_xpath(inner_links).click()
                assert len(driver.find_elements_by_tag_name('h1')) == 1
            else:
                assert len(
                    driver.find_elements_by_tag_name('h1')) == 1

    driver.quit()