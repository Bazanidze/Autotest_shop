import allure

from playwright.sync_api import Playwright, Page

from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.add_product_basket.add_desert_basket import (
    add_dessert_basket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.add_product_basket.add_pizza_basket import (
    add_pizza_basket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.asserts.all_asserts import (
    check_go_pizza_page,
    check_name_option_pizza_add_basket,
    check_empty_basket,
    check_menu_page,
    check_desserts_page,
    check_payment_no_authorized,
    check_open_my_account_page_no_authorized,
    check_open_registration_page,
    check_summ_products_basket,
    check_summ_after_payment,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.fixtures.action.clear_basket import (
    ClearBasket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.fixtures.action.de_authorized import (
    DeAuthorized,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.fixtures.open_pages.pages import (
    OpenPage,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.normal_name_elements.all_normal_name import (
    normal_name_pizza,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.authorization_page.authorized_user import (
    authorized_user,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.authorization_page.click_buttons.button_registration import (
    button_registration,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.check_option_add_pizza import (
    check_option_add_pizza,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.check_product_basket import (
    check_product_basket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.click_buttons.delete_all_product import (
    delete_all_product,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.click_buttons.delete_promocode import (
    delete_promocode,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.click_buttons.increasing_product import (
    increasing_product,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.click_buttons.proceed_payment import (
    button_proceed_payment,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.basket_page.click_buttons.reducing_product import (
    reducing_product,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.bonus_programm_page.apply_bonus_programm import (
    apply_bonus_programm,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.buttons_section_main_page.all_buttons import (
    button_basket,
    button_menu,
    button_my_account,
    button_main,
    button_bonus_programm,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.main_page_slider_pizza.click_buttons\
    .click_left_slider_pizza import click_left_slider_pizza

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.main_page_slider_pizza.click_buttons\
    .click_right_slider_pizza import click_right_slider_pizza

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.main_page_slider_pizza\
    .main_page_slider_pizza import main_page_slider_pizza_names

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.main_page_slider_pizza.right_slider_pizza import (
    right_slider_pizza,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.menu_page.filtr_price.filter_max_price import (
    filter_max_price,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.menu_page.rubricator.select_desserts import (
    select_desserts_rubricator_menu,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.page_pizza.add_basket import (
    button_basket_pizza_page,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.page_pizza.name_pizza import (
    name_pizza_page_pizza,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.page_pizza.select_option_add_basket import (
    select_option_add_basket,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.payment_page.activate_promocode import (
    activate_promocode,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.payment_page.clear_payment_form import (
    clear_payment_form,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.payment_page.completion_payment_form import (
    completion_payment_form,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.registration_page.registration_account import (
    correct_registration_account,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.playwright.block_server_promocode import (
    block_server,
)
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.price_products.normal_price_product_and_option import (
    normal_price_product,
)


@allure.feature("Все тесты финальной работы. Автотесты на Python. Базовая часть")
class TestsTask1(OpenPage, ClearBasket, DeAuthorized):
    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title(
        "Тест-кейс №1: Проверка названий пицц в слайдере при загрузке главной страницы"
    )
    def test_case_1(self, selenium, main_page):
        main_page_slider_pizza_names(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title(
        "Тест-кейс №2: Добавление пиццы из слайдера в корзину и проверка, "
        "что добавлена верная пицца"
    )
    def test_case_2(self, selenium, main_page):
        add_pizza_basket(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title(
        "Тест-кейс №3: Проверка кнопок 'влево' и 'вправо' слайдера пицц на главной странице"
    )
    def test_case_3(self, selenium, clear_basket, main_page):
        click_right_slider_pizza(selenium)
        right_slider_pizza(selenium)
        click_left_slider_pizza(selenium)
        main_page_slider_pizza_names(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №4: Переход на страницу пиццы с главной страницы")
    def test_case_4(self, selenium, main_page):
        with allure.step("Выбор пиццы"):
            name_pizza = selenium.find_element(
                By.XPATH,
                '(//section[@id="product1"]' '//li[@aria-hidden="false"]//h3)[1]',
            )

        name_pizza_main_page = normal_name_pizza(name_pizza.text)

        with allure.step(f'Клик на выбранную пиццу: "{name_pizza_main_page}"'):
            name_pizza.click()

        name_page_pizza = name_pizza_page_pizza(selenium)
        name_page_pizza = normal_name_pizza(name_page_pizza)
        check_go_pizza_page(name_pizza_main_page, name_page_pizza)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №5: Добавление пиццы в корзину с дополнительной опцией")
    def test_case_5(self, selenium, pizza_page):
        name_page_pizza = name_pizza_page_pizza(selenium)
        name_select_options = select_option_add_basket(selenium)
        price_product = selenium.find_element(By.CSS_SELECTOR, 'p[class="price"]').text
        price_product = normal_price_product(price_product)
        button_basket_pizza_page(selenium)
        button_basket(selenium)
        check_product_basket(selenium, name_page_pizza, price_product)
        basket_name_option_pizza = check_option_add_pizza(selenium)
        check_name_option_pizza_add_basket(
            name_select_options, basket_name_option_pizza
        )

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №6: Увеличение и уменьшение количества товара в корзине")
    def test_case_6(self, selenium, clear_basket, main_page):
        add_pizza_basket(selenium)
        increasing_product(selenium)
        reducing_product(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №7: Удаление пиццы из корзины")
    def test_case_7(self, selenium, clear_basket, main_page):
        add_pizza_basket(selenium)
        delete_all_product(selenium)
        check_empty_basket(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №8: Переход со страницы 'Корзина' на страницу 'Меню'")
    def test_case_8(self, selenium, basket_page):
        button_menu(selenium)
        check_menu_page(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title('Тест-кейс №9: Переход на страницу "Десерты" через рубрикатор "Меню"')
    def test_case_9(self, selenium, main_page):
        select_desserts_rubricator_menu(selenium)
        check_desserts_page(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title(
        'Тест-кейс №10: Изменение фильтра "максимальная цена" на странице "Десерты"'
    )
    def test_case_10(self, selenium, desserts_page):
        filter_max_price(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title('Тест-кейс №11: Добавление товара "Десерт" в корзину ')
    def test_case_11(self, selenium, desserts_page):
        add_dessert_basket(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №12: Оформление заказа не авторизованным пользователем")
    def test_case_12(self, selenium, clear_basket, main_page):
        add_pizza_basket(selenium)
        button_proceed_payment(selenium)
        check_payment_no_authorized(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title(
        'Тест-кейс №13: Переход на страницу "Мой аккаунт" со страницы оформление заказа'
    )
    def test_case_13(self, selenium, payment_page):
        check_payment_no_authorized(selenium)
        button_my_account(selenium)
        check_open_my_account_page_no_authorized(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title(
        'Тест-кейс №14: Переход на страницу формы "Регистрация" со страницы "Мой аккаунт"'
        " не авторизованным пользователем"
    )
    def test_case_14(self, selenium, clear_basket, my_account_page):
        button_registration(selenium)
        check_open_registration_page(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №15: Регистрация аккаунта")
    def test_case_15(self, selenium, registration_page):
        correct_registration_account(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №16: Авторизация пользователя")
    def test_case_16(self, selenium, de_authorized, my_account_page):
        authorized_user(selenium)

    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №17: Оформление заказа")
    def test_case_17(self, selenium):
        button_main(selenium)
        add_pizza_basket(selenium)
        select_desserts_rubricator_menu(selenium)
        add_dessert_basket(selenium)
        summ_products = check_summ_products_basket(selenium)
        button_proceed_payment(selenium)
        clear_payment_form(selenium)
        completion_payment_form(selenium)
        check_summ_after_payment(selenium, summ_products)

    @allure.story("Задание №2. Флоу с промокодом")
    @allure.title("Тест-кейс №1: Проверка ввода валидного промокода 'GIVEMEHALYAVA'")
    def test_case_18(self, selenium):
        button_main(selenium)
        add_pizza_basket(selenium)
        summ_products = check_summ_products_basket(selenium)
        button_proceed_payment(selenium)
        promocode = "GIVEMEHALYAVA"
        activate_promocode(selenium, summ_products, promocode)

    @allure.story("Задание №2. Флоу с промокодом")
    @allure.title("Тест-кейс №2: Проверка ввода не валидного промокода 'DC120'")
    def test_case_19(self, selenium):
        button_basket(selenium)
        delete_promocode(selenium)
        summ_products = check_summ_products_basket(selenium)
        button_proceed_payment(selenium)
        promocode = "DC120"
        activate_promocode(selenium, summ_products, promocode)

    @allure.story("Задание №2. Флоу с промокодом")
    @allure.title(
        "Тест-кейс №3: Проверка при не работающем сервере валидации промокодов"
    )
    def test_case_20(self, playwright: Playwright, page: Page):
        block_server(playwright, page)

    @allure.story("Задание №2. Флоу с промокодом")
    @allure.title(
        "Тест-кейс №4: Повторное применение промокода 'GIVEMEHALYAVA' одним пользователем"
    )
    def test_case_21(self, selenium, de_authorized, registration_page):
        correct_registration_account(selenium)
        button_main(selenium)
        add_pizza_basket(selenium)
        summ_products = check_summ_products_basket(selenium)
        button_proceed_payment(selenium)
        promocode = "GIVEMEHALYAVA"
        summ_products = activate_promocode(selenium, summ_products, promocode)
        clear_payment_form(selenium)
        completion_payment_form(selenium)
        check_summ_after_payment(selenium, summ_products)
        with allure.step(
            f"Повторная активация промокода '{promocode}' при оформлении заказа. "
            f"В случае активации: Баг-репорт"
        ):
            button_main(selenium)
            add_pizza_basket(selenium)
            summ_products = check_summ_products_basket(selenium)
            button_proceed_payment(selenium)
            promocode = "GIVEMEHALYAVA"
            summ_products = activate_promocode(selenium, summ_products, promocode)
            clear_payment_form(selenium)
            completion_payment_form(selenium)
            check_summ_after_payment(selenium, summ_products)

    @allure.story("Задание №3. Флоу с бонусной системой")
    @allure.title("Тест-кейс №1: Регистрация в бонусной программе")
    def test_case_22(self, selenium, de_authorized, registration_page):
        correct_registration_account(selenium)
        button_bonus_programm(selenium)
        apply_bonus_programm(selenium)
