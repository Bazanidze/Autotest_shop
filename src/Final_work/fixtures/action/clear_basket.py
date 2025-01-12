import time

import pytest
import allure
from selenium.webdriver.common.by import By

from src.Final_work.pages.main_page.buttons_section_main_page.all_buttons import button_basket


class ClearBasket:
    @pytest.fixture()
    def clear_basket(self, selenium):
        with allure.step('Очистка корзины'):
            button_basket(selenium)
            delete_product_basket = selenium.find_elements(By.XPATH, '(//a[@class="remove"])')
            count = len(delete_product_basket)
            for position in range(count):
                selenium.find_element(By.XPATH, '(//a[@class="remove"])[1]').click()
                time.sleep(1.5)
                pass
