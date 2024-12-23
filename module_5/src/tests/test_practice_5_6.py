import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element, \
    text_to_be_present_in_element_attribute, text_to_be_present_in_element_value
from selenium.webdriver.support.wait import WebDriverWait


class TestExample:
    def test_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        word_search = 'bug'
        word_search_2 = 'Bug'
        text_search = 'in:title ' + word_search

        # Ниже ищу поле поиска, ввожу символы, нажимаю ввод и проверяю валидацию введенного текста

        test_in_search = driver.find_element(By.CSS_SELECTOR, 'input[class="Input-module__Box_4--GVHsf"]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(test_in_search).double_click(test_in_search).send_keys(Keys.BACKSPACE).perform()
        test_in_search.send_keys(text_search + Keys.ENTER)
        assert test_in_search.get_attribute('value') == text_search

        # Ниже жду когда загрузится страница после нажатия ввода (после прогрузки страницы к тексту поиска прибавляется пробел)

        driver.find_element(By.CSS_SELECTOR, 'input[value="' + text_search + ' ' + '"]')

        # Ниже дождались пока загрузилась страница и считаю количество элементов, необходимых проверить

        quantity_text = driver.find_elements(By.XPATH, "(//h3//span)")
        quantity = 0
        for qua in quantity_text:
            quantity += 1

        # Ниже проверяю каждый элемент на странице (я пробовал использовать text_to_be_present_in_element (закоментировано ) можно было с ним как то сделать ? и вообще правильно его использовал??? И для чего он? Я как понял он должен был брать текст из элемента)

        for num in range(1, quantity + 1):
            text_value_1 = driver.find_element(By.XPATH, "(//h3//span)" + "[" + str(num) + "]").text
            if word_search in text_value_1:
                word_search = text_value_1
                assert word_search == text_value_1
                word_search = 'bug'
                # assert text_to_be_present_in_element(locator=(By.XPATH, "(//h3//span)" + "[" + str(num) + "]"), text_=word_search)
            elif word_search_2 in text_value_1:
                word_search_2 = text_value_1
                assert word_search_2 == text_value_1
                word_search_2 = 'Bug'
                # assert text_to_be_present_in_element(locator=(By.XPATH, "(//h3//span)" + "[" + str(num) + "]"), text_=word_search_2)
            else:
                print(num, ':Не верно')
        pass

    def test_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        text = 'bpasero'
        test_in_author = driver.find_element(By.CSS_SELECTOR, '[data-testid="authors-anchor-button"]')
        test_in_author.click()
        test_bpasero = driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Filter authors"]')
        test_bpasero.click()
        test_bpasero.send_keys(text)
        test_bpasero = driver.find_element(By.XPATH, "//span[contains(text(), '" + text + "')]")
        test_bpasero.click()
        search_input = driver.find_element(By.CSS_SELECTOR, "input[value='is:issue state:open author:bpasero ']")
        assert search_input.get_attribute('value') == 'is:issue state:open author:bpasero '

        # Можете объяснить, как работает то что я пытался сделать НИЖЕ, что это, для чего это, и как оно должно работать? (оно же по идеи должно брать текст из атрибута? нет?)

        # assert text_to_be_present_in_element_attribute(locator=(By.CSS_SELECTOR, 'input[placeholder="Search Issues"]'), attribute_= 'value=', text_= text)
        # assert text_to_be_present_in_element_attribute(locator=(By.CSS_SELECTOR, 'input[placeholder="Search Issues"]'), attribute_= 'value=', text_='is:issue state:open author:bpasero ') is True

        pass

    def test_3(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/search/advanced")
        test_in_select = driver.find_element(By.XPATH, '(//select[@class="form-select js-advanced-search-prefix"])[1]')
        test_in_select.click()
        test_python = driver.find_element(By.XPATH, "//option[contains(text(), 'Python')]")
        test_python.click()
        test_repositories_options_stars = driver.find_element(By.CSS_SELECTOR, '[placeholder="0..100, 200, >1000"]')
        test_repositories_options_stars.click()
        input_text_stars = 20000
        test_repositories_options_stars.send_keys('>' + str(input_text_stars))
        test_code_options_file_name = driver.find_element(By.CSS_SELECTOR, '[placeholder="app.rb, footer.erb"]')
        test_code_options_file_name.click()
        test_code_options_file_name.send_keys('environment.yml')
        test_button_search = driver.find_element(By.XPATH, "(//button[contains(text(), 'Search')])[1]")
        test_button_search.click()

        quantity_repositories = driver.find_elements(By.XPATH, '(//span[@class="Text__StyledText-sc-17v1xeu-0 fsOMbO search-match"])')
        quantity = 0
        for qua in quantity_repositories:
            quantity += 1

        for num in range(1, quantity + 1):
            quantity_stars_text = ''
            text_stars = driver.find_element(By.XPATH, '(//a[@class="Box-sc-g0xbh4-0 jJYFGF prc-Link-Link-85e08"]/span)[' + str(num) + ']').text
            for delete_k in text_stars:
                if delete_k == 'k':
                    break
                else:
                    quantity_stars_text += delete_k
            quantity_stars_text = float(quantity_stars_text) * 1000
            assert quantity_stars_text > input_text_stars
        pass

    def test_4(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru/code/")
        driver.maximize_window()
        action_chains = webdriver.ActionChains(driver)
        test_radio_profession = driver.find_element(By.CSS_SELECTOR, 'label[value="profession"]')
        test_range_left_button = driver.find_element(By.XPATH, '(//button[@class="ui-range__dot"])[1]')
        test_range_right_button = driver.find_element(By.XPATH, '(//button[@class="ui-range__dot"])[2]')
        test_open_tematic = driver.find_element(By.XPATH, '(//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"])')
        test_radio_profession.click()
        action_chains.click_and_hold(test_range_left_button).move_by_offset(xoffset=40, yoffset=10).perform()
        action_chains.release().perform()
        action_chains.click_and_hold(test_range_right_button).move_by_offset(xoffset=-40, yoffset=10).perform()
        action_chains.release().perform()
        test_open_tematic.click()
        test_open_tematic_checkbox_python = driver.find_element(By.XPATH, "(//span[contains(text(), 'Python')])[2]")
        test_open_tematic_checkbox_python.click()

        driver.find_element(By.XPATH, '//div[@class="ui-choice-chip ui-choice-chip--big ui-choice-chip--stroke"]/span[contains(text(), "Python")]')

        quantity_type_profession = driver.find_elements(By.XPATH, '(//span[@class ="ui-product-card-main__label f f--12"])')
        quantity = 0
        text_type_training = 'Профессия'
        for qua in quantity_type_profession:
            quantity += 1
        for num in range(1, quantity + 1):
            text_profession = driver.find_element(By.XPATH, '(//span[@class ="ui-product-card-main__label f f--12"])[' + str(num) + ']').text
            text_mount = driver.find_element(By.XPATH, '(//b[@class="card__count f f--12 f--m"])[' + str(num) + ']').text
            assert text_profession == text_type_training and 6 <= int(text_mount) <= 12                                                         # Не нашел как проверить фильтр Python
        pass

    def test_5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.maximize_window()
        action_chains = webdriver.ActionChains(driver)
        test_chart = driver.find_element(By.CSS_SELECTOR, 'section[class="commit-activity-master mb-6"]')
        time.sleep(2)
        action_chains.move_to_element_with_offset(test_chart, xoffset=95, yoffset=0).perform()

        text_pie = driver.find_element(By.XPATH, '//div[@class="svg-tip n"]/strong').text
        assert text_pie == '223'
        pass



