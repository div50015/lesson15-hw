from selene import browser, be, have, query
from data.user import Customer


class MainPage:

    def open(self):
        browser.open('/')
        return self

    def select_customer(self, user:Customer):
        browser.element('[ng-click="customer()"]').click()
        browser.element('#userSelect').type(f'{user.f_name} {user.l_name}')
        browser.element('[ng-show="custId != \'\'"]').click()
        return self

    def check_deposit(self, n: int):
        browser.all('strong:nth-child(2)').second.should(have.text(str(n)))
        return self

    def add_deposit(self, n:int):
        browser.element('[ng-click="deposit()"]').click()
        browser.element('input[ng-model=amount]').type(str(n))
        browser.element('button[type=submit]').click()
        browser.element('span[ng-show=message]').should(have.exact_text('Deposit Successful'))
        return self

    def chech_deposit_after_add(self, n: int, user: Customer):
        browser.element('[ng-click="home()"]').click()
        browser.element('[ng-click="customer()"]').click()
        browser.element('#userSelect').type(f'{user.f_name} {user.l_name}')
        browser.element('[ng-show="custId != \'\'"]').click()
        browser.all('strong:nth-child(2)').second.should(have.text(str(n)))
        return self

    def withdrawl_deposit(self, n: int):
        browser.element('[ng-click="withdrawl()"]').click()
        browser.element('input[ng-model=amount]').type(str(n))
        browser.element('button[type=submit]').click()
        browser.element('span[ng-show=message]').should(have.exact_text('Transaction successful'))
        browser.element('[ng-click="home()"]').click()

    def check_deposit_after_withdrawl(self, n :int, user: Customer):
        browser.element('[ng-click="customer()"]').click()
        browser.element('#userSelect').type(f'{user.f_name} {user.l_name}')
        browser.element('[ng-show="custId != \'\'"]').click()
        browser.all('strong:nth-child(2)').second.should(have.text(str(n)))

    # with allure.step('Добавление клиента'):
    def add_customer(self, user: Customer):
        browser.element('[ng-click="manager()"]').click()
        browser.element('[ng-class=btnClass1]').click()
        browser.element('[ng-model=fName]').type(f'{user.f_name}')
        browser.element('[ng-model=lName]').type(f'{user.l_name}')
        browser.element('[ng-model=postCd]').type(f'{user.n_id}')
        browser.element('[class="btn btn-default"]').click()
        browser.switch_to.alert.accept()

#    with allure.step('Проверка добавленя клиента'):
    def check_add_customer(self, user: Customer):
        browser.element('[ng-class="btnClass3"]').click()
        browser.all('tr').element_by(have.text(f'{user.f_name}')).should(have.text(f'{user.f_name} {user.l_name} {user.n_id}'))


#    with allure.step('Удаление клиента'):
    def del_customer(self, user: Customer):
        browser.element('[ng-click="home()"]').click()
        browser.element('[ng-click="manager()"]').click()
        browser.element('[ng-class="btnClass3"]').click()
        browser.element('[ng-model=searchCustomer]').type(f'{user.f_name}')
        browser.element('[ng-click="deleteCust(cust)"]').click()

#    with (allure.step('Проверка удаления клиента')):
    def check_del_customer(self, user: Customer):
        browser.element('[ng-click="home()"]').click()
        browser.element('[ng-click="manager()"]').click()
        browser.element('[ng-class="btnClass3"]').click()
        browser.all('tr').element_by(have.text(f'{user.f_name}')).should(be.not_.existing)
