import allure
from selenium.webdriver.common.by import By


def button_proceed_payment(selenium):
    with allure.step('Клик на кнопку "Перейти к оплате"'):
        selenium.find_element(
            By.XPATH, '//a[contains(text(), "ПЕРЕЙТИ К ОПЛАТЕ")]'
        ).click()
