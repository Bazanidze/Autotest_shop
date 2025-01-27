import allure
from selenium.webdriver.common.by import By


def button_basket_pizza_page(selenium):
    with allure.step('Клик кнопки "В корзину"'):
        selenium.find_element(
            By.XPATH, '//button[contains(text(), "В корзину")]'
        ).click()
