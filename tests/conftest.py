import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser
from utils import attach

@pytest.fixture(scope='function', autouse=True)
def browser_management():
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
    driver = webdriver.Remote(command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",options=options)

    browser.config.driver = driver
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