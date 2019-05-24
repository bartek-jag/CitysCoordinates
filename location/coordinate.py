from urllib.request import urlopen
from urllib.parse import quote  # encoding non-ASCII characters
import xml.etree.ElementTree

"""
User gives the name of the city and receives its coordinates
Input: city's name
Output: city's coordinates

Example:
Input: Spychowo
Output: 53°36'02.2"N 21°20'46.6"E
"""


class Coordinate:

    def __init__(self, city_name):
        self.latitude = ""
        self.longitude = ""
        if city_name != "":
            contents = urlopen("http://api.geonames.org/search?maxRows=1"
                               + "&name_equals=" + quote(city_name)
                               + "&username=lightheaded").read()
            # example:
            # http://api.geonames.org/search?&name_equals=spychowo&username=lightheaded

            # parsing xml content
            root = xml.etree.ElementTree.fromstring(contents)
            # check if there is a result and an error is not occurred
            if (root.findtext("totalResultsCount") != "0"
                    and root.find("totalResultsCount") is not None):
                # get the values form result
                self.latitude = root.findtext("./geoname/lat")
                self.longitude = root.findtext("./geoname/lng")

    def __str__(self):
        if self.latitude == "" or self.longitude == "":
            return "City not found"
        return self.latitude + " " + self.longitude

    # converting latitude and longitude
    def convert(self):
        if self.latitude != "" or self.longitude != "":
            if self.latitude.split(".").__len__() == 2:
                self.latitude = self.__convert(self.latitude)
            else:
                self.latitude += "°"
            if self.latitude[0] == "-":
                self.latitude = self.latitude[1:] + "S"
            else:
                self.latitude += "N"

            if self.longitude.split(".").__len__() == 2:
                self.longitude = self.__convert(self.longitude)
            else:
                self.longitude += "°"
            if self.longitude[0] == "-":
                self.longitude = self.longitude[1:] + "W"
            else:
                self.longitude += "E"

    # (-?)12.34567 -> 12°34'56.7"
    @staticmethod
    def __convert(coordinate):
        coordinate, coordinate_minutes_and_seconds = coordinate.split(".")
        coordinate += "°"
        if coordinate_minutes_and_seconds != "":  # fractional part can be empty
            coordinate += coordinate_minutes_and_seconds[:2] + "'"
            if coordinate_minutes_and_seconds[2:4] != "":  # or short etc.
                coordinate += coordinate_minutes_and_seconds[2:4]
                if coordinate_minutes_and_seconds[4:] != "":
                    coordinate += "." + coordinate_minutes_and_seconds[4:]
                coordinate += "\""
        return coordinate
