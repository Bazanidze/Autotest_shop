import time
import random

import allure
from selenium.webdriver.common.by import By


def apply_bonus_programm(selenium):
    number_phone = ''
    name_user = 'Nikifor'
    for _ in range(10):
        number_phone += str(random.randrange(0, 9))
    with allure.step('Заполнение полей ввода на странице "Бонусная программа":'):
        with allure.step(f'Заполнение поля ввода "Имя": {name_user}'):
            selenium.find_element(By.ID, 'bonus_username').send_keys(name_user)
        with allure.step(f'Заполнение поля ввода "Телефон": 8{number_phone}'):
            selenium.find_element(By.ID, 'bonus_phone').send_keys('8' + number_phone)
        with allure.step('Клик на кнопку "Оформить карту"'):
            selenium.find_element(By.XPATH, '//button[contains(text(), "Оформить карту")]').click()
            time.sleep(0.5)
        with allure.step('Подтверждение всплывающего окна'):
            window_allert = selenium.switch_to.alert
            window_allert.accept()
    time.sleep(2)
    with allure.step('Проверка: Карта оформлена'):
        text_you_card_apply = 'Ваша карта оформлена!'
        card_apply = selenium.find_element(By.CSS_SELECTOR, 'div[id="bonus_main"] h3').text
        assert (text_you_card_apply == card_apply) is True
