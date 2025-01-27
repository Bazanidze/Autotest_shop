import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.asserts.all_asserts import (
    check_quantity_product,
)


def reducing_product(selenium):
    with allure.step(
        'Уменьшение количества товара в корзине при нажатии кнопки "Вниз"'
    ):
        down_quantity = selenium.find_element(By.CSS_SELECTOR, 'input[type="number"]')
        value = int(down_quantity.get_attribute("value"))
        action_chains = webdriver.ActionChains(selenium)
        action_chains.move_to_element(down_quantity).move_by_offset(
            xoffset=15, yoffset=10
        ).click().perform()
        action_chains.release()
        value -= 1
        selenium.find_element(
            By.CSS_SELECTOR, 'button[value="Обновить корзину"]'
        ).click()
    check_quantity_product(value, int(down_quantity.get_attribute("value")))
    time.sleep(1.5)
