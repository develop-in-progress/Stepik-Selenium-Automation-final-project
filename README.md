# Фильнальный проект курса ["Автоматизация тестирования с помощью Selenium и Python"](https://stepik.org/course/575/syllabus)
### Пример проекта автоматизации тестирования на Selenium/PyTest с применением Page Object паттерна. Реализована возможность смены браузеров (для каждого тестового комплекта браузер запускатся отдельно и закрывается после теста) и маркировка тестов
1.  Клонируйте проект с GitHub и активируйте виртуальное окружение:
    ##### `python -m venv selenium_env`
    For Win:
    ##### `selenium_env\Scripts\activate.bat`
    For Unix:
    ##### `source selenium_env\Scripts\activate`
    Не сработает - запустите через sudo, или откройте проект в PyCharm, он поднимет venv с колен самостоятельно)
2.  Для запуска вам потребуется актуальная версия Питона, Селениум и PyTest
    Установка зависимостей (при наличии [Python](https://www.python.org/)) через терминал:
    ##### `pip install -r requirements.txt`
3. Актульные версии ChromeDriver, Geckodriver:
    * ###### [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
    * ###### [Geckodriver](https://github.com/mozilla/geckodriver/releases/)
   Скачайте архивы, распакуйте .exe файлы и обязательно добавьте драйвера (как на UNIX системах, так и Windows). 
4. Общий тест запускается командой (терминал открыт в папке проекта):
    ##### `pytest --browser_name=chrome`
    Смена браузера на Firefox:
    ##### `pytest --browser_name=firefox`
    Выполнение заданий с меткой 'need_review':
    ##### `pytest -v --tb=line --language=en -m need_review`
