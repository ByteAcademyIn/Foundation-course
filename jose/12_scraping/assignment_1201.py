"""
Scraping Numbers from HTML using BeautifulSoup

The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment:

http://py4e-data.dr-chuck.net/comments_42.html (Sum = 2553)
http://py4e-data.dr-chuck.net/comments_64152.html (Sum = 2600)

You do not need to save these files to your folder since your program will read the data directly from the URL.

Hint: 
Look at the source code(HTML) of each file. 
Notice the tag within which you have the numbers. Try to extract those specific tags and their contents using BeautifulSoup.
Be careful of what the return type of each method is (string or a list or something else?).
"""


#importing libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#prompts input
url = input("Please enter the url: ")

#opening and parsing the url
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#initialising addi
addi=0

#retrieves span tags
tags = soup('span')

#extracting and compute the sum 
for tag in tags:
    y=tag.text
    addi+=int(y)

#print the sum    
print("Sum =",addi)
