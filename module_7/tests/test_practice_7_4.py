import time

from playwright.sync_api import Page
import allure

from src.module_7.input_text.input_text_enter import input_text_enter
from src.module_7.slide.slide_two_button.change_hor_pos_two_button import change_hor_position_two_button


@allure.feature('Все тесты практических работ')
@allure.title('Проверка правильности выдачи результатов поиска на github.com')
def test_1(page: Page):
    with allure.step('Создание переменной с текстом для ввода "in:title bug"'):
        word_search = 'bug'
        word_search_2 = 'Bug'
        text_search = 'in:title ' + word_search

    with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
        page.goto("https://github.com/microsoft/vscode/issues", wait_until="domcontentloaded")

    test_in_search = page.query_selector('input[class="Input-module__Box_4--GVHsf"]')
    input_text_enter(page, test_in_search, text_search)

    with allure.step('Ожидание загрузки результата поиска'):
        time.sleep(2)

    with allure.step('Подсчёт количества репозиториев после поиска'):
        search_field = page.query_selector_all("//h3//span")
        length = len(search_field)

    with allure.step('Проверка наличия "bug" или "Bug" в результатах поиска'):
        for num in range(length):
            element_text = search_field[num].inner_text()
            assert (word_search in element_text or word_search_2 in element_text) is True
    pass


@allure.title('Проверка поиска задач от определенного автора на github.com')
def test_2(page: Page):
    with allure.step('Создание переменной с названием автора задач'):
        text = 'bpasero'

    with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
        page.goto("https://github.com/microsoft/vscode/issues", wait_until="domcontentloaded")

    with allure.step('Клик на селект Авторы, ввод в поле поиска автора, выбор автора'):
        page.query_selector('[data-testid="authors-anchor-button"]').click()
        time.sleep(0.5)
        page.query_selector('input[placeholder="Filter authors"]').fill(text)
        page.query_selector("//span[contains(text(), '" + text + "')]").click()

    with allure.step('Ожидание загрузки результата выбора автора'):
        time.sleep(2)

    with allure.step('Подсчёт количества задач от автора'):
        search_field = page.query_selector("//input[@id='repository-input']")
        list_tasks = page.query_selector_all("//div/a[contains(@aria-label, 'author')]")
        length = len(list_tasks)

    with allure.step('Проверка наличия выбранного автора как создателя задач'):
        for position in range(length):
            assert (text in (list_tasks[position].get_attribute("aria-label")
                             and search_field.get_attribute("value"))) is True
    pass


@allure.title('Проверка работоспособности фильтров на github.com')
def test_3(page: Page):
    with allure.step('Создание переменной для поиска по рейтингу звёзд'):
        input_text_stars = 20000

    with allure.step('Открытие страницы https://github.com/search/advanced'):
        page.goto("https://github.com/search/advanced", wait_until="domcontentloaded")

    with allure.step('Заполнение фильтров:'):

        with allure.step('Выбор в селекте значения "Python"'):
            page.query_selector('//select[@class="form-select js-advanced-search-prefix"][1]').click()
            count_python = 19
            for i in range(count_python):
                page.keyboard.press('ArrowDown')
            page.keyboard.press('Enter')

        with allure.step('Ввод значения поиска по рейтингу звёзд'):
            page.query_selector("//input[@id='search_stars']").fill('>' + str(input_text_stars))

        with allure.step('Указание поиска файлов с именем "environment.yml"'):
            page.query_selector("//input[@id='search_filename']").fill('environment.yml')

        with allure.step('Нажатие кнопки поиск'):
            page.query_selector("(//button[contains(text(), 'Search')])[2]").click()

    with allure.step('Ожидание загрузки страницы с результатами поиска'):
        time.sleep(2)

    with allure.step('Подсчёт количества результатов поиска'):
        list_repositories = page.query_selector_all("//a[contains(@aria-label, 'stars')]")
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
def test_4(page: Page):
    with allure.step('Открытие страницы https://skillbox.ru/code/'):
        page.goto("https://skillbox.ru/code/", wait_until='domcontentloaded')

    with allure.step('Выбор радиобаттон "Профессия" в "Тип обучения на платформе"'):
        page.query_selector('label[value="profession"]').click()

    test_range_left_button = page.locator('(//button[@class="ui-range__dot"])[1]')
    test_range_right_button = page.locator('(//button[@class="ui-range__dot"])[2]')
    change_hor_position_two_button(page, test_range_left_button, test_range_right_button, 100, 230)

    with allure.step('Выбор "Python" в фильтре "Тематика"'):
        page.query_selector("//h4[contains(text(), 'Тематика')]/following-sibling::button").click()
        time.sleep(1)
        page.query_selector("(//span[contains(text(), 'Python')])[2]").click()

    with allure.step('Проверка правильности выдачи результатов по фильтрам'):
        with allure.step('Проверка фильтра "Профессия"'):
            radio_status = page.query_selector("//label[@value='profession']/input")
            radio_text = page.query_selector("//label[@value='profession']//span")
            list_labels = page.query_selector_all("//article//span[contains(@class, 'ui-product-card-main__label')]")
            number_labels = len(list_labels)
            for position in range(number_labels):
                label = list_labels[position].inner_text()
                if radio_status.is_enabled():
                    radio_text.inner_text() == label

        with allure.step('Проверка фильтра длительности обучения'):
            list_duration = page.query_selector_all("//span/ancestor::article[@class='ui-product-card']"
                                                    "//span[contains(@class, 'card__duration')]")
            number_duration = len(list_duration)
            for i in range(number_duration):
                duration = list_duration[i].inner_text()
                cipher = ''
                for symbol in duration:
                    if '0' <= symbol <= '9':
                        cipher += symbol
                assert 6 <= (int(cipher)) <= 12

        with allure.step('Проверка названий профессий по введённым фильтрам'):
            blocks_name_proffesions = page.query_selector_all(".courses-block__list h3")
            lenght = len(blocks_name_proffesions)
            prof_1 = 'Python-разработчик'
            prof_2 = 'Data scientist'
            prof_3 = 'Data Scientist с нуля до Junior'
            prof_4 = 'Разработчик'
            prof_5 = 'Data-аналитик'
            prof_6 = 'Machine Learning Engineer'
            prof_7 = 'Инженер по автоматизации тестирования'
            for position in range(lenght):
                text_name_block = blocks_name_proffesions[position].inner_text()
                assert (prof_1 in text_name_block or prof_2 in text_name_block or prof_3 in text_name_block
                        or prof_4 in text_name_block or prof_5 in text_name_block
                        or prof_6 in text_name_block or prof_7 in text_name_block) is True
    pass


@allure.title('Проверка правильности наведения курсора на график на '
              'сайте https://github.com/microsoft/vscode/graphs/commit-activity')
def test_5(page: Page):
    with allure.step('Открытие страницы https://github.com/microsoft/vscode/graphs/commit-activity'):
        page.goto("https://github.com/microsoft/vscode/graphs/commit-activity")

    with allure.step('Ожидание загрузки страницы'):
        time.sleep(2)

    with allure.step('Наведение курсора на график'):

        test_chart = page.query_selector('section[class="commit-activity-master mb-6"]')
        test_chart.hover()

    with allure.step('Проверка значения графика в место наведения курсора'):
        text_pie = page.query_selector('//div[@class="svg-tip n"]/strong').inner_text()
        assert text_pie == '179'
    pass
