import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.utils.check_results_search import check_results_search
from src.utils.quantity_answer_search import quantity_answer_search

@allure.feature('Full tests practice work')
# @allure.story('Waiting page load')

class TestsPracticeWork:
    @allure.title('Проверка правильности выдачи результатов поиска на github.com')
    def test_1(self, selenium):
        driver = selenium
        driver.get("https://github.com/microsoft/vscode/issues")
        word_search = 'bug'
        word_search_2 = 'Bug'
        text_search = 'in:title ' + word_search

        test_in_search = driver.find_element(By.CSS_SELECTOR, 'input[class="Input-module__Box_4--GVHsf"]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(test_in_search).double_click(test_in_search).send_keys(Keys.BACKSPACE).perform()
        test_in_search.send_keys(text_search + Keys.ENTER)
        time.sleep(3)

        search_field = driver.find_elements(By.XPATH, "//h3//span")
        length = len(search_field)

        for num in range(length):
            assert (word_search in (search_field[num].text) or word_search_2 in (search_field[num].text)) is True
        pass

    def test_2(self, selenium):
        driver = selenium
        driver.get("https://github.com/microsoft/vscode/issues")
        text = 'bpasero'
        driver.find_element(By.CSS_SELECTOR, '[data-testid="authors-anchor-button"]').click()

        driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Filter authors"]').send_keys(text)

        driver.find_element(By.XPATH, "//span[contains(text(), '" + text + "')]").click()
        time.sleep(3)

        search_field = driver.find_element("xpath", "//input[@id='repository-input']")

        list_tasks = driver.find_elements(By.XPATH, "//div/a[contains(@aria-label, 'author')]")
        length = len(list_tasks)

        for position in range(length):
            assert (text in (list_tasks[position].get_attribute("aria-label") and search_field.get_attribute(
                "value"))) is True
        pass

    def test_3(self, selenium):
        driver = selenium
        input_text_stars = 20000
        driver.get("https://github.com/search/advanced")
        driver.find_element(By.XPATH, '(//select[@class="form-select js-advanced-search-prefix"])[1]').click()
        driver.find_element(By.XPATH, "//option[contains(text(), 'Python')]").click()
        driver.find_element(By.ID, 'search_stars').send_keys('>' + str(input_text_stars))
        driver.find_element(By.ID, 'search_filename').send_keys('environment.yml')
        driver.find_element(By.XPATH, "(//button[contains(text(), 'Search')])[2]").click()
        time.sleep(2)

        list_repositories = driver.find_elements(By.XPATH, "//a[contains(@aria-label, 'stars')]")
        elements_number = len(list_repositories)

        for position in range(elements_number):
            value = list_repositories[position].get_attribute('aria-label')
            checked_value = ''
            for character in value:
                if '0' <= character <= '9':
                    checked_value += character
            assert (int(checked_value)) > input_text_stars
        pass

    def test_4(self, selenium):
        driver = selenium
        text_type_training = 'Профессия'
        driver.get("https://skillbox.ru/code/")
        driver.maximize_window()
        action_chains = webdriver.ActionChains(driver)
        driver.find_element(By.CSS_SELECTOR, 'label[value="profession"]').click()
        test_range_left_button = driver.find_element(By.XPATH, '(//button[@class="ui-range__dot"])[1]')
        test_range_right_button = driver.find_element(By.XPATH, '(//button[@class="ui-range__dot"])[2]')

        action_chains.click_and_hold(test_range_left_button).move_by_offset(xoffset=40, yoffset=10).perform()
        action_chains.release().perform()
        action_chains.click_and_hold(test_range_right_button).move_by_offset(xoffset=-40, yoffset=10).perform()
        action_chains.release().perform()

        driver.find_element(By.XPATH, '(//button[@class="ui-expand-button filter-checkboxes__button ui-expand-button--small"])').click()
        time.sleep(1)

        driver.find_element(By.XPATH, "(//span[contains(text(), 'Python')])[2]").click()
        time.sleep(2)

        radio_status = driver.find_element(By.XPATH, "//label[@value='profession']/input")
        radio_text = driver.find_element(By.XPATH, "//label[@value='profession']//span")
        list_labels = driver.find_elements(By.XPATH, "//article//span[contains(@class, 'ui-product-card-main__label')]")

        number_labels = len(list_labels)
        for position in range(number_labels):
            label = list_labels[position].text
            if radio_status.is_selected():
                radio_text.get_attribute("text") == label

        list_duration = driver.find_elements(By.XPATH, "//span/ancestor::article[@class='ui-product-card']//span[contains(@class, 'card__duration')]")
        number_duration = len(list_duration)
        for i in range(number_duration):
            duration = list_duration[i].text
            cipher = ''
            for symbol in duration:
                if '0' <= symbol <= '9':
                    cipher += symbol
            assert 6 <= (int(cipher)) <= 12
        pass

    def test_5(self, selenium):
        driver = selenium
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.maximize_window()
        action_chains = webdriver.ActionChains(driver)
        test_chart = driver.find_element(By.CSS_SELECTOR, 'section[class="commit-activity-master mb-6"]')
        time.sleep(2)
        action_chains.move_to_element_with_offset(test_chart, xoffset=95, yoffset=0).perform()

        text_pie = driver.find_element(By.XPATH, '//div[@class="svg-tip n"]/strong').text
        assert text_pie == '223'
        pass



