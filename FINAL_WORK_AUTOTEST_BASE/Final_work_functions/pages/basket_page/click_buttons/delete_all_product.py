import time

import allure
from selenium.webdriver.common.by import By


def delete_all_product(selenium):
    with allure.step("Удаление всего товара из корзины"):
        delete_product_basket = selenium.find_elements(
            By.XPATH, '(//a[@class="remove"])'
        )
        count = len(delete_product_basket)
        for position in range(count):
            selenium.find_element(By.XPATH, '(//a[@class="remove"])[1]').click()
            time.sleep(1.5)
