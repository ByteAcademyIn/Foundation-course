import urllib
from bs4 import BeautifulSoup
url = ('http://py4e-data.dr-chuck.net/comments_42.html')
html = urllib.request.urlopen(url).read()
#print(html)
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
spans = soup('span')
#print(spans)
numbers = []
for span in spans:
    numbers.append(int(span.string))
print(sum(numbers))
