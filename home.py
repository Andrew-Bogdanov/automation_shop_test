import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600);")
ruby = driver.find_element_by_css_selector(".post-160>.woocommerce-LoopProduct-link>h3").click()
reviews = driver.find_element_by_css_selector(".reviews_tab>a").click()
driver.execute_script("window.scrollBy(0, 600);")
star5 = driver.find_element_by_css_selector(".star-5").click()
comment = driver.find_element_by_css_selector("#comment").send_keys("Nice Book!")
author = driver.find_element_by_css_selector("#author").send_keys("Andrew")
email = driver.find_element_by_css_selector("#email").send_keys("bogdanovwork95@yandex.ru")
time.sleep(2)
submit = driver.find_element_by_css_selector(".submit").click()
time.sleep(2)
driver.quit()

