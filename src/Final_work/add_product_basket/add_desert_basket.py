import allure
from selenium.webdriver.common.by import By

from src.Final_work.asserts.all_asserts import check_name_product_add_basket
from src.Final_work.pages.basket_page.normal_name_product_basket import normal_name_product_basket

from src.Final_work.normal_name_elements.all_normal_name import normal_name_dessert
from src.Final_work.pages.main_page.buttons_section_main_page.all_buttons import button_basket


def add_dessert_basket(selenium):
    with allure.step('Выбор десерта'):
        name_dessert = selenium.find_element(By.XPATH, '(//div[@class="wc-products"]//h3)[1]')
    name_dessert = normal_name_dessert(name_dessert.text)
    with allure.step(f'Добавление десерта: {name_dessert}, в корзину'):
        selenium.find_element(By.XPATH, '(//a[contains(text(), "В корзину")])[1]').click()

    button_basket(selenium)
    basket_name_dessert = normal_name_product_basket(selenium)
    check_name_product_add_basket(name_dessert, basket_name_dessert)
