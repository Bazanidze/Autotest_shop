from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest

@pytest.fixture()
def set_up_browser():
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()