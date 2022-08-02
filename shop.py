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
# login_log = driver.find_element_by_css_selector("#username").send_keys("bogdanovwork95@yandex.ru")
# password_log = driver.find_element_by_css_selector("#password").send_keys("Parallellogramm555test")
# login_button = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button").click()
# time.sleep(2)
# shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
# html5 = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/html5-forms/']>h3").click()
# html5title = driver.find_element_by_css_selector(".entry-summary>h1")
# html5title_get_text = html5title.text
# assert html5title_get_text == "HTML5 Forms"
# driver.quit()

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
# login_log = driver.find_element_by_css_selector("#username").send_keys("bogdanovwork95@yandex.ru")
# password_log = driver.find_element_by_css_selector("#password").send_keys("Parallellogramm555test")
# login_button = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button").click()
# time.sleep(2)
# shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
# html_cat = driver.find_element_by_css_selector(".cat-item-19>a").click()
# html_count = driver.find_elements_by_css_selector(".masonry-done>li")
# if len(html_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка")
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(2)
# myaccount = driver.find_element_by_css_selector("#menu-item-50>a").click()
# login_log = driver.find_element_by_css_selector("#username").send_keys("bogdanovwork95@yandex.ru")
# password_log = driver.find_element_by_css_selector("#password").send_keys("Parallellogramm555test")
# login_button = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button").click()
# time.sleep(2)
# shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
# orderbymain = driver.find_element_by_css_selector("[value='menu_order']")
# orderbymain_selected = orderbymain.get_attribute("value")
# if orderbymain_selected is not None:
#     print("Сортировка установлена по умолчанию")
# else:
#     print("Сортировка НЕ установлена по умолчанию")
# orderby = driver.find_element_by_css_selector(".orderby")
# select = Select(orderby)
# select.select_by_index(5)
# orderby = driver.find_element_by_css_selector(".orderby")
# orderby_high_low = driver.find_element_by_css_selector("[value = 'price-desc']")
# orderby_high_low_selected = orderby_high_low.get_attribute("value")
# if orderby_high_low_selected is not None:
#     print("Сортировка установлена по убыванию")
# else:
#     print("Сортировка НЕ установлена по убыванию")
# driver.quit()

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
# login_log = driver.find_element_by_css_selector("#username").send_keys("bogdanovwork95@yandex.ru")
# password_log = driver.find_element_by_css_selector("#password").send_keys("Parallellogramm555test")
# login_button = driver.find_element_by_css_selector(".login>.form-row>.woocommerce-Button").click()
# time.sleep(2)
# shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
# android = driver.find_element_by_css_selector("[href='https://practice.automationtesting.in/product/android-quick-start-guide/']>h3").click()
# old_price = driver.find_element_by_css_selector(".price>del>span")
# old_price_get_text = old_price.text
# assert old_price_get_text == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# new_price_get_text = new_price.text
# assert new_price_get_text == "₹450.00"
# bookimage = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".attachment-shop_single")) )
# bookimage.click()
# close_bookimage = WebDriverWait(driver, 20).until(
# EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
# close_bookimage.click()
# time.sleep(1)
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(2)
# shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
# html5_webapp = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(2)
# one_item = driver.find_element_by_css_selector(".cartcontents")
# one_item_get_text = one_item.text
# assert one_item_get_text == "1 Item"
# price_item = driver.find_element_by_css_selector(".wpmenucart-contents>span:nth-child(3)")
# price_item_get_text = price_item.text
# assert price_item_get_text == "₹180.00"
# cart = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# subtotal= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal>td>span"), "₹180.00"))
# total= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total>td>strong>span"), "₹183.60"))
# driver.quit()

# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(2)
# shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(1)
# html5_webapp = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
# time.sleep(1)
# jsdata = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']").click()
# time.sleep(1)
# cart = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
# remove_book = driver.find_element_by_css_selector("[data-product_id='182']").click()
# time.sleep(1)
# undo_book = driver.find_element_by_css_selector(".woocommerce-message>a").click()
# field1 = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
# field2 = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").send_keys("3")
# update_basket = driver.find_element_by_css_selector(".actions>.button").click()
# field3 = driver.find_element_by_css_selector("[name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# field_check = field3.get_attribute("value")
# assert field_check == "3"
# time.sleep(1)
# apply_coupon = driver.find_element_by_css_selector(".coupon>input:nth-child(3)").click()
# time.sleep(1)
# coupon_message = driver.find_element_by_css_selector(".woocommerce-error>li")
# coupon_message_get_text = coupon_message.text
# assert coupon_message_get_text == "Please enter a coupon code."
# driver.quit()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
shop = driver.find_element_by_css_selector("#menu-item-40>a").click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)
html5_webapp = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']").click()
time.sleep(1)
cart = driver.find_element_by_css_selector("a.wpmenucart-contents").click()
proceed_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button")) )
proceed = driver.find_element_by_css_selector(".checkout-button").click()
first_name_field = WebDriverWait(driver, 5).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "#billing_first_name")) )
first_name = driver.find_element_by_css_selector("#billing_first_name").send_keys("Andrew")
last_name = driver.find_element_by_css_selector("#billing_last_name").send_keys("Bogdanov")
email = driver.find_element_by_css_selector("#billing_email").send_keys("bogdanovwork95@yandex.ru")
phone = driver.find_element_by_css_selector("#billing_phone").send_keys("-")
country = driver.find_element_by_css_selector("#s2id_billing_country").click()
country_search = driver.find_element_by_css_selector("#s2id_autogen1_search").send_keys("Russia")
country_click = driver.find_element_by_css_selector(".select2-result-label").click()
address = driver.find_element_by_css_selector("p>#billing_address_1").send_keys("-")
city = driver.find_element_by_css_selector("p>#billing_city").send_keys("-")
state = driver.find_element_by_css_selector("p>#billing_state").send_keys("-")
postcode = driver.find_element_by_css_selector("p>#billing_postcode").send_keys("-")
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)
button_check = driver.find_element_by_css_selector("[value='cheque']").click()
place_order = driver.find_element_by_css_selector("#place_order").click()
thanks_message = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_message= WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".method>strong"), "Check Payments"))
driver.quit()
