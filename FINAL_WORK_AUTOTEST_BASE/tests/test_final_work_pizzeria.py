import allure
from selenium.webdriver.common.by import By

from src.Final_work.add_product_basket.add_desert_basket import add_dessert_basket
from src.Final_work.add_product_basket.add_pizza_basket import add_pizza_basket
from src.Final_work.asserts.all_asserts import check_name_option_pizza_add_basket, \
    check_go_pizza_page, check_empty_basket, check_menu_page, check_desserts_page, check_name_product_add_basket, \
    check_payment_no_authorized, check_open_my_account_page_no_authorized, check_open_registration_page, \
    check_registration_completed

from src.Final_work.pages.authorization_page.click_buttons.button_registration import button_registration
from src.Final_work.pages.basket_page.check_option_add_pizza import check_option_add_pizza

from src.Final_work.pages.basket_page.click_buttons.delete_all_product import delete_all_product
from src.Final_work.pages.basket_page.click_buttons.increasing_product import increasing_product
from src.Final_work.pages.basket_page.click_buttons.proceed_payment import button_proceed_payment
from src.Final_work.pages.basket_page.click_buttons.reducing_product import reducing_product

from src.Final_work.pages.basket_page.normal_name_product_basket import normal_name_product_basket
from src.Final_work.fixtures.open_pages.clear_basket import ClearBasket

from src.Final_work.fixtures.open_pages.pages import OpenPage
from src.Final_work.pages.main_page.buttons_section_main_page.all_buttons import button_basket, button_menu, \
    button_my_account

from src.Final_work.pages.main_page.main_page_slider_pizza.click_buttons.click_right_slider_pizza import \
    click_right_slider_pizza
from src.Final_work.pages.main_page.main_page_slider_pizza.main_page_slider_pizza import main_page_slider_pizza_names
from src.Final_work.pages.main_page.main_page_slider_pizza.right_slider_pizza import right_slider_pizza
from src.Final_work.pages.menu_page.filtr_price.filter_max_price import filter_max_price
from src.Final_work.pages.menu_page.rubricator.select_desserts import select_desserts_rubricator_menu

from src.Final_work.normal_name_elements.all_normal_name import normal_name_pizza
from src.Final_work.pages.main_page.main_page_slider_pizza.click_buttons.click_left_slider_pizza import \
    click_left_slider_pizza

from src.Final_work.pages.page_pizza.name_pizza import name_pizza_page_pizza
from src.Final_work.pages.page_pizza.select_option_add_basket import select_option_add_basket
from src.Final_work.pages.registration_page.registration_account import correct_registration_account


@allure.feature("Все тесты финальной работы. Автотесты на Python. Базовая часть")
@allure.story("Авто-тесты Pizzeria")
class TestsFullCasePizzeria(OpenPage, ClearBasket):
    @allure.title("Тест-кейс №1: Проверка названий пицц в слайдере при загрузке главной страницы")
    def test_case_1(self, selenium, main_page):
        main_page_slider_pizza_names(selenium)
        pass

    @allure.title("Тест-кейс №2: Добавление пиццы из слайдера в корзину и проверка по названию, "
                  "что добавлена верная пицца")
    def test_case_2(self, selenium, main_page):
        add_pizza_basket(selenium)
        pass

    @allure.title("Тест-кейс №3: Проверка кнопок 'влево' и 'вправо' слайдера пицц на главной странице")
    def test_case_3(self, selenium, clear_basket, main_page):
        click_right_slider_pizza(selenium)
        right_slider_pizza(selenium)
        click_left_slider_pizza(selenium)
        main_page_slider_pizza_names(selenium)
        pass

    @allure.title("Тест-кейс №4: Переход на страницу пиццы с главной страницы")
    def test_case_4(self, selenium, main_page):
        with allure.step('Выбор пиццы'):
            name_pizza = selenium.find_element(By.XPATH, '(//section[@id="product1"]'
                                                         '//li[@aria-hidden="false"]//h3)[1]')

        name_pizza_main_page = normal_name_pizza(name_pizza.text)

        with allure.step(f'Клик на выбранную пиццу: "{name_pizza_main_page}"'):
            name_pizza.click()

        name_page_pizza = name_pizza_page_pizza(selenium)
        check_go_pizza_page(name_pizza_main_page, name_page_pizza)
        pass

    @allure.title("Тест-кейс №5: Добавление пиццы в корзину с дополнительной опцией")
    def test_case_5(self, selenium, pizza_page):
        name_page_pizza = name_pizza_page_pizza(selenium)
        name_select_options = select_option_add_basket(selenium)
        button_basket(selenium)
        name_pizza_basket = normal_name_product_basket(selenium)
        basket_name_option_pizza = check_option_add_pizza(selenium)
        check_name_product_add_basket(name_page_pizza, name_pizza_basket)
        check_name_option_pizza_add_basket(name_select_options, basket_name_option_pizza)
        pass

    @allure.title("Тест-кейс №6: Увеличение и уменьшение количества товара в корзине")
    def test_case_6(self, selenium, clear_basket, main_page):
        add_pizza_basket(selenium)
        increasing_product(selenium)
        reducing_product(selenium)
        pass

    @allure.title("Тест-кейс №7: Удаление пиццы из корзины")
    def test_case_7(self, selenium, clear_basket, main_page):
        add_pizza_basket(selenium)
        delete_all_product(selenium)
        check_empty_basket(selenium)
        pass

    @allure.title("Тест-кейс №8: Переход со страницы 'Корзина' на страницу 'Меню'")
    def test_case_8(self, selenium, basket_page):
        button_menu(selenium)
        check_menu_page(selenium)
        pass

    @allure.title('Тест-кейс №9: Переход на страницу "Десерты" через рубрикатор "Меню"')
    def test_case_9(self, selenium, main_page):
        select_desserts_rubricator_menu(selenium)
        check_desserts_page(selenium)
        pass

    @allure.title('Тест-кейс №10: Изменение фильтра "максимальная цена" на странице "Десерты"')
    def test_case_10(self, selenium, desserts_page):
        filter_max_price(selenium)
        pass

    @allure.title('Тест-кейс №11: Добавление товара "Десерт" в корзину ')
    def test_case_11(self, selenium, desserts_page):
        add_dessert_basket(selenium)
        pass

    @allure.title('Тест-кейс №12: Оформление заказа не авторизованным пользователем')
    def test_case_12(self, selenium, clear_basket, main_page):
        add_pizza_basket(selenium)
        button_proceed_payment(selenium)
        check_payment_no_authorized(selenium)
        pass

    @allure.title('Тест-кейс №13: Переход на страницу "Мой аккаунт" со страницы оформление заказа')
    def test_case_13(self, selenium, payment_page):
        check_payment_no_authorized(selenium)
        button_my_account(selenium)
        check_open_my_account_page_no_authorized(selenium)
        pass

    @allure.title('Тест-кейс №14: Переход на страницу формы "Регистрация" со страницы "Мой аккаунт"'
                  ' не авторизованным пользователем')
    def test_case_14(self, selenium, clear_basket, my_account_page):
        button_registration(selenium)
        check_open_registration_page(selenium)
        pass

    @allure.title('Тест-кейс №15: Регистрация аккаунта')
    def test_case_15(self, selenium, registration_page):
        correct_registration_account(selenium)
        button_registration(selenium)
        check_registration_completed(selenium)
        pass
