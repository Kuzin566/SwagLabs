import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""Список пользователей"""
user_name = ["standard_user", "locked_out_user", "problem_user", "performance_glitch_user", "Nick_Kuzin"]
"""Список паролей"""
user_password = ["secret_sauce", "secret_sauce", "secret_sauce", "secret_sauce", "my_parol"]
"Список локаторов Названий"
locator_title = ["//*[@id='item_4_title_link']/div", "//*[@id='item_0_title_link']/div", "//*[@id='item_1_title_link']/div", "//*[@id='item_5_title_link']/div", "//*[@id='item_2_title_link']/div", "//*[@id='item_3_title_link']/div"]
"""Список локаторов цены"""
locator_price = ["//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[2]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[3]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[4]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[5]/div[2]/div[2]/div", "//*[@id='inventory_container']/div/div[6]/div[2]/div[2]/div"]
"Список локаторов Add_to cart"
locator_add_to_cart = ["//*[@id='add-to-cart-sauce-labs-backpack']", "//*[@id='add-to-cart-sauce-labs-bike-light']", "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']", "//*[@id='add-to-cart-sauce-labs-fleece-jacket']", "//*[@id='add-to-cart-sauce-labs-onesie']", "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']"]


"""Класс для авторизации"""
class Login_page():
    def __init__(self, driver, login_name, login_password):
        self.driver = driver
        self.login_name = login_name
        self.login_password = login_password
    def avtorization(self):
        """Авторизация на сайте"""
        user_name = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.click()
        user_name.send_keys(self.login_name)
        print("Input Login : " + self.login_name)
        user_password = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        user_password.click()
        user_password.send_keys(self.login_password)
        print("Input Password : " + self.login_password)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='login-button']"))).click()
        print("Click Button Login")

    def logout_user(self):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@id= 'react-burger-menu-btn']"))).click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id= 'logout_sidebar_link']"))).click()
        print("Logout")

        """Очистка полей ввода логина и пароля"""
    def cleaning_field(self):
        user_name = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.click()
        user_name.send_keys(Keys.COMMAND + "a")
        user_name.send_keys(Keys.BACKSPACE)
        print("Поле User_name очищенно")
        user_password = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        user_password.click()
        user_password.send_keys(Keys.COMMAND + "a")
        user_password.send_keys(Keys.BACKSPACE)
        print("Поле User_pasword очищенно")


"""Класс для описания продукта и добавления в корзину"""
class Product_1():
    def __init__(self, driver):
        self.driver = driver
        """Описание продукта и добавление в корзину"""
    def description_product(self, number_product):
        self.number_product = number_product
        if self.number_product == "1":
            product_our = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_title[0]))))
            product_text = product_our.text
            print("Название продукта: " + product_text)
            price_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_price[0]))))
            price_product_text = price_product.text
            print("Цена продукта : " + price_product_text)
            add_to_cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_add_to_cart[0]))))
            add_to_cart.click()
            print("Product добавлен в корзину")
        elif self.number_product == "2":
            product_our = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_title[1]))))
            product_text = product_our.text
            print("Название продукта: " + product_text)
            price_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_price[1]))))
            price_product_text = price_product.text
            print("Цена продукта : " + price_product_text)
            add_to_cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_add_to_cart[1]))))
            add_to_cart.click()
            print("Product добавлен в корзину")
        elif self.number_product == "3":
            product_our = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_title[2]))))
            product_text = product_our.text
            print("Название продукта: " + product_text)
            price_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_price[2]))))
            price_product_text = price_product.text
            print("Цена продукта : " + price_product_text)
            add_to_cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_add_to_cart[2]))))
            add_to_cart.click()
            print("Product добавлен в корзину")
        elif self.number_product == "4":
            product_our = WebDriverWait(self.driver, 30).until( expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_title[3]))))
            product_text = product_our.text
            print("Название продукта: " + product_text)
            price_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_price[3]))))
            price_product_text = price_product.text
            print("Цена продукта : " + price_product_text)
            add_to_cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_add_to_cart[3]))))
            add_to_cart.click()
            print("Product добавлен в корзину")
        elif self.number_product == "5":
            product_our = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_title[4]))))
            product_text = product_our.text
            print("Название продукта: " + product_text)
            price_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_price[4]))))
            price_product_text = price_product.text
            print("Цена продукта : " + price_product_text)
            add_to_cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_add_to_cart[4]))))
            add_to_cart.click()
            print("Product добавлен в корзину")
        elif self.number_product == "6":
            product_our = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_title[5]))))
            product_text = product_our.text
            print("Название продукта: " + product_text)
            price_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_price[5]))))
            price_product_text = price_product.text
            print("Цена продукта : " + price_product_text)
            add_to_cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "{0}".format(locator_add_to_cart[5]))))
            add_to_cart.click()
            print("Product добавлен в корзину")

    """Описание продукта в корзине"""
    def description_product_cart(self):
        cart_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class = 'inventory_item_name']")))
        cart_product_text = cart_product.text
        print("Название продукта в корзине: " + cart_product_text)
        # assert product_text == cart_product_text
        # print("Название product_1 верное")
        price_cart_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='cart_contents_container']/div/div[1]/div[3]/div[2]/div[2]/div")))
        price_cart_product_text = price_cart_product.text
        print("Цена продукта в корзине: " + price_cart_product_text)

    def description_product_order(self):
        order_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class = 'inventory_item_name']")))
        order_product_text = order_product.text
        print("Название продукта в заказе : " + order_product_text)
        price_order_product = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[@class = 'inventory_item_price']")))
        price_order_product_text = price_order_product.text
        print("Цена продукта в заказе : " + price_order_product_text)


"""Класс для различные переходов"""
class Operation():
    def __init__(self, driver):
        self.driver = driver
    """Переход в корзину с главной страницы"""
    def go_cart(self):
        cart = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='shopping_cart_container']/a")))
        cart.click()
        print("Click Button cart")
    """Кликаем кнопку CHECKOUT"""
    def click_checkout(self):
        button_checkout_1 = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='checkout']")))
        button_checkout_1.click()
        print("Click Button CHECKOUT")
    """Добавляем информацию о User"""
    def user_information(self, first_name, last_name, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.postal_code = postal_code
        pole_first_name = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='first-name']")))
        pole_first_name.send_keys(self.first_name)
        print("Input FirstName : " + self.first_name)
        pole_last_name = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='last-name']")))
        pole_last_name.send_keys(self.last_name)
        print("Input LastName : " + self.last_name)
        pole_zip_postal_code = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='postal-code']")))
        pole_zip_postal_code.send_keys(self.postal_code)
        print("Input Postal Code : " + str(self.postal_code))

    """Кликаем кнопку CONTINUE"""
    def click_continue(self):
        button_continue_1 = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='continue']")))
        button_continue_1.click()
        print("Click Button CONTINUE")

    """Кликаем кнопку Finish"""
    def click_finish(self):
        button_finish_1 = button_continue_1 = WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@id='finish']")))
        button_finish_1.click()
        print("Click Button Finish")


