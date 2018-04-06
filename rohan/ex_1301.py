'''
Extracting Data from JSON
The program will prompt for a URL, read the JSON data from that URL using
urllib and then parse and extract the comment counts from the JSON data, and
compute the sum of the numbers in the file.

We provide two files for this assignment.
http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
http://py4e-data.dr-chuck.net/comments_64155.json (Sum ends with 64)

You do not need to save these files to your folder since your program will read
the data directly from the URL.
'''

#importing libraries
import urllib.request, urllib.parse, urllib.error
import json

#input prompts
url = input('Enter URL: ')

#opening the webpage and getting the data
page = urllib.request.urlopen(url)
data = page.read().decode()

#loading JSON Data
info = json.loads(data)

#initiazing the variable to store the sum
sum = 0

for i in info["comments"]:
    num = int(i["count"])
    sum += num

print('Sum =', sum)
