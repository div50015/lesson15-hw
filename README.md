# Проект по тестированию учедной формы BankingProject сайта "www.globalqa.com"
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

<img title="Python" src="./pictures/python-original.svg" height="40" width="40"/> 
<img title="Pytest" src="./pictures/pytest-original.svg" height="40" width="40"/> 
<img title="Pycharm" src="./pictures/pycharm.png" height="40" width="40"/> 
<img title="Selenium" src="./pictures/selenium-original.svg" height="40" width="40"/> 
<img title="Selene" src="./pictures/selene.png" height="40" width="40"/> 
<img title="GitHub" src="./pictures/github-original.svg" height="40" width="40"/> 
<img title="Allure Report" src="./pictures/Allure_Report.png" height="40" width="40"/> 
<img title="Allure TestOps" src="./pictures/AllureTestOps.png" height="40" width="40"/>
<img title="Telegram" src="./pictures/tg.png" height="40" width="40"/>
<img title="Jira" src="./pictures/jira-original.svg" height="40" width="40"/> 

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
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/Saber-Interactive-Auto-Tests/">проект</a>
2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать: PROD
4. В поле "COMMENT" ввести комментарий
5. Нажать "Build"

----

### Allure отчет
#### Общие результаты 
![allure_report_overview](qa_guru_python_8_15/pictures/allure_report_overview.png)

#### Результаты прохождения теста
![allure_reports_behaviors](qa_guru_python_8_15/pictures/allure_reports_behaviors.png)

#### Графики

![allure_reports_graphs](qa_guru_python_8_15/pictures/alluere_reports_graphs_1.png)
![allure_reports_graphs](qa_guru_python_8_15/pictures/alluere_reports_graphs_2.png)

----

### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/project/3782/dashboards">Ссылка на проект</a>

#### Дашборд с общими показателями тестовых прогонов

![allure_test_ops_dashboards](qa_guru_python_8_15/pictures/allure_testops_dashboards.png)

#### История запуска тестовых наборов

![allure_testops_launches](qa_guru_python_8_15/pictures/allure_testops_launches.png)

#### Тест кейсы

![allure_testops_suites](qa_guru_python_8_15/pictures/allure_testops_suites.png)

----

### Интеграция с Jira
> <a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-953">Ссылка на проект</a>

![jira_project](qa_guru_python_8_15/pictures/jira_project.png)

----

### Оповещения в Telegram

![telegram_allert](/home/igor/PycharmProjects/lesson15-hw/pictures/telegram.png)

----

### Видео прохождения автотеста
![autotest_gif](qa_guru_python_8_15/pictures/autotest.gif)

----

### Mind map тест плана

![allure_reports_graphs](qa_guru_python_8_15/pictures/test-case-mind-map.png)
