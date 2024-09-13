import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(300)
    yield driver
    driver.quit()

def test_search(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Переводчик")
    chrome_browser.find_element(By.ID, "suggest-item-film-927898").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Переводчик (2022)"

def test_online_button(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.CSS_SELECTOR, "a[data-tid='acc26a70']").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='component']").text == "Попробовать 60 дней бесплатно"

def test_search_english(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("Covenant")
    chrome_browser.find_element(By.ID, "suggest-item-film-927898").click()
    assert chrome_browser.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Переводчик (2022)"

def test_negative_search(chrome_browser):
    chrome_browser.get("https://www.kinopoisk.ru/")
    chrome_browser.find_element(By.NAME, "kp_query").send_keys("#$#")
    assert chrome_browser.find_element(By.CSS_SELECTOR, "div.styles_emptySuggest__XEkB0").text == "По вашему запросу ничего не найдено"

def test