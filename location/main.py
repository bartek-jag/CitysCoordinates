from location.coordinate import Coordinate

city = input("Enter city name: ")
city_coordinates = Coordinate(city)
city_coordinates.convert()
print(city_coordinates)
