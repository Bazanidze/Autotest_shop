import allure
from selenium.webdriver.common.by import By


def check_name_product_add_basket(name_product, basket_name_product):
    with allure.step("Проверка: Выбранный товар, находится в корзине"):
        assert (name_product == basket_name_product) is True


def check_name_option_pizza_add_basket(name_select_options, basket_name_option_pizza):
    with allure.step('Проверка: Опция пиццы в корзине == опции добавленной пиццы'):
        assert (name_select_options == basket_name_option_pizza) is True


def check_quantity_product(value, int_element_attribute_value):
    with allure.step('Проверка: Изменения количества товара в корзине'):
        assert (value == int_element_attribute_value) is True


def check_go_pizza_page(name_page_pizza, name_pizza_main_page):
    with allure.step('Проверка: Название пиццы, открытой страницы, соответсвует, '
                     'названию выбранной пицце на главной странице'):
        assert (name_page_pizza == name_pizza_main_page) is True


def check_empty_basket(selenium):
    with allure.step('Проверка: Корзина пуста'):
        text_empty_basket = 'Корзина пуста.'
        assert (text_empty_basket == selenium.find_element(By.XPATH, '//p[contains(text(), '
                                                                     '"Корзина пуста.")]').text) is True


def check_menu_page(selenium):
    with allure.step('Проверка: Открыта страница "Меню"'):
        text_h1_menu_page = 'МЕНЮ'
        assert (text_h1_menu_page == selenium.find_element(By.XPATH, '//h1[contains(text(), "Меню")]').text) is True


def check_desserts_page(selenium):
    with allure.step('Проверка: Открыта страница "Десерты"'):
        text_h1_desserts_page = 'ДЕСЕРТЫ'
        assert (text_h1_desserts_page == selenium.find_element(By.XPATH, '//h1[contains(text(), '
                                                                         '"Десерты")]').text) is True


def check_payment_no_authorized(selenium):
    with allure.step('Проверка: Не авторизованный пользователь не может продолжить оформление заказа'):
        assert selenium.find_element(By.XPATH, '//a[contains(text(), "Авторизуйтесь")]').is_displayed()


def check_open_my_account_page_no_authorized(selenium):
    with allure.step('Проверка: Открыта страница "Мой аккаунт" без авторизации'):
        text_h2_menu_page = 'МОЙ АККАУНТ'
        assert (text_h2_menu_page == selenium.find_element(By.CSS_SELECTOR, 'h2[class="post-title"]').text) is True


def check_open_registration_page(selenium):
    with allure.step('Проверка: Открыта страница "Регистрация"'):
        text_h2_registration = 'РЕГИСТРАЦИЯ'
        assert (text_h2_registration == selenium.find_element(By.XPATH, '//h2[@class="post-title"]').text) is True


def check_registration_completed(selenium):
    with allure.step('Проверка: Пользователь зарегистрирован'):
        assert selenium.find_element(By.XPATH, '//div[contains(text(), "Регистрация завершена")]').is_displayed()
