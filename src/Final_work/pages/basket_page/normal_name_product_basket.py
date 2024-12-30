import allure
from selenium.webdriver.common.by import By

from src.Final_work.normal_name_elements.all_normal_name import normal_name_pizza, normal_name_dessert


def normal_name_product_basket(selenium):
    with allure.step("Товар, добавленный в корзину"):
        basket_name_product = selenium.find_element(By.CSS_SELECTOR, 'td[class="product-name"] a').text
        if 'Пицца' in basket_name_product:
            basket_name_product = normal_name_pizza(basket_name_product)
        elif 'Десерт' in basket_name_product:
            basket_name_product = normal_name_dessert(basket_name_product)
        return basket_name_product
