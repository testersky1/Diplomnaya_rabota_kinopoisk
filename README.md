# Diplomnaya_rabota_kinopoisk
Автоматизированное тестирование сайта "Кинопоиск"
Важная инфо:
Из-за специфики защиты сайта, используется imlicitly wait для обхода капчи. Необходимо проходить проверки на капчу вручную.

Шаги:
Склонировать репозиторий "https://github.com/testersky1/Diplomnaya_rabota_kinopoisk.git"
Установить окружение "python -m pip install -r requirements.txt"
Запустить тесты "pytest -s -v --alluredir allure_results"
Просмотреть отчет "allure serve allure_results"

Стэк:
Selenium
Webdriver-manager
Requests
PyTest
Allure

Структура:
./tests - тесты
    test_api.py - API тесты
    test_ui.py - UI тесты
conftest.py - фикстуры
requirements.txt - настройка окружения

Библиотеки:
pip install selenium
pip install webdriver-manager
pip install pytest
pip install requests
pip install allure-pytest

