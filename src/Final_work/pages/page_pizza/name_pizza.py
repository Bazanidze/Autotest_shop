import allure
from selenium.webdriver.common.by import By

from src.Final_work.normal_name_elements.all_normal_name import normal_name_pizza


def name_pizza_page_pizza(selenium):
    with allure.step('Открылась страница пиццы'):
        name_page_pizza = selenium.find_element(By.CSS_SELECTOR, 'h1[class="product_title entry-title"]')
        name_page_pizza = normal_name_pizza(name_page_pizza.text)
        return name_page_pizza
