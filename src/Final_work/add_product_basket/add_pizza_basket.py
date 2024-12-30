import allure
from selenium.webdriver.common.by import By

from src.Final_work.asserts.all_asserts import check_name_product_add_basket
from src.Final_work.pages.basket_page.normal_name_product_basket import normal_name_product_basket

from src.Final_work.normal_name_elements.all_normal_name import normal_name_pizza
from src.Final_work.pages.main_page.buttons_section_main_page.all_buttons import button_basket


def add_pizza_basket(selenium):
    with allure.step("Выбор пиццы"):
        name_pizza = selenium.find_element(By.XPATH, '(//section[@id="product1"]'
                                                     '//li[@aria-hidden="false"]//h3)[2]').text
    name_pizza = normal_name_pizza(name_pizza)

    with allure.step(f"Добавление пиццы: '{name_pizza}' в корзину"):
        selenium.find_element(By.XPATH, '//li[@aria-hidden="false"]//a[@href="?add-to-cart=423"]').click()

    button_basket(selenium)

    basket_name_pizza = normal_name_product_basket(selenium)

    check_name_product_add_basket(name_pizza, basket_name_pizza)
