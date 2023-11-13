import time
from selene import browser, have, be
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
    time.sleep(5)
    browser.element('[ng-click="home()"]').click()

    browser.element('[ng-click="manager()"]').click()
    time.sleep(5)
    browser.element('[ng-class="btnClass3"]').click()
    time.sleep(5)
    browser.element('[ng-model=searchCustomer]').type('Piter')
    time.sleep(5)
    browser.element('[ng-click="deleteCust(cust)"]').click()
    time.sleep(5)




