import allure
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.price_products.normal_price_product_and_option import (
    normal_price_product,
)


def check_name_product_add_basket(name_product, basket_name_product):
    with allure.step("Проверка: Выбранный товар, находится в корзине"):
        assert (name_product == basket_name_product) is True


def check_name_option_pizza_add_basket(name_select_options, basket_name_option_pizza):
    with allure.step("Проверка: Опция пиццы в корзине == опции добавленной пиццы"):
        assert (name_select_options == basket_name_option_pizza) is True


def check_quantity_product(value, int_element_attribute_value):
    with allure.step("Проверка: Изменения количества товара в корзине"):
        assert (value == int_element_attribute_value) is True


def check_go_pizza_page(name_page_pizza, name_pizza_main_page):
    with allure.step(f"Проверка: Открыта страница, выбранной пиццы: {name_page_pizza}"):
        assert (name_page_pizza == name_pizza_main_page) is True


def check_empty_basket(selenium):
    with allure.step("Проверка: Корзина пуста"):
        text_empty_basket = "Корзина пуста."
        assert (
            text_empty_basket
            == selenium.find_element(
                By.XPATH, "//p[contains(text(), " '"Корзина пуста.")]'
            ).text
        ) is True


def check_menu_page(selenium):
    with allure.step('Проверка: Открыта страница "Меню"'):
        text_h1_menu_page = "МЕНЮ"
        assert (
            text_h1_menu_page
            == selenium.find_element(By.XPATH, '//h1[contains(text(), "Меню")]').text
        ) is True


def check_desserts_page(selenium):
    with allure.step('Проверка: Открыта страница "Десерты"'):
        text_h1_desserts_page = "ДЕСЕРТЫ"
        assert (
            text_h1_desserts_page
            == selenium.find_element(
                By.XPATH, "//h1[contains(text(), " '"Десерты")]'
            ).text
        ) is True


def check_payment_no_authorized(selenium):
    with allure.step(
        "Проверка: Не авторизованный пользователь не может продолжить оформление заказа"
    ):
        assert selenium.find_element(
            By.XPATH, '//a[contains(text(), "Авторизуйтесь")]'
        ).is_displayed()


def check_open_my_account_page_no_authorized(selenium):
    with allure.step('Проверка: Открыта страница "Мой аккаунт" без авторизации'):
        text_h2_menu_page = "МОЙ АККАУНТ"
        assert (
            text_h2_menu_page
            == selenium.find_element(By.CSS_SELECTOR, 'h2[class="post-title"]').text
        ) is True


def check_open_registration_page(selenium):
    with allure.step('Проверка: Открыта страница "Регистрация"'):
        text_h2_registration = "РЕГИСТРАЦИЯ"
        assert (
            text_h2_registration
            == selenium.find_element(By.XPATH, '//h2[@class="post-title"]').text
        ) is True


def check_registration_completed(selenium):
    with allure.step("Проверка: Пользователь зарегистрирован"):
        assert selenium.find_element(
            By.XPATH, '//div[contains(text(), "Регистрация завершена")]'
        ).is_displayed()


def check_authorized(name_user, authorized_name_user):
    with allure.step("Проверка: Пользователь авторизован"):
        assert (name_user == authorized_name_user) is True


def check_price_product(price_product, basket_price_product):
    with allure.step("Проверка: Цена товара совпадает с ценой в корзине"):
        assert (price_product == basket_price_product) is True


def check_summ_products_basket(selenium):
    with allure.step(
        "Проверка: Итоговая сумма товаров в корзине отображается корректно"
    ):
        basket_price_products = selenium.find_elements(
            By.XPATH, '//td[@class="product-price"]'
        )
        count = len(basket_price_products)
        total_summ_products = 0
        for position in range(count):
            basket_price_product = basket_price_products[position].text
            basket_price_product = normal_price_product(basket_price_product)
            total_summ_products += basket_price_product
        summ_products = selenium.find_element(
            By.CSS_SELECTOR, 'td[data-title="Сумма"]'
        ).text
        summ_products = normal_price_product(summ_products)
        assert (total_summ_products == summ_products) is True
        return summ_products


def check_summ_after_payment(selenium, summ_products):
    with allure.step(
        "Проверка: После оформления заказа, сумма товаров указана корректно"
    ):
        end_total_summ = selenium.find_element(
            By.XPATH, '//th[contains(text(), "Total")]/following-sibling::td'
        ).text
        end_total_summ = normal_price_product(end_total_summ)
        assert (summ_products == end_total_summ) is True
