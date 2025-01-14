import allure
from selenium.webdriver.common.by import By


def button_registration(selenium):
    with allure.step('Клик на кнопку "Зарегистрироваться"'):
        selenium.find_element(By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()
