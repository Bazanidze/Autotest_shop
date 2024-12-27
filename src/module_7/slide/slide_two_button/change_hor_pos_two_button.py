import allure
from playwright.sync_api import Page


def change_hor_position_two_button(page: Page, left_button, right_button,
                                   left_button_position_x, right_button_position_x):
    with allure.step('Выбор длительности обучения от 6 до 12 месяцев'):
        left_button.hover()
        page.mouse.down()
        page.mouse.move(x=left_button_position_x, y=0)
        page.mouse.up()
        right_button.hover()
        page.mouse.down()
        page.mouse.move(x=right_button_position_x, y=0)
        page.mouse.up()
