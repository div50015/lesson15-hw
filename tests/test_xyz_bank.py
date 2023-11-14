import time
from selene import browser, have, be, query
import os
from selene import command

def test_add_customer():
    browser.open('/')

    browser.element('[ng-click="manager()"]').click()
    browser.element('[ng-class=btnClass1]').click()
    browser.element('[ng-model=fName]').type('Piter')
    browser.element('[ng-model=lName]').type('Pen')
    browser.element('[ng-model=postCd]').type('E12345')
    browser.element('[class="btn btn-default"]').click()

    browser.switch_to.alert.accept()

    browser.element('[ng-class="btnClass3"]').click()

    browser.all('tr').element_by(have.text('Piter')).should(have.text('Piter Pen E12345'))

    browser.element('[ng-click="home()"]').click()

    browser.element('[ng-click="manager()"]').click()

    browser.element('[ng-class="btnClass3"]').click()

    browser.element('[ng-model=searchCustomer]').type('Piter')

    browser.element('[ng-click="deleteCust(cust)"]').click()


def test_deopsit_and_withdrawal():
    browser.open('/')

    browser.element('[ng-click="customer()"]').click()
    browser.element('#userSelect').type('Harry Potter')
    browser.element('[ng-show="custId != \'\'"]').click()
    browser.all('strong:nth-child(2)').second.should(have.text('0'))

    browser.element('[ng-click="deposit()"]').click()
    browser.element('input[ng-model=amount]').type('100')
    browser.element('button[type=submit]').click()
    browser.element('span[ng-show=message]').should(have.exact_text('Deposit Successful'))

    browser.element('[ng-click="home()"]').click()

    browser.element('[ng-click="customer()"]').click()
    browser.element('#userSelect').type('Harry Potter')
    browser.element('[ng-show="custId != \'\'"]').click()
    browser.all('strong:nth-child(2)').second.should(have.text('100'))

    browser.element('[ng-click="withdrawl()"]').click()
    browser.element('input[ng-model=amount]').type('70')
    browser.element('button[type=submit]').click()
    browser.element('span[ng-show=message]').should(have.exact_text('Transaction successful'))
    browser.element('[ng-click="home()"]').click()

    browser.element('[ng-click="customer()"]').click()
    browser.element('#userSelect').type('Harry Potter')
    browser.element('[ng-show="custId != \'\'"]').click()
    browser.all('strong:nth-child(2)').second.should(have.text('30'))

