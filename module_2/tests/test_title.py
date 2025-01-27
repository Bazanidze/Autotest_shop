import allure

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.fixtures.action.clear_basket import ClearBasket
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.fixtures.action.de_authorized import DeAuthorized
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.fixtures.open_pages.pages import OpenPage
from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.pages.main_page.main_page_slider_pizza\
    .main_page_slider_pizza import main_page_slider_pizza_names


class TestExample(OpenPage, ClearBasket, DeAuthorized):
    @allure.story("Задание №1. Основной флоу клиента")
    @allure.title("Тест-кейс №1: Проверка названий пицц в слайдере при загрузке главной страницы")
    def test_case_1(self, selenium, main_page):
        main_page_slider_pizza_names(selenium)
