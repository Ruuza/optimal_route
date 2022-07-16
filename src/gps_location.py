from geopy import distance as gdistance


class GPS_location:
    def __init__(self, latitude: float, longtitude: float) -> None:
        latitude = float(latitude)
        longtitude = float(longtitude)
        GPS_location.latitude_validator(latitude)
        GPS_location.longtitude_validator(longtitude)
        self._latitude = latitude
        self._longtitude = longtitude

    @property
    def latitude(self) -> float:
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float) -> None:
        GPS_location.latitude_validator(latitude)
        self._latitude = latitude

    @property
    def longtitude(self) -> float:
        return self._longtitude

    @longtitude.setter
    def longtitude(self, longtitude: float) -> None:
        GPS_location.longtitude_validator(longtitude)
        self._longtitude = longtitude

    @property
    def coord(self) -> tuple[float, float]:
        return (self._latitude, self._longtitude)

    def distance(self, location: "GPS_location") -> float:
        """Returns the distance between this location and another location in meters

        Args:
            location (GPS_location): Second location to compare to

        Returns:
            float: distance between locations in meters
        """
        return GPS_location.locations_distance(self, location)

    @staticmethod
    def locations_distance(
        location1: "GPS_location", location2: "GPS_location"
    ) -> float:
        """Returns the distance between two GPS_location in meters

        Args:
            location1 (GPS_location): First location
            location2 (GPS_location): Second location

        Returns:
            float: The location distance
        """

        return gdistance.distance(location1.coord, location2.coord).m

    @staticmethod
    def latitude_validator(latitude: float):
        """Validates the latitude

        Args:
            latitude (float): Latitude in decimal degrees format

        Raises:
            ValueError: If value is not valid latitude

        Returns:
            True: True if the value is correct
        """
        if not (-90 <= latitude <= 90):
            raise ValueError(
                "Latitude has to be in range between -90.0 to 90.0 degrees"
            )
        return True

    @staticmethod
    def longtitude_validator(longtitude: float):
        """Validates the longtitude

        Args:
            longtitude (float): Longtitude in decimal degrees format

        Raises:
            ValueError: If value is not valid longtitude

        Returns:
            True: True if the value is correct
        """
        if not (-180 <= longtitude <= 180):
            raise ValueError(
                "Longtitude has to be in range between -180.0 to 180.0 degrees"
            )
        return True
