'''
Scraping Numbers from HTML using BeautifulSoup

The program will use urllib to read the HTML from the data files below, and
parse the data, extracting numbers and compute the sum of the numbers in the
file.

We provide two files for this assignment:

http://py4e-data.dr-chuck.net/comments_42.html (Sum = 2553)
http://py4e-data.dr-chuck.net/comments_64152.html (Sum = 2600)

You do not need to save these files to your folder since your program will read
the data directly from the URL.

Hint:
Look at the source code(HTML) of each file.
Notice the tag within which you have the numbers. Try to extract those specific
tags and their contents using BeautifulSoup.
Be careful of what the return type of each method is (string or a list or
something else?).
'''

#importing libraries
import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup

#input prompts
url = input('Enter URL: ')

#using urllib to open the webpage
html_source = urllib.request.urlopen(url)

#using BeautifulSoup to parse the html_source
soup = BeautifulSoup(html_source, 'html5lib')

#initializing the list of numbers
num = []

#Retrieving <span> tags
tags = soup('span')

for tag in tags:
    num.append(tag.text)

#converting the num list to integer format
numbers = list(map(int, num))

#printing the Sum
print('Sum:', sum(numbers))
