import time

import allure
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.check_product_basket import check_product_basket
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.buttons_section_main_page.all_buttons import \
    button_basket
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.price_products.normal_price_product_and_option import \
    normal_price_product


def add_dessert_basket(selenium):
    with allure.step('Выбор десерта'):
        time.sleep(0.5)
        name_dessert = selenium.find_element(By.XPATH, '(//div[@class="wc-products"]//h3)[1]').text
        price_dessert = selenium.find_element(By.XPATH, '(//div[@class="price-cart"]//span[@class="price"])[1]').text
        price_dessert = normal_price_product(price_dessert)

        with allure.step(f"Добавление десерта: '{name_dessert}' стоимостью {price_dessert} в корзину"):
            selenium.find_element(By.XPATH, '(//a[contains(text(), "В корзину")])[1]').click()

    button_basket(selenium)
    name_dessert = name_dessert.upper()
    check_product_basket(selenium, name_dessert, price_dessert)
