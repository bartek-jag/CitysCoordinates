import unittest
from location.coordinate import Coordinate


class CoordinateTests(unittest.TestCase):

    def test_forbidden_characters(self):
        city_coordinate = Coordinate("\\\"\'.,!@#$%^&*()1234567890{[}];:,<>.?/`~")
        self.assertEqual(city_coordinate.__str__(), "City not found")

    def test_example_non_ascii_characters(self):
        city_coordinate = Coordinate("Gdańsk")
        self.assertEqual(city_coordinate.__str__(), "54.35205 18.64637")

    def test_not_existing_city(self):
        city_coordinate = Coordinate("fdsfewsflhkkknnkaaawwdccc")
        self.assertEqual(city_coordinate.__str__(), "City not found")

    def test_convert_example_case(self):
        city_coordinate = Coordinate("Spychowo")
        city_coordinate.convert()
        self.assertEqual(city_coordinate.__str__(), "53°60'04.3\"N 21°34'73.8\"E")

    def test_convert_example_of_city_located_in_south_west_part_of_earth(self):
        city_coordinate = Coordinate("Buenos Aires")
        city_coordinate.convert()
        self.assertEqual(city_coordinate.__str__(), "34°61'31.5\"S 58°37'72.3\"W")

    def test_convert_negative_values(self):
        city_coordinate = Coordinate("")
        city_coordinate.latitude = "-11.23456"
        city_coordinate.longitude = "-12.34567"
        city_coordinate.convert()
        self.assertEqual(city_coordinate.__str__(), "11°23'45.6\"S 12°34'56.7\"W")

    def test_convert_values_without_fractional_part(self):
        city_coordinate = Coordinate("")
        city_coordinate.latitude = "11"
        city_coordinate.longitude = "12"
        city_coordinate.convert()
        self.assertEqual(city_coordinate.__str__(), "11°N 12°E")

    def test_convert_values_without_seconds_part(self):
        city_coordinate = Coordinate("")
        city_coordinate.latitude = "11.01"
        city_coordinate.longitude = "-12.1"
        city_coordinate.convert()
        self.assertEqual(city_coordinate.__str__(), "11°01'N 12°1'W")

    def test_convert_values_without_fractional_part_in_seconds_part(self):
        city_coordinate = Coordinate("")
        city_coordinate.latitude = "-11.0100"
        city_coordinate.longitude = "12.111"
        city_coordinate.convert()
        self.assertEqual(city_coordinate.__str__(), "11°01'00\"S 12°11'1\"E")
