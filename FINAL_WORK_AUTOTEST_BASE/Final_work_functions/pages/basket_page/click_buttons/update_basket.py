from selenium.webdriver.common.by import By


def update_basket(selenium):
    selenium.find_element(By.CSS_SELECTOR, 'button[value="Обновить корзину"]').click()
