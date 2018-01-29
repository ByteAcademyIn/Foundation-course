import json
import urllib.request, urllib.parse

# Initialize the api link and ask the user for the location
api = 'http://py4e-data.dr-chuck.net/geojson?'
location = input('Please enter the location: ')
if len(location) <1: location='South Federal University'

# encode the location and add it to the url
url = api+urllib.parse.urlencode({'address':location})

# call the api and load the json
data = urllib.request.urlopen(url).read().decode()
info =json.loads(data)

# Find and print the place_id
print(info['results'][0]['place_id'])
