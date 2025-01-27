import time

import allure
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.check_product_basket import (
    check_product_basket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.buttons_section_main_page.all_buttons import (
    button_basket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.price_products.normal_price_product_and_option import (
    normal_price_product,
)


def add_pizza_basket(selenium):
    with allure.step("Выбор пиццы"):
        time.sleep(0.5)
        name_pizza = selenium.find_element(
            By.XPATH, '(//section[@id="product1"]' '//li[@aria-hidden="false"]//h3)[2]'
        ).text

        price_pizza = selenium.find_element(
            By.XPATH,
            '(//section[@id="product1"]//li[@aria-hidden="false"]'
            '//span[@class="price"])[2]',
        ).text
        price_pizza = normal_price_product(price_pizza)

        with allure.step(
            f"Добавление пиццы: '{name_pizza}' стоимостью {price_pizza} в корзину"
        ):
            selenium.find_element(
                By.XPATH, '//li[@aria-hidden="false"]//a[@href="?add-to-cart=423"]'
            ).click()

    button_basket(selenium)
    name_pizza = name_pizza.upper()
    check_product_basket(selenium, name_pizza, price_pizza)
