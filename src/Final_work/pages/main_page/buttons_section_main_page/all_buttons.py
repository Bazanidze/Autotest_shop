import time

import allure
from selenium.webdriver.common.by import By


def button_basket(selenium):
    with allure.step('Нажатие на кнопку "Корзина" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Корзина")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Корзина"'):
            time.sleep(1)


def button_main(selenium):
    with allure.step('Нажатие на кнопку "Главная" в разделах сайта'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "Главная")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Главная"'):
            time.sleep(1)


def button_menu(selenium):
    with allure.step('Нажатие на кнопку "Меню" в разделах сайта'):
        selenium.find_element(By.XPATH, '//a[contains(text(), "Меню")]').click()
        with allure.step('Ожидание загрузки страницы "Меню"'):
            time.sleep(1)


def button_place_order(selenium):
    with allure.step('Нажатие на кнопку "Оформление заказа" в разделах сайта'):
        selenium.find_element(By.XPATH, '//a[contains(text(), "Оформление заказа")]').click()
        with allure.step('Ожидание загрузки страницы "Оформление заказа"'):
            time.sleep(1)


def button_my_account(selenium):
    with allure.step('Нажатие на кнопку "Мой аккаунт" в разделах сайта'):
        selenium.find_element(By.XPATH, '//a[contains(text(), "Мой аккаунт")]').click()
        with allure.step('Ожидание загрузки страницы "Мой аккаунт"'):
            time.sleep(1)
