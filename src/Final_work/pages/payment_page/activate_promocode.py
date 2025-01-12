import time

import allure
from selenium.webdriver.common.by import By

from src.Final_work.price_products.normal_price_product_and_option import normal_price_product


def activate_promocode(selenium, summ_products, promocode):
    with allure.step("Ввод промокода"):
        with allure.step("Клик на ссылку: 'Нажмите для ввода купона'"):
            selenium.find_element(By.CSS_SELECTOR, 'a[class="showcoupon"]').click()
        with allure.step(f"Ввод купона в поле ввода: '{promocode}'"):
            selenium.find_element(By.ID, 'coupon_code').send_keys(promocode)
            selenium.find_element(By.CSS_SELECTOR, 'button[name="apply_coupon"]').click()
            time.sleep(0.5)
        with allure.step("Проверка введённого промокода"):
            if promocode == 'GIVEMEHALYAVA':
                with allure.step("Уведомление об активации промокода есть"):
                    text_allert = 'Coupon code applied successfully.'
                    allert_promocode = selenium.find_element(By.CSS_SELECTOR, 'div[role="alert"]').text
                    assert (text_allert == allert_promocode) is True
                    with allure.step(f"Активирован промокод: '{promocode}' со скидкой 10% процентов "):
                        discount = summ_products / 100 * 10
            else:
                with allure.step("Уведомление: 'Неверный купон'"):
                    text_allert = 'Неверный купон.'
                    allert_promocode = selenium.find_element(By.CSS_SELECTOR, 'ul[role="alert"]').text
                    assert (text_allert == allert_promocode) is True
                    with allure.step(f"Введён не верный промокод: '{promocode}'"):
                        discount = 0
            summ_products = summ_products - discount
            summ_payment_products = selenium.find_element(By.CSS_SELECTOR, 'tr[class="order-total"] bdi').text
            summ_payment_products = normal_price_product(summ_payment_products)
            with allure.step(f"Проверка: промокод '{promocode}' сделает скидку на {discount} руб.  "):
                with allure.step(f"Итоговая стоимость товара: {summ_products} руб."):
                    assert (summ_products == summ_payment_products) is True
            return summ_products
