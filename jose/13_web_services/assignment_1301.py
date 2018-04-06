"""
The program will prompt for a URL, read the JSON data 
from that URL using urllib and then parse and extract 
the comment counts from the JSON data, and compute 
the sum of the numbers in the file. 

We provide two files for this assignment.
http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
http://py4e-data.dr-chuck.net/comments_64155.json (Sum ends with 64)

You do not need to save these files to your folder 
since your program will read the data directly from the URL.

"""
#importing libraries and json
import urllib.request, urllib.parse, urllib.error
import json

#prompts input
url = input("Please enter the json URL: ")

#opening the url and reading 
connection = urllib.request.urlopen(url)
raw_data = connection.read()

#decoding or deserialising 
parsed_data = json.loads(raw_data)
comments = parsed_data["comments"]

#initiaising count
counts = []

#extraxting the comment counts
for comment in comments:
    counts.append(comment["count"])

# prints sum
print("Sum =",sum(counts))
