import allure
from selenium.webdriver.common.by import By


def main_page_slider_pizza_names(selenium):
    with allure.step("Проверка названий пицц в слайдере на главной странице"):
        pizza_main_page = selenium.find_elements(By.XPATH, '//section[@id="product1"]//li[@aria-hidden="false"]//h3')
        count = len(pizza_main_page)
        name_pizza_1 = 'ПИЦЦА «4 В 1»'
        name_pizza_2 = 'ПИЦЦА «КАК У БАБУШКИ»'
        name_pizza_3 = 'ПИЦЦА «РАЙ»'
        name_pizza_4 = 'ПИЦЦА «ВЕТЧИНА И ГРИБЫ»'
        for position in range(count):
            text_pizza = pizza_main_page[position].text
            assert ((name_pizza_1 in text_pizza) or (name_pizza_2 in text_pizza) or (name_pizza_3 in text_pizza) or (
                        name_pizza_4 in text_pizza)) is True
