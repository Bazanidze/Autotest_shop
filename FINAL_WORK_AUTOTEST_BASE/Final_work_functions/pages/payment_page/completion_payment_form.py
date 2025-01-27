import allure

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def completion_payment_form(selenium):
    first_name = "Иван"
    last_name = "Иванов"
    street_house = "ул. Иванова, д. 5"
    city = "г. Иваново"
    state = "Ивановская обл."
    postcode = "111111"
    number_phone = "81111111212"
    email_address = selenium.find_element(By.CSS_SELECTOR, 'input[type="email"]')
    email_address = email_address.get_attribute("value")
    with allure.step("Заполнение страницы оформления заказа:"):
        with allure.step(f'Заполнение поля ввода "Имя": {first_name}'):
            selenium.find_element(By.ID, "billing_first_name").send_keys(first_name)

        with allure.step(f'Заполнение поля ввода "Фамилия": {last_name}'):
            selenium.find_element(By.ID, "billing_last_name").send_keys(last_name)

        with allure.step(f'Заполнение поля ввода "Улица, дом": {street_house}'):
            selenium.find_element(By.ID, "billing_address_1").send_keys(street_house)

        with allure.step(f'Заполнение поля ввода "Город": {city}'):
            selenium.find_element(By.ID, "billing_city").send_keys(city)

        with allure.step(f'Заполнение поля ввода "Область": {state}'):
            selenium.find_element(By.ID, "billing_state").send_keys(state)

        with allure.step(f'Заполнение поля ввода "Почтовый индекс": {postcode}'):
            selenium.find_element(By.ID, "billing_postcode").send_keys(postcode)

        with allure.step(f'Заполнение поля ввода "Телефон": {number_phone}'):
            selenium.find_element(By.ID, "billing_phone").send_keys(number_phone)

        with allure.step("Выбор даты заказа на завтра"):
            action_chains = webdriver.ActionChains(selenium)
            button_calendar = selenium.find_element(By.ID, "order_date")
            action_chains.move_to_element(button_calendar).move_by_offset(
                xoffset=250, yoffset=0
            ).click().send_keys(Keys.ARROW_RIGHT + Keys.ENTER).perform()
            action_chains.release()

        with allure.step('Выбор способа оплаты: "Оплата при доставке"'):
            selenium.find_element(
                By.XPATH, '(//input[@class="input-radio"])[2]'
            ).click()

        with allure.step(
            'Выбор чекбокса: "Ознакомился с условиями использования веб-сайта и согласен с ними"'
        ):
            selenium.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()

        with allure.step('Клик на кнопку "Оформить заказ"'):
            selenium.find_element(By.ID, "place_order").click()

        personal_info = selenium.find_element(By.XPATH, "(//address)[1]")
        personal_info = personal_info.text
        entered_data = (
            first_name
            + " "
            + last_name
            + "\n"
            + street_house
            + "\n"
            + city
            + "\n"
            + state
            + "\n"
            + postcode
            + "\n"
            + number_phone
            + "\n"
            + email_address
        )
        with allure.step("Проверка: Личных данных после оформления заказа"):
            assert (personal_info == entered_data) is True
        pass
