class TestExample:
    def test_title(self, selenium_browser_driver):
        driver = selenium_browser_driver
        driver.get("https://skillbox.ru/")
        assert 'Skillbox' == driver.title
        pass

