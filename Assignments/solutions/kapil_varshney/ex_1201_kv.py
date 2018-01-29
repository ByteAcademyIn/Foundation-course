from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
# Create variables to hold the links
link1= 'http://py4e-data.dr-chuck.net/comments_42.html'
link2 = 'http://py4e-data.dr-chuck.net/comments_64152.html'

'''
#Open the link and make a BeautifulSoup object
html = urlopen(link1)
soup = bs(html, 'html.parser')

#Extract all span tags and their contents
spans = soup('span')
sumnum = 0

#Iterate over each span in the list spans
for span in spans:
    #print (span.contents)
    sumnum = sumnum+int(span.contents[0])

print(sumnum)
'''

#Using List comprehension
print(sum([int(span.contents[0]) for span in bs(urlopen(link2), 'html.parser')('span')]))
