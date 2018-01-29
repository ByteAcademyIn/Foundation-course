from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

# Ask the user to input URL, count and position of name
url = input('Enter URL: ')
if len(url)<1 : url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
count = int(input('Enter count: '))
pos = int(input('Enter position: '))-1
next_link = None

# Create a loop to extract the link and the name 'count' number of times
while count>0:

    # Change the url except for the first time
    if next_link is not None: url = next_link
    print ('Retrieving: '+url)

    #Open the url and extract the anchor tags
    soup = bs(urlopen(url), 'html.parser')
    tags = soup('a')

    #Find the link at the specified position and extract the name
    tag = tags[pos]
    next_link = tag.get('href', None)
    name = tag.contents[0]

    #Decrement the count variable
    count-=1

# Print the final name
print ('The final name is:',name)
