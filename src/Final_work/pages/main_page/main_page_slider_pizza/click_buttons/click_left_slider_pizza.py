import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


def click_left_slider_pizza(selenium):
    with allure.step("Нажатие кнопки 'ВЛЕВО' на слайдере пицц"):
        right_button_slider = selenium.find_element(By.CSS_SELECTOR, 'a[class="slick-prev"]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.move_to_element(right_button_slider).click().perform()
        action_chains.release()
        time.sleep(0.5)
