import time

import pytest
import allure


class OpenPage:
    @pytest.fixture()
    def main_page(self, selenium):
        with allure.step("Открытие главной страницы"):
            selenium.get("https://pizzeria.skillbox.cc/")
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(3)

    @pytest.fixture()
    def pizza_page(self, selenium):
        with allure.step("Открытие страницы пиццы"):
            selenium.get(
                "https://pizzeria.skillbox.cc/product/%d0%bf%d0%b8%d1%86%d1%86%d0%b0-%d1%80%d0%b0%d0%b9/"
            )
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(1)

    @pytest.fixture()
    def basket_page(self, selenium):
        with allure.step("Открытие страницы 'Корзина'"):
            selenium.get("https://pizzeria.skillbox.cc/cart/")
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(1)

    @pytest.fixture()
    def desserts_page(self, selenium):
        with allure.step("Открытие страницы 'Десерты'"):
            selenium.get("https://pizzeria.skillbox.cc/product-category/menu/deserts/")
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(1)

    @pytest.fixture()
    def payment_page(self, selenium):
        with allure.step("Открытие страницы 'Оформления заказа'"):
            selenium.get("https://pizzeria.skillbox.cc/checkout/")
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(1)

    @pytest.fixture()
    def my_account_page(self, selenium):
        with allure.step("Открытие страницы 'Мой аккаунт'"):
            selenium.get("https://pizzeria.skillbox.cc/my-account/")
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(1)

    @pytest.fixture()
    def registration_page(self, selenium):
        with allure.step("Открытие страницы 'Регистрация'"):
            selenium.get("https://pizzeria.skillbox.cc/register/")
            with allure.step("Ожидание загрузки страницы"):
                time.sleep(1)
