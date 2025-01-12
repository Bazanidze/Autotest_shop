import allure
from selenium.webdriver.common.by import By

from src.Final_work.asserts.all_asserts import check_name_product_add_basket, check_price_product
from src.Final_work.normal_name_elements.all_normal_name import normal_name_pizza, normal_name_dessert
from src.Final_work.price_products.normal_price_product_and_option import normal_price_product


def normal_name_product_basket(selenium, name_product, price_product):
    with allure.step("Проверка: Товара, добавленного в корзину"):
        basket_name_products = selenium.find_elements(By.XPATH, '//td[@class="product-name"]/a')
        basket_price_products = selenium.find_elements(By.XPATH, '//td[@class="product-price"]')
        count = len(basket_name_products)
        with allure.step(f"Количество товаров в корзине: {count}"):
            for position in range(count):
                basket_name_product = basket_name_products[position].text
                basket_price_product = basket_price_products[position].text
                basket_price_product = normal_price_product(basket_price_product)
                basket_name_product = basket_name_product.upper()
                if ('ПИЦЦА' in basket_name_product) and ('ПИЦЦА' in name_product):
                    with allure.step(f"Товар №{position + 1}"):
                        with allure.step("Добавленный товар"):
                            name_product = normal_name_pizza(name_product)
                        with allure.step("Товар в корзине"):
                            basket_name_product = normal_name_pizza(basket_name_product)
                        check_name_product_add_basket(name_product, basket_name_product)
                        check_price_product(price_product, basket_price_product)
                elif ('ДЕСЕРТ' in basket_name_product) and ('ДЕСЕРТ' in name_product):
                    with allure.step(f"Товар №{position + 1}"):
                        with allure.step("Добавленный товар"):
                            name_product = normal_name_dessert(name_product)
                        with allure.step("Товар в корзине"):
                            basket_name_product = normal_name_dessert(basket_name_product)
                        check_name_product_add_basket(name_product, basket_name_product)
                        check_price_product(price_product, basket_price_product)
