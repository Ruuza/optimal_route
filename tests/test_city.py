import json
from typing import List
from src.city import City

FILE = "tests/test_cities1.json"


def assert_cities(cities: List["City"]):

    assert len(cities) == 3
    assert cities[0].name == "Brno"
    assert cities[0].coord == (49.19564, 16.60895)

    assert cities[1].name == "Jihlava"
    assert cities[1].latitude == 49.39933
    assert cities[1].longtitude == 15.58344

    assert cities[2].name == "Prague"
    assert cities[2].coord == (50.08144, 14.424088)


def test_load_cities_file():
    cities = City.load_cities(from_json_file=FILE)

    assert_cities(cities)


def test_load_cities_dict():
    f = open(FILE)
    loaded_json = json.load(f)

    cities = City.load_cities(from_dict=loaded_json)

    assert_cities(cities)
