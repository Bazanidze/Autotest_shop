from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.normal_name_elements.all_normal_name import (
    basket_normal_name_option_pizza,
)


def check_option_add_pizza(selenium):
    basket_name_option_pizza = selenium.find_element(
        By.XPATH, '(//dd[@class="variation-"])'
    )
    basket_name_option_pizza = basket_normal_name_option_pizza(
        basket_name_option_pizza.text
    )
    return basket_name_option_pizza
