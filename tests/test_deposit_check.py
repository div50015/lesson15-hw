import allure
from pages.main_page import MainPage
from data.user import Customer


@allure.tag("web")
@allure.label("owner", "div50015")
@allure.title("Проверка состояния счета")
def test_check_deposite():
    main_page = MainPage()

    # GIVEN
    customer = Customer(
        f_name='Harry',
        l_name='Potter',
        n_id='E725JB'
    )

    with allure.step('Открытие формы'):
        main_page.open()

    # WHEN
    with allure.step('Выбор клиента'):
        main_page.select_customer(customer)

    # THEN
    with allure.step('Проверка состояния счета'):
        main_page.check_deposit(0)


