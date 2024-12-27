import time
import logging

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.module_6.module_6_test_4.slide_two_button import duration_training


@allure.feature('Все тесты практических работ')
class TestsPracticeWork:
    logging.info('Начало первого теста')
    @allure.title('Проверка правильности выдачи результатов поиска на github.com')
    def test_1(self, selenium):
        with allure.step('Создание переменной с текстом для ввода "in:title bug'):
            word_search = 'bug'
            word_search_2 = 'Bug'
            text_search = 'in:title ' + word_search

        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            selenium.get("https://github.com/microsoft/vscode/issues")

        with allure.step('Удаление старого текста и ввод нового текста в поле поиска'):
            test_in_search = selenium.find_element(By.CSS_SELECTOR, 'input[class="Input-module__Box_4--GVHsf"]')
            action_chains = webdriver.ActionChains(selenium)
            action_chains.double_click(test_in_search).double_click(test_in_search).send_keys(Keys.BACKSPACE).perform()
            test_in_search.send_keys(text_search + Keys.ENTER)

        with allure.step('Ожидание загрузки результата поиска'):
            time.sleep(3)

        with allure.step('Подсчёт количества репозиториев после поиска'):
            search_field = selenium.find_elements(By.XPATH, "//h3//span")
            length = len(search_field)

        with allure.step('Проверка наличия "bug" или "Bug" в результатах поиска'):
            for num in range(length):
                element_text = search_field[num].text
                assert (word_search in element_text or word_search_2 in element_text) is True
        pass
    logging.info('Конец первого теста')

    @allure.title('Проверка поиска задач от определенного автора на github.com')
    def test_2(self, selenium):
        with allure.step('Создание переменной с названием автора задач'):
            text = 'bpasero'

        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            selenium.get("https://github.com/microsoft/vscode/issues")

        with allure.step('Клик на селект Авторы, ввод в поле поиска автора, выбор автора'):
            selenium.find_element(By.CSS_SELECTOR, '[data-testid="authors-anchor-button"]').click()
            selenium.find_element(By.CSS_SELECTOR, 'input[placeholder="Filter authors"]').send_keys(text)
            selenium.find_element(By.XPATH, "//span[contains(text(), '" + text + "')]").click()

        with allure.step('Ожидание загрузки результата выбора автора'):
            time.sleep(3)

        with allure.step('Подсчёт количества задач от автора'):
            search_field = selenium.find_element("xpath", "//input[@id='repository-input']")
            list_tasks = selenium.find_elements(By.XPATH, "//div/a[contains(@aria-label, 'author')]")
            length = len(list_tasks)

        with allure.step('Проверка наличия выбранного автора как создателя задач'):
            for position in range(length):
                assert (text in (list_tasks[position].get_attribute("aria-label")
                                 and search_field.get_attribute("value"))) is True
        pass

    @allure.title('Проверка работоспособности фильтров на github.com')
    def test_3(self, selenium):
        with allure.step('Создание переменной для поиска по рейтингу звёзд'):
            input_text_stars = 20000

        with allure.step('Открытие страницы https://github.com/search/advanced'):
            selenium.get("https://github.com/search/advanced")

        with allure.step('Заполнение фильтров:'):

            with allure.step('Выбор в селекте значения "Python"'):
                selenium.find_element(By.XPATH, '(//select[@class="form-select js-advanced-search-prefix"])[1]').click()
                selenium.find_element(By.XPATH, "//option[contains(text(), 'Python')]").click()

            with allure.step('Ввод значения поиска по рейтингу звёзд'):
                selenium.find_element(By.ID, 'search_stars').send_keys('>' + str(input_text_stars))

            with allure.step('Указание поиска файлов с именем "environment.yml"'):
                selenium.find_element(By.ID, 'search_filename').send_keys('environment.yml')

            with allure.step('Нажатие кнопки поиск'):
                selenium.find_element(By.XPATH, "(//button[contains(text(), 'Search')])[2]").click()

        with allure.step('Ожидание загрузки страницы с результатами поиска'):
            time.sleep(2)

        with allure.step('Подсчёт количества результатов поиска'):
            list_repositories = selenium.find_elements(By.XPATH, "//a[contains(@aria-label, 'stars')]")
            elements_number = len(list_repositories)

        with allure.step('Проверка, что все результаты содержат рейтинг звёзд, больше введенного значения в фильтр'):
            for position in range(elements_number):
                value = list_repositories[position].get_attribute('aria-label')
                checked_value = ''
                for character in value:
                    if '0' <= character <= '9':
                        checked_value += character
                assert (int(checked_value)) > input_text_stars
        pass

    @allure.title('Проверка выдачи результатов по фильтрам на сайте https://skillbox.ru/code/')
    def test_4(self, selenium):
        with allure.step('Открытие страницы https://skillbox.ru/code/'):
            selenium.get("https://skillbox.ru/code/")

        with allure.step('Выбор радиобаттон "Профессия" в "Тип обучения на платформе"'):
            selenium.find_element(By.CSS_SELECTOR, 'label[value="profession"]').click()

        with allure.step('Выбор длительности обучения от 6 до 12 месяцев'):
            test_range_left_button = selenium.find_element(By.XPATH, '(//button[@class="ui-range__dot"])[1]')
            test_range_right_button = selenium.find_element(By.XPATH, '(//button[@class="ui-range__dot"])[2]')
            duration_training(selenium, test_range_left_button, test_range_right_button)

        with allure.step('Выбор "Python" в фильтре "Тематика"'):
            selenium.find_element(By.XPATH, "//h4[contains(text(), 'Тематика')]/following-sibling::button").click()
            time.sleep(1)
            selenium.find_element(By.XPATH, "(//span[contains(text(), 'Python')])[2]").click()

        with allure.step('Ожидание обновления страницы по выбранным фильтрам'):
            time.sleep(2)

        with allure.step('Проверка правильности выдачи результатов по фильтрам'):
            with allure.step('Проверка фильтра "Профессия"'):
                radio_status = selenium.find_element(By.XPATH, "//label[@value='profession']/input")
                radio_text = selenium.find_element(By.XPATH, "//label[@value='profession']//span")
                list_labels = selenium.find_elements(By.XPATH, "//article//span[contains(@class, "
                                                               "'ui-product-card-main__label')]")
                number_labels = len(list_labels)
                for position in range(number_labels):
                    label = list_labels[position].text
                    if radio_status.is_selected():
                        radio_text.get_attribute("text") == label

            with allure.step('Проверка фильтра длительности обучения'):
                list_duration = selenium.find_elements(By.XPATH, "//span/ancestor::article[@class='ui-product-card']"
                                                                 "//span[contains(@class, 'card__duration')]")
                number_duration = len(list_duration)
                for i in range(number_duration):
                    duration = list_duration[i].text
                    cipher = ''
                    for symbol in duration:
                        if '0' <= symbol <= '9':
                            cipher += symbol
                    assert 6 <= (int(cipher)) <= 12

            with allure.step('Проверка названий профессий по введённым фильтрам'):
                blocks_name_proffesions = selenium.find_elements(By.CSS_SELECTOR, ".courses-block__list h3")
                lenght = len(blocks_name_proffesions)
                prof_1 = 'Python-разработчик'
                prof_2 = 'Data scientist'
                prof_3 = 'Data Scientist с нуля до Junior'
                prof_4 = 'Разработчик'
                prof_5 = 'Data-аналитик'
                prof_6 = 'Machine Learning Engineer'
                prof_7 = 'Инженер по автоматизации тестирования'
                for position in range(lenght):
                    text_name_block = blocks_name_proffesions[position].text
                    assert (prof_1 in text_name_block or prof_2 in text_name_block or prof_3 in text_name_block
                            or prof_4 in text_name_block or prof_5 in text_name_block
                            or prof_6 in text_name_block or prof_7 in text_name_block) is True

        pass

    @allure.title('Проверка правильности наведения курсора на график на '
                  'сайте https://github.com/microsoft/vscode/graphs/commit-activity')
    def test_5(self, selenium):
        with allure.step('Открытие страницы https://github.com/microsoft/vscode/graphs/commit-activity'):
            selenium.get("https://github.com/microsoft/vscode/graphs/commit-activity")

        with allure.step('Ожидание загрузки страницы'):
            time.sleep(2)

        with allure.step('Наведение курсора на график'):
            action_chains = webdriver.ActionChains(selenium)
            test_chart = selenium.find_element(By.CSS_SELECTOR, 'section[class="commit-activity-master mb-6"]')
            action_chains.move_to_element_with_offset(test_chart, xoffset=95, yoffset=0).perform()

        with allure.step('Проверка значения графика в место наведения курсора'):
            text_pie = selenium.find_element(By.XPATH, '//div[@class="svg-tip n"]/strong').text
            assert text_pie == '223'
        pass
