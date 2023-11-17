from selene import browser, have, be, query
import allure


@allure.title("Проверка существования клиента")
def test_add_customer():
    with allure.step('Открытие формы'):
        browser.open('/')

    with allure.step('Переход к списку клиентов'):
        browser.element('[ng-click="manager()"]').click()
        browser.element('[ng-class="btnClass3"]').click()

    # with allure.step('Проверка существования клиента'):
        browser.all('tr').element_by(have.text('Potter')).should(have.text('Harry Potter E725JB'))
