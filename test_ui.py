import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(300)
    yield driver
    driver.quit()

@allure.epic("Тестирование UI")
@allure.title("Поиск фильма по названию")
@allure.severity("BLOCKER")
def test_search(chrome_browser):
    with allure.step("Переход на сайт кинопоиска"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод названия фильма в поисковик"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("Переводчик")
        chrome_browser.find_element(By.ID, "suggest-item-film-927898").click()
    with allure.step("Проверка на соответствие названия фильма"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Переводчик (2022)"

@allure.epic("Тестирование UI")
@allure.title("Проверка кнопки 'Онлайн-кинотеатр'")
@allure.severity("BLOCKER")
def test_online_cinema(chrome_browser):
    with allure.step("Переход на сайт кинопоиска"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Переход на страницу онлайн-кинотеатра"):
        chrome_browser.find_element(By.CSS_SELECTOR, "a[data-tid='acc26a70']").click()
    with allure.step("Проверка наличия веб-элемента на странице"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='component']").text == "Попробовать 30 дней бесплатно"

@allure.epic("Тестирование UI")
@allure.title("Поиск на латинице")
@allure.severity("CRITICAL")
def test_search_english(chrome_browser):
    with allure.step("Переход на сайт кинопоиска"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод названия фильма на латинице в поисковик"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("Covenant")
        chrome_browser.find_element(By.ID, "suggest-item-film-927898").click()
    with allure.step("Проверка на наличие и отображение фильма"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Переводчик (2022)"

@allure.epic("Тестирование UI")
@allure.title("Негативный тест. Поиск с вводом спецсимволов")
@allure.severity("NORMAL")
def test_negative_search(chrome_browser):
    with allure.step("Переход на сайт кинопоиска"):
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Ввод спецсимволов в поисковик"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("#$#")
    with allure.step("Проверка результата поиска"):
        assert chrome_browser.find_element(By.CSS_SELECTOR, "div.styles_emptySuggest__XEkB0").text == "По вашему запросу ничего не найдено"

@allure.epic("Тестирование UI")
@allure.title("Поиск с пустым полем")
@allure.severity("CRITICAL")
def test_empty_search_field(chrome_browser):
    with allure.step("Переход на сайт кинопоиска"): 
        chrome_browser.get("https://www.kinopoisk.ru/")
    with allure.step("Поиск фильма с пустым значением поисковика"):
        chrome_browser.find_element(By.NAME, "kp_query").send_keys("")
        chrome_browser.find_element(By.CSS_SELECTOR, "button[type='Submit']").click()
    with allure.step("Проверка отображения функции 'случайный фильм'"):
        assert chrome_browser.find_element(By.ID, "search").is_displayed()