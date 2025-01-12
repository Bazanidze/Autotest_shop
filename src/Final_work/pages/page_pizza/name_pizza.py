import allure
from selenium.webdriver.common.by import By


def name_pizza_page_pizza(selenium):
    with allure.step('Открытие страницы пиццы'):
        name_page_pizza = selenium.find_element(By.CSS_SELECTOR, 'h1[class="product_title entry-title"]').text
        name_page_pizza = name_page_pizza.upper()
        return name_page_pizza
