import pytest
import allure
from selenium.webdriver.common.by import By


class ClearBasket:
    @pytest.fixture()
    def clear_basket(self, selenium):
        with allure.step('Очистка корзины'):
            selenium.get('https://pizzeria.skillbox.cc/cart/')
            delete_product_basket = selenium.find_elements(By.CSS_SELECTOR, 'a[class="remove"]')
            count = len(delete_product_basket)
            for position in range(count):
                delete_product_basket[position].click()
