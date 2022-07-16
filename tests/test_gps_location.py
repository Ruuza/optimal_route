import pytest  # noqa
from src.gps_location import GPS_location
from src.city import City
from tests.conftest import city_brno, loc_brno


@pytest.mark.parametrize("latitude", [0, 20, -24, 22.5135, -89.9999, -90.0, 90.0])
@pytest.mark.parametrize("longtitude", [0, 21, -47, 57.352343, -179.999, -180, 180])
@pytest.mark.parametrize("cls", [City, GPS_location])
def test_create_ok(latitude, longtitude, cls):
    if cls == City:
        loc = cls(latitude, longtitude, "CityName")
    else:
        loc = cls(latitude, longtitude)
    assert loc.latitude == latitude
    assert loc.longtitude == longtitude


@pytest.mark.parametrize("latitude", [-90.1, 90.2123142, 120.12423, -126])
@pytest.mark.parametrize("cls", [City, GPS_location])
def test_create_fail_latitude(latitude, cls):
    longtitude = 0

    with pytest.raises(ValueError):
        if cls == City:
            cls(latitude, longtitude, "CityName")
        else:
            cls(latitude, longtitude)


@pytest.mark.parametrize("longtitude", [-180.1, 180.21424, -10000, 214543])
@pytest.mark.parametrize("cls", [City, GPS_location])
def test_create_fail_longtitude(longtitude, cls):
    latitude = 0

    with pytest.raises(ValueError):
        if cls == City:
            cls(latitude, longtitude, "CityName")
        else:
            cls(latitude, longtitude)


@pytest.mark.parametrize("loc_brno", [loc_brno, city_brno], indirect=True)
@pytest.mark.parametrize("loc_prague", [loc_brno, city_brno], indirect=True)
@pytest.mark.parametrize("cls", [GPS_location, City])
def test_distance(loc_brno: GPS_location, loc_prague: GPS_location, cls):
    approx_real_distance = 185600
    delta = 500
    distance_from_brno = loc_brno.distance(loc_prague)
    distance_from_prague = loc_prague.distance(loc_brno)
    distance_between = GPS_location.locations_distance(loc_brno, loc_prague)

    assert distance_from_brno == distance_from_prague == distance_between
    assert abs(approx_real_distance - distance_between) < delta
