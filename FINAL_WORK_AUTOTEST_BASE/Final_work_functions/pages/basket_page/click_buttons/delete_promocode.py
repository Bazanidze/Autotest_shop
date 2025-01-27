import time

import allure

from selenium.webdriver.common.by import By


def delete_promocode(selenium):
    with allure.step("Удаление промокода"):
        selenium.find_element(By.XPATH, '//a[contains(text(), "Удалить")]').click()
        time.sleep(1.5)
