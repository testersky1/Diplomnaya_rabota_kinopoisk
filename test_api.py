import requests
import allure
from constant import *


@allure.epic("Тестирование API")
@allure.title("Поиск фильма по id через API")
@allure.severity("CRITICAL")
def test_search_id():
    with allure.step("api.Поиск фильма по {id}"):
        response = requests.get(base_url + "movie/" + id, headers=my_headers)
        with allure.step("Проверка названия фильма"):
            assert response.json()['name'] == "Форсаж"
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

@allure.epic("Тестирование API")
@allure.title("Поиск фильма по фильтру")
@allure.severity("CRITICAL")
def test_search_with_filters():
    with allure.step("api.Поиск фильма по фильтру"):
        response = requests.get(base_url + 
        "movie?notNullFields=name&selectFields=name&selectFields=id", 
        headers=my_headers)
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

@allure.epic("Тестирование API")
@allure.title("Поиск фильма по названию")
@allure.severity("CRITICAL")
def test_search_title():
    with allure.step("api.Поиск фильма по названию"):
        response = requests.get(base_url +
        "movie/search?query=8 миля&limit=1", headers=my_headers)
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

@allure.epic("Тестирование API")
@allure.title("Получение списка актеров")
@allure.severity("NORMAL")
def test_actors():
    with allure.step("api.Получение списка актеров"):
        response = requests.get(base_url +
        "person?selectFields=id&selectFields=name", headers = my_headers)
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200

@allure.epic("Тестирование API")
@allure.title("Поиск конкретного отзыва от пользователя")
@allure.severity("MINOR")
def test_reviews():
    with allure.step("api.Поиск отзыва по автору и фильму"):
        response = requests.get(base_url +
        "review?authorId=23107424&movieId=1402937", headers = my_headers)
        with allure.step("Проверка статус-кода"):
            assert response.status_code == 200