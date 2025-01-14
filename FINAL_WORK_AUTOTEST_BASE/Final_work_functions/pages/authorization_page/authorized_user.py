import allure
from selenium.webdriver.common.by import By

from FINAL_WORK_AUTOTEST_BASE.Final_work_functions.asserts.all_asserts import check_authorized


def authorized_user(selenium):
    name_user = 'Nikifor'
    password_user = 'VabloPablo123'
    with allure.step('Вход в аккаунт'):
        with allure.step('Заполнение полей ввода на странице "Авторизация":'):
            with allure.step('Заполнение поля ввода "Имя пользователя": ' + name_user):
                selenium.find_element(By.ID, 'username').send_keys(name_user)
            with allure.step('Заполнение поля ввода "Пароль": ' + password_user):
                selenium.find_element(By.ID, 'password').send_keys(password_user)
        with allure.step('Клик на кнопку "ВОЙТИ"'):
            selenium.find_element(By.CSS_SELECTOR, 'button[value="Войти"]').click()
        authorized_name_user = selenium.find_element(By.CSS_SELECTOR, 'div[class="woocommerce-MyAccount-content"] '
                                                                      'strong').text
        check_authorized(name_user, authorized_name_user)
