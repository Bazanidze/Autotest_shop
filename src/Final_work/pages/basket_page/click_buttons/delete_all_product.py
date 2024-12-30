import allure
from selenium.webdriver.common.by import By


def delete_all_product(selenium):
    with allure.step('Удаление всего товара из корзины'):
        selenium.get('https://pizzeria.skillbox.cc/cart/')
        delete_product_basket = selenium.find_elements(By.CSS_SELECTOR, 'a[class="remove"]')
        count = len(delete_product_basket)
        for position in range(count):
            delete_product_basket[position].click()
