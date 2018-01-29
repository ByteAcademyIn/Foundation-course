import urllib.request
import json

# The URL to be used for extracting JSON
url1 = 'http://py4e-data.dr-chuck.net/comments_42.json'
url2 = 'http://py4e-data.dr-chuck.net/comments_64155.json'

#Open the url, read the json and load it
data = urllib.request.urlopen(url2).read().decode()
info = json.loads(data)

#Extract all the integers in 'count' and sum them up
'''
num = []
comments = info['comments']
for comment in comments:
    num.append(comment['count'])
print(sum(num))
'''

#Using List comprehension
print('Sum:',sum([comment['count'] for comment in info['comments']]))
