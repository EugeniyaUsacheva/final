import requests
import pytest

url = "https://api.kinopoisk.dev/v1.4/movie"
token = "ZETEA7K-WFZ4G2T-K39J7XA-5HYRXS2"
invalid_token = "invalid_token_for_testing"


@pytest.mark.parametrize("film_id",
                         [535341, 258687])
def test_film_by_id(film_id):
    headers = {
        "X-API-KEY": token,
        "Content-Type": "application/json"
    }
    get_url = f"{url}/{film_id}"

    response = requests.get(get_url, headers=headers)

    assert response.json()["id"] == film_id
    assert response.json()["name"] == "1+1" or response.json()["name"] == "Интерстеллар"


@pytest.mark.parametrize("film_id",
                         [535341, 258687])
def test_film_by_id_negative(film_id):
    headers = {
        "X-API-KEY": invalid_token,
        "Content-Type": "application/json"
    }
    get_url = f"{url}/{film_id}"

    response = requests.get(get_url, headers=headers)

    assert response.status_code == 401


@pytest.mark.parametrize("film_name",
                         ["Шрэк"])
def test_film_by_name(film_name):
    headers = {
        "X-API-KEY": token,
        "Content-Type": "application/json"
    }
    params = {
        "query" : film_name,
        "page" : 1,
        "limit" : 10
    }

    response = requests.get(url+"/search", headers=headers, params = params)

    assert response.status_code == 200
    assert response.json()["docs"][0]["name"] == film_name
