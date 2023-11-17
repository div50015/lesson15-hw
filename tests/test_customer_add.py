import allure
from pages.main_page import MainPage
from data.user import Customer


@allure.tag("web")
@allure.label("owner", "div50015")
@allure.title("Проверка добавления клиента")
def test_add_customer():
    main_page = MainPage()

    # GIVEN
    customer = Customer(
        f_name='Piter',
        l_name='Pen',
        n_id='E12345'
    )

    # WHEN
    with allure.step('Открытие формы'):
        main_page.open()

    with allure.step('Добавление клиента'):
        main_page.add_customer(customer)

    # THEN
    with allure.step('Проверка добавленя клиента'):
        main_page.check_add_customer(customer)





