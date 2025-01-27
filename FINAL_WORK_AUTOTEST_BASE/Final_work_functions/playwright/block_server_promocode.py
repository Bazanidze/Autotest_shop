import time

import allure

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.price_products.normal_price_product_and_option import (
    normal_price_product,
)


def block_server(playwright, page):
    with allure.step("Запуск браузера"):
        chromium = playwright.chromium
        chromium.launch()
    with allure.step("Блокировка ссылки на активацию промокода"):
        page.route("**/?wc-ajax=apply_coupon", lambda route: route.abort())
    promocode = "GIVEMEHALYAVA"
    name_user = "Nikifor"
    password_user = "VabloPablo123"
    page.goto("https://pizzeria.skillbox.cc/my-account/")
    with allure.step("Вход в аккаунт"):
        with allure.step('Заполнение полей ввода на странице "Авторизация":'):
            with allure.step('Заполнение поля ввода "Имя пользователя": ' + name_user):
                page.query_selector('[id="username"]').fill(name_user)
            with allure.step('Заполнение поля ввода "Пароль": ' + password_user):
                page.query_selector('[id="password"]').fill(password_user)
        with allure.step('Клик на кнопку "ВОЙТИ"'):
            page.query_selector('button[value="Войти"]').click()
    with allure.step('Клик на кнопку "Корзина" в разделах сайта'):
        page.query_selector('(//a[contains(text(), "Корзина")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Корзина"'):
            time.sleep(1)
    price_pizza = page.query_selector(
        '(//span[@class="woocommerce-Price-amount amount"]) [2]'
    ).inner_text()
    with allure.step(f"Общая стоимость товара в корзине {price_pizza}"):
        price_pizza = normal_price_product(price_pizza)
    with allure.step('Клик на кнопку "Перейти к оплате"'):
        page.query_selector('//a[contains(text(), "ПЕРЕЙТИ К ОПЛАТЕ")]').click()
    with allure.step("Ввод промокода"):
        with allure.step("Клик на ссылку: 'Нажмите для ввода купона'"):
            page.query_selector('a[class="showcoupon"]').click()
        with allure.step(f"Ввод купона в поле ввода: '{promocode}'"):
            page.query_selector("[id=coupon_code]").fill(promocode)
            page.query_selector('button[name="apply_coupon"]').click()
            time.sleep(0.5)
    summ_payment_products = page.query_selector(
        'tr[class="order-total"] bdi'
    ).inner_text()
    summ_payment_products = normal_price_product(summ_payment_products)
    with allure.step(f"Проверка: Промокод '{promocode}' не применился"):
        with allure.step(f"Итоговая стоимость товара: {summ_payment_products} руб."):
            assert (price_pizza == summ_payment_products) is True
            time.sleep(3)
    with allure.step('Клик на кнопку "Корзина" в разделах сайта'):
        page.query_selector('(//a[contains(text(), "Корзина")])[1]').click()
        with allure.step('Ожидание загрузки страницы "Корзина"'):
            time.sleep(1)
    with allure.step("Удаление всего товара из корзины"):
        delete_product_basket = page.query_selector_all('(//a[@class="remove"])')
        count = len(delete_product_basket)
        for position in range(count):
            page.query_selector('(//a[@class="remove"])[1]').click()
            time.sleep(1.5)
