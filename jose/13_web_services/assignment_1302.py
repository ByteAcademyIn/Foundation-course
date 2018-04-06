"""
The program will prompt for a location, contact a web service 
and retrieve JSON for the web service and parse that data, 
and retrieve the first place_id from the JSON. A place ID is 
a textual identifier that uniquely identifies a place as within 
Google Maps.

API End Points
To complete this assignment, you should use this API endpoint 
that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/geojson?

This API uses the same parameter (address) as the Google API. 
This API also has no rate limit so you can test as often as you like. 
If you visit the URL with no parameters, you get a list of all 
of the address values which can be used with this API. To call 
the API, you need to provide address that you are requesting as 
the address= parameter that is properly URL encoded using 
the urllib.urlencode() fuction.

You can test to see if your program is working with a location of:
"South Federal University" 
place_id: "ChIJJ8oO7_B_bIcR2AlhC8nKlok". 
"allama iqbal open university islamabad" 
place_id: "ChIJA1SH1B1qIjkR5PsU3PVJ0x0"
"""

#importing libraries and json
import urllib.request, urllib.parse, urllib.error
import json

#prompts input
loc = input("Please enter the location: ")

#API End Points
api_end = "http://py4e-data.dr-chuck.net/geojson?"

#url encoding
address_param = urllib.parse.urlencode({'address': loc})

#url to contact the web service
url = api_end + address_param

#opening the url and reading
connection = urllib.request.urlopen(url)
raw_data = connection.read()

#decoding or deserialising 
parsed_data = json.loads(raw_data)

#extracting and printing the place id 
print("Place id:", parsed_data["results"][0]["place_id"])
