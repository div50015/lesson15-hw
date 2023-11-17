import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach
import os
from dotenv import load_dotenv


DEFAULT_BROWSER_VERSION = "100.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def browser_management(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    print(f' {login} {password} ')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub", options=options)


    # browser.config.driver = driver
    browser.config.base_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
    browser.config.timeout = 2.0
    browser.config.window_width = 1200
    browser.config.window_height = 1080

    # browser.config.type_by_js = True
    # закрытие сообщения о том что браузер запущен в отладочном режиме
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # driver_options.add_argument('--headless=new')
    # browser.config.driver_options = driver_options

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()

