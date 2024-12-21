class TestExample:
    def test_title(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru/")
        assert 'Skillbox – образовательная платформа с онлайн-курсами.' == driver.title
        pass

