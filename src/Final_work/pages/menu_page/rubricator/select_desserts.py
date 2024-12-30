import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


def select_desserts_rubricator_menu(selenium):
    with allure.step('Выбор "Десерты" в рубрикаторе "Меню"'):
        menu_page = selenium.find_element(By.XPATH, '//a[contains(text(), "Меню")]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.move_to_element(menu_page).move_by_offset(xoffset=0, yoffset=90).click().perform()
        action_chains.release()
