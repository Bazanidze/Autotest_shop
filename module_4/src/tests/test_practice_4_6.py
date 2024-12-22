import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestExample:
    def test_1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        test_in_search = driver.find_element(By.CSS_SELECTOR, '[class="Input-module__Box_4--GVHsf"]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(test_in_search).double_click(test_in_search).send_keys(Keys.BACKSPACE).perform()
        test_in_search.send_keys('in:title bug' + Keys.ENTER)
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
        test_bpasero = driver.find_element(By.XPATH, "//span[contains(text(), 'bpasero')]")
        test_bpasero.click()
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
        test_repositories_options_stars.send_keys('>20000')
        test_code_options_file_name = driver.find_element(By.CSS_SELECTOR, '[placeholder="app.rb, footer.erb"]')
        test_code_options_file_name.click()
        test_code_options_file_name.send_keys('environment.yml')
        test_button_search = driver.find_element(By.XPATH, "(//button[contains(text(), 'Search')])[1]")
        test_button_search.click()
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
        pass

    def test_5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.maximize_window()
        time.sleep(1)
        action_chains = webdriver.ActionChains(driver)
        test_chart = driver.find_element(By.CSS_SELECTOR, 'section[class="commit-activity-master mb-6"]')
        action_chains.move_to_element_with_offset(test_chart, xoffset=100, yoffset=0).perform()
        pass

