import allure
from selenium.webdriver.common.by import By

from src.Final_work.normal_name_elements.all_normal_name import normal_name_option_pizza


def select_option_add_basket(selenium):
    with allure.step('Открытие списка дополнительных опций'):
        selenium.find_element(By.CSS_SELECTOR, 'span select[name="board_pack"]').click()
        with allure.step('Выбор дополнительной опции'):
            name_select_options = selenium.find_element(By.XPATH, '(//option)[2]')
            name_select_options.click()
        with allure.step(f'Выбрана опция: "{name_select_options.text}"'):
            name_select_options = normal_name_option_pizza(name_select_options.text)
    return name_select_options
