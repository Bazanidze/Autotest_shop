import pytest


from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope='class')
def selenium(pytestconfig):

    options = ChromeOptions()
    options.add_argument("--window-size=1920,1080")


    # Создание объекта Service с указанием пути к Chromedriver
    service = Service(executable_path=pytestconfig.getini("path_to_driver_chrome"))


    # Запуск Chrome с указанным сервисом и опциями
    driver = Chrome(service=service, options=options)

    # Можно еще так на весь экран раскрывать браузер
    # driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver

    driver.quit()


@pytest.fixture()
def selenium_local():
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
