import requests
from constant import *

def test_search_id():
    response = requests.get(base_url + "movie/666", headers=my_headers)

    assert response.status_code == 200

def test_search_with_filters():
    response = requests.get(base_url + 
    "movie?notNullFields=name&selectFields=name&selectFields=id", 
    headers=my_headers)
    assert response.status_code == 200

def test_search_title():
    response = requests.get(base_url +
    "movie/search?query=8 миля&limit=1", headers=my_headers)
    assert response.status_code == 200

def test_actors():
    response = requests.get(base_url +
    "person?selectFields=id&selectFields=name", headers = my_headers)
    assert response.status_code == 200

def test_reviews():
    response = requests.get(base_url +
    "review?authorId=23107424&movieId=1402937", headers = my_headers)
    assert response.status_code == 200