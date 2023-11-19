# Проект по тестированию учебной формы BankingProject сайта "www.globalqa.com"
> <a target="_blank" href="https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login">ссылка на форму</a>

![main page screenshot](./pictures/main_page.png)

----

### Список проверок, реализованных в автотестах

- [x] Поис клиента в списке
- [x] Добавление нового клиента
- [x] Удаление клиента 
- [x] Проверка депозита клиента
- [x] Пополнение депозита клиента
- [x] Списание депозита клиента

----

### Используемый стэк

<img title="Python" src="./pictures/python-original.svg" height="40" width="40"/> <img title="Pytest" src="./pictures/pytest-original.svg" height="40" width="40"/> <img title="Pycharm" src="./pictures/pycharm.png" height="40" width="40"/> <img title="Selenium" src="./pictures/selenium-original.svg" height="40" width="40"/> <img title="Selene" src="./pictures/selene.png" height="40" width="40"/> <img title="GitHub" src="./pictures/github-original.svg" height="40" width="40"/> <img title="Allure Report" src="./pictures/Allure_Report.png" height="40" width="40"/> <img title="Allure TestOps" src="./pictures/AllureTestOps.png" height="40" width="40"/><img title="Telegram" src="./pictures/tg.png" height="40" width="40"/><img title="Jira" src="./pictures/jira-original.svg" height="40" width="40"/> 

----

### Локальный запуск автотестов

#### Выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```

#### Получение отчёта:
```bash
allure serve build/allure-results
```

----

### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/lesson15-hw_jenkins_full_project//">Ссылка</a>

#### Параметры сборки


* environment - параметр определяет окружение для запуска тестов
* comment - комментарий


#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/lesson15-hw_jenkins_full_project//">проект</a>
2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать: PROD
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

----

### Allure отчет
#### Общие результаты

![allure_report_overview](./pictures/allure_all.jpg)

#### Список тест кейсов

![allure_reports_behaviors](./pictures/allure_behaviors.jpg)

#### Отчет прохождения теста

![allure_reports_graphs](./pictures/test_report.jpg)


----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3787/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](./pictures/allure_dashboards.jpg)

#### История запуска тестовых наборов

![allure_testops_launches](./pictures/allure_launches.jpg)

#### Тест кейсы

![allure_testops_suites](./pictures/allure_suites.jpg)

----



### Оповещения в Telegram

![telegram_allert](./pictures/telegram.png)

----

### Видео прохождения автотеста

![autotest_gif](./pictures/video.gif)

----

