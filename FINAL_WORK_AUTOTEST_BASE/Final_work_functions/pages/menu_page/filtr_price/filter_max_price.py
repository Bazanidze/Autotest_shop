import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.price_products.normal_price_product_and_option import (
    normal_price_product,
)


def filter_max_price(selenium):
    with allure.step('Изменение фильтра "Максимальная цена" товара'):
        right_button_filter_price = selenium.find_element(
            By.XPATH, '(//span[contains(@class,"ui-corner-all")])[2]'
        )
        action_chains = webdriver.ActionChains(selenium)
        action_chains.click_and_hold(right_button_filter_price).move_by_offset(
            xoffset=-230, yoffset=0
        ).perform()
        action_chains.release()

    with allure.step('Клик на кнопку "Применить"'):
        selenium.find_element(
            By.XPATH, '//button[contains(text(), "Применить")]'
        ).click()
    max_price_filter = selenium.find_element(
        By.XPATH, '(//div[@class="price_label"]/span)[2]'
    ).text

    with allure.step(f'Фильтр "Максимальная цена": {max_price_filter}'):
        max_price_filter = max_price_filter[0:-1]
    all_products = selenium.find_elements(
        By.CSS_SELECTOR, 'div[class="wc-products"] bdi'
    )
    count_products = len(all_products)

    with allure.step(f"Количество товаров: {count_products}"):

        with allure.step("Проверка цены товаров"):
            for position in range(count_products):
                price_product = all_products[position].text

                with allure.step(f"Цена {position + 1} товара: {price_product}"):
                    price_product = normal_price_product(price_product)

                    with allure.step(
                        "Проверка: Товар с ценной, не превышает, максимальную цену в фильтре"
                    ):
                        assert (float(price_product) <= int(max_price_filter)) is True
