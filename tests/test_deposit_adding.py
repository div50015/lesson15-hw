import allure
from pages.main_page import MainPage
from data.user import Customer


@allure.title("Проверка пополнения счета")
def test_check_deposite():
    main_page = MainPage()

    customer = Customer(
        f_name='Harry',
        l_name='Potter',
        n_id='E725JB'
    )

    with allure.step('Открытие формы'):
        main_page.open()

    with allure.step('Выбор клиента'):
        main_page.select_customer(customer)

    with allure.step('Проверка состояния счета до пополнения'):
        main_page.check_deposit(0)

    with allure.step('Пополнение счета'):
        main_page.add_deposit(100)

    with allure.step('Проверка состояния счета после пополнения'):
        main_page.chech_deposit_after_add(100, customer)
