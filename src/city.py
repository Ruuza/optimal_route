import json
from src.gps_location import GPS_location


class City(GPS_location):
    """Describes city and it's position"""

    def __init__(self, latitude, longtitude, name) -> None:
        self._name = name
        super().__init__(latitude, longtitude)

    def __str__(self) -> str:
        return f"{self._name}, {self._latitude}, {self._longtitude}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def load_cities(
        cls, from_dict: dict = None, from_json_file: str = None
    ) -> list["City"]:
        """Load cities from either a json file (path in the string format) or from a dict of the cities

            Format example:

        {
            "City_name_1": [
                "49.19564",
                "16.60895"
            ],
            "City_name_2": [
                "49.39933",
                "15.58344"
            ]
        }

            Raises:
                ValueError: Wrong values inserted

            Returns:
                list["City"]: List of loaded City classes
        """
        if from_dict and from_json_file:
            raise ValueError(
                "only one of the options [from_object, from_json_file] can be selected!"
            )

        if from_json_file:
            f = open(from_json_file)
            data = json.load(f)
            data = data
        else:
            data = from_dict

        cities: list["City"] = []

        for city_name in data:
            cities.append(
                cls(float(data[city_name][0]), float(data[city_name][1]), city_name)
            )

        return cities
