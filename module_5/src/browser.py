import pytest

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

path_to_driver = 'D:/Chrome driver/chromedriver-win64.131.0.6778.108/chromedriver.exe'


@pytest.fixture()
def set_up_browser():
    options = ChromeOptions()

    # Создание объекта Service с указанием пути к Chromedriver
    service = Service(executable_path=path_to_driver)

    # Запуск Chrome с указанным сервисом и опциями
    driver = Chrome(service=service, options=options)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
