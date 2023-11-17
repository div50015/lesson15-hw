from selene import browser, have, be, query
import allure
from pages.main_page import MainPage
from data.user import Customer


@allure.title("Проверка удаления клиента")
def test_del_customer():
    main_page = MainPage()

    customer = Customer(
        f_name='Piter',
        l_name='Pen',
        n_id='E12345'
    )

    with allure.step('Открытие формы'):
        main_page.open()

    with allure.step('Добавление клиента'):
        main_page.add_customer(customer)

    with allure.step('Удаление клиента'):
        main_page.del_customer(customer)

    with (allure.step('Проверка удаления клиента')):
        main_page.check_del_customer(customer)
