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


# converting latitude and longitude
# (-?)12.34567 -> 12°34'56.7"
def convert(val, is_latitude):
    degree, min_sec = val.split(".")
    degree += "°"
    if min_sec != "":  # fractional part can be empty
        degree += min_sec[:2] + "'"
        if min_sec[2:4] != "":  # or short etc.
            degree += min_sec[2:4]
            if min_sec[4:] != "":
                degree += "." + min_sec[4:]
            degree += "\""
    if is_latitude:
        if degree[0] == "-":
            degree = degree[1:] + "S"
        else:
            degree += "N"
    else:
        if degree[0] == "-":
            degree = degree[1:] + "W"
        else:
            degree += "E"
    return degree


print("Enter city name: ")
city = input()
if city != "":
    contents = urlopen("http://api.geonames.org/search?maxRows=1"
                       + "&name_equals=" + quote(city)
                       + "&username=lightheaded").read()
    # example:
# http://api.geonames.org/search?&name_equals=spychowo&username=lightheaded

    # parsing xml content
    root = xml.etree.ElementTree.fromstring(contents)
    # check if there is a result and an error is not occurred
    if (root.findtext("totalResultsCount") != "0"
            and root.find("totalResultsCount") is not None):
        # get the values form result
        latitude = root.findtext("./geoname/lat")
        longitude = root.findtext("./geoname/lng")

        print(convert(latitude, True) + " "
              + convert(longitude, False))
