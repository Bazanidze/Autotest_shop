import pytest
import allure
from selenium.webdriver.common.by import By


class DeAuthorized:
    @pytest.fixture()
    def de_authorized(self, selenium):
        with allure.step("Выход с аккаунта"):
            selenium.get("https://pizzeria.skillbox.cc/")
            selenium.find_element(By.CSS_SELECTOR, 'a[class="logout"]').click()
