import random

import allure
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.asserts.all_asserts import (
    check_registration_completed,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.authorization_page.click_buttons.button_registration import (
    button_registration,
)


def correct_registration_account(selenium):
    with allure.step("Форма регистрации:"):
        with allure.step('Корректное заполнение формы "Регистрация"'):
            number_random = random.randrange(1, 100000)
            with allure.step('Заполнение поля ввода "Имя пользователя"'):
                user_name_enter = "Niki" + str(number_random) + "for"
                with allure.step(f"Имя пользователя: {user_name_enter}"):
                    selenium.find_element(
                        By.XPATH, '(//form[@method="post"]//input)[1]'
                    ).send_keys(user_name_enter)
            with allure.step('Заполнение поля ввода "Адрес почты"'):
                email_enter = "tes" + str(number_random) + "up@mail.ru"
                with allure.step(f"Адрес почты: {email_enter}"):
                    selenium.find_element(
                        By.XPATH, '(//form[@method="post"]//input)[2]'
                    ).send_keys(email_enter)
            with allure.step('Заполнение поля ввода "Пароль"'):
                password_enter = "VabloPablo123"
                with allure.step(f"Пароль: {password_enter}"):
                    selenium.find_element(
                        By.XPATH, '(//form[@method="post"]//input)[3]'
                    ).send_keys(password_enter)
        button_registration(selenium)
        check_registration_completed(selenium)
