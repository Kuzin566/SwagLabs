import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from main import user_name, user_password
from main import Login_page
from selenium import webdriver
from main import Product_1, Operation
from selenium.webdriver.common.by import By

print("Приветсвую тебя в нашем интеренет магащине")
print("Выберите один из следующих товаров и укажите его номер\n1 : Sauce Labs Backpack\n2 : Sauce Labs Bike Light\n3 : Sauce Labs Bolt T-Shirt\n4 : Sauce Labs Fleece Jacket\n5 : Sauce Labs Onesie\n6 : Test.allTheThings() T-Shirt (Red)\n")

product = input()
print(product)
time.sleep(2)
driver = webdriver.Chrome(executable_path='/Users/viktoria27vika27/PycharmProjects/resource/chromedriver')
base_url = 'https://www.saucedemo.com'
driver.get(base_url)
driver.maximize_window()
"""Авторизация на сайте"""
user = Login_page(driver, user_name[0], user_password[0])
user.avtorization()
"""Выбор продукта и добавление его в корзину"""
thing = Product_1(driver)
thing.description_product(product)
time.sleep(2)
"""Переходим в корзину"""
go_to_cart = Operation(driver)
go_to_cart.go_cart()
"""Описание продукта в корзине"""
thing_cart = Product_1(driver)
thing_cart.description_product_cart()
time.sleep(2)
"""Переходим к заполнению заказа"""
button_checkout = Operation(driver)
button_checkout.click_checkout()
"""Заполняем информацию пользователя"""
user_information = Operation(driver)
user_information.user_information("Nick", "Kuzin", 426000)
time.sleep(2)
"""Переходим в CHECKOUT: OVERVIEW. Нажимаем на кнопку CONTINUE"""
button_continue = Operation(driver)
button_continue.click_continue()
"""Проверям информацию о продукте в заказе"""
thing_order = Product_1(driver)
thing_order.description_product_order()
time.sleep(2)
"""Завершаем покупку. Нажимаем на кнопку Finich"""
button_finish = Operation(driver)
button_finish.click_finish()
"""Проверяем переход на страницу с большими благодарностями за покупку"""
text_complete = WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='checkout_complete_container']/h2")))
value_text_complete = text_complete.text
print(value_text_complete)
assert value_text_complete == "THANK YOU FOR YOUR ORDER"
print("GOOD TEST")
time.sleep(2)
driver.close()