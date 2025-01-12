import allure

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def clear_payment_form(selenium):
    city = 'г. Иваново'
    state = 'Ивановская обл.'
    postcode = '111111'
    number_phone = '81111111212'
    action_chains = webdriver.ActionChains(selenium)
    with allure.step('Очистка страницы оформления заказа:'):
        with allure.step('Очистка поля ввода "Имя"'):
            first_name = selenium.find_element(By.ID, 'billing_first_name')
            action_chains.click(first_name).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()

        with allure.step('Очистка поля ввода "Фамилия"'):
            last_name = selenium.find_element(By.ID, 'billing_last_name')
            action_chains.click(last_name).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()

        with allure.step('Очистка поля ввода "Улица, дом"'):
            street_house = selenium.find_element(By.ID, 'billing_address_1')
            action_chains.click(street_house).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()

        with allure.step('Очистка поля ввода "Город"'):
            city = selenium.find_element(By.ID, 'billing_city')
            action_chains.click(city).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()

        with allure.step('Очистка поля ввода "Область"'):
            state = selenium.find_element(By.ID, 'billing_state')
            action_chains.click(state).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()

        with allure.step('Очистка поля ввода "Почтовый индекс"'):
            postcode = selenium.find_element(By.ID, 'billing_postcode')
            action_chains.click(postcode).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()

        with allure.step('Очистка поля ввода "Телефон"'):
            number_phone = selenium.find_element(By.ID, 'billing_phone')
            action_chains.click(number_phone).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)\
                .send_keys(Keys.BACKSPACE).perform()
            action_chains.release()
