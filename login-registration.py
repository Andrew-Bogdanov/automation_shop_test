# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(2)
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a").click()
# login_reg = driver.find_element_by_css_selector("#reg_email").send_keys("bogdanovwork95@yandex.ru")
# password_reg = driver.find_element_by_css_selector("#reg_password").send_keys("Parallellogramm555test")
# body = driver.find_element_by_css_selector("#body").click()
# register_button = driver.find_element_by_css_selector(".woocomerce-FormRow>.woocommerce-Button").click()
# time.sleep(5)
# driver.quit()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
myaccount = driver.find_element_by_css_selector("#menu-item-50>a").click()
login_log = driver.find_element_by_css_selector("#username").send_keys("bogdanovwork95@yandex.ru")
password_log = driver.find_element_by_css_selector("#password").send_keys("Parallellogramm555test")
time.sleep(2)
login_button = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button").click()
time.sleep(3)
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation-link>[href='https://practice.automationtesting.in/my-account/customer-logout/']")
logout_get_text = logout.text
assert logout_get_text == "Logout"
driver.quit()

