from selene import browser, have, be, query
import allure
from pages.main_page import MainPage
from data.user import Customer

@allure.tag("web")
@allure.label("owner", "div50015")
@allure.title("Проверка существования клиента")
def test_add_customer():
    main_page = MainPage()

    # GIVEN
    customer = Customer(
        f_name='Harry',
        l_name='Potter',
        n_id='E725JB'
    )

    with allure.step('Открытие формы'):
        main_page.open()
        # browser.open('/')

    # WHEN
    with allure.step('Переход к списку клиентов'):
        main_page.list_customers()

    # THEN
    with allure.step('Проверка существования клиента'):
        main_page.check_customer_existence(customer)




