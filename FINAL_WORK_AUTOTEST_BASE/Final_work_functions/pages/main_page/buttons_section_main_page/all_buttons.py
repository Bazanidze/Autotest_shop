import time

import allure
from selenium.webdriver.common.by import By


def button_basket(selenium):
    with allure.step('Клик на кнопку "Корзина" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Корзина")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Корзина"'):
            time.sleep(1)


def button_main(selenium):
    with allure.step('Клик на кнопку "Главная" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Главная")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Главная"'):
            time.sleep(1)


def button_menu(selenium):
    with allure.step('Клик на кнопку "Меню" в разделах сайта'):
        selenium.find_element(By.XPATH, '//a[contains(text(), "Меню")]').click()
        with allure.step('Ожидание загрузки страницы "Меню"'):
            time.sleep(1)


def button_place_order(selenium):
    with allure.step('Клик на кнопку "Оформление заказа" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Оформление заказа")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Оформление заказа"'):
            time.sleep(1)


def button_my_account(selenium):
    with allure.step('Клик на кнопку "Мой аккаунт" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Мой аккаунт")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Мой аккаунт"'):
            time.sleep(1)


def button_bonus_programm(selenium):
    with allure.step('Клик на кнопку "Бонусная Программа" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Бонусная программа")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Бонусная программа"'):
            time.sleep(1)
