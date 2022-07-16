import json
import pytest
from src.gps_location import GPS_location
from src.city import City

TEST_FILE1 = "tests/test_cities1.json"


@pytest.fixture
def loc_brno() -> GPS_location:
    f = open(TEST_FILE1)
    data = json.load(f)
    loc_brno = GPS_location(data["Brno"][0], data["Brno"][1])
    return loc_brno


@pytest.fixture
def loc_prague() -> GPS_location:
    f = open(TEST_FILE1)
    data = json.load(f)
    loc_brno = GPS_location(data["Prague"][0], data["Prague"][1])
    return loc_brno


@pytest.fixture
def city_brno() -> City:
    f = open(TEST_FILE1)
    data = json.load(f)
    loc_brno = City(data["Brno"][0], data["Brno"][1], "Brno")
    return loc_brno


@pytest.fixture
def city_prague() -> City:
    f = open(TEST_FILE1)
    data = json.load(f)
    loc_brno = City(data["Prague"][0], data["Prague"][1], "Prague")
    return loc_brno
