import allure
from playwright.sync_api import Page


def input_text_enter(page: Page, element, text):
    with allure.step('Удаление старого текста и ввод нового текста в поле поиска с нажатием "Enter"'):
        element.click()
        element.press("Control+A")
        element.press("Backspace")
        element.fill(text)
        element.press("Enter")
