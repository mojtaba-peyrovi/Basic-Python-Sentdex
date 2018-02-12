import urllib.request
import urllib.parse
#the following post sends s get request to the url and pulls the source code/
#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())
# pull the data from this link: https://pythonprogramming.net/search/?q=basic
'''
url = 'https://pythonprogramming.net'
values = {'q': 'basic'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)
'''
#parsing data from google search
try:
    x = urllib.request.urlopen('http://www.google.com/search?q=test')
    print(x.read())
except Exception as e:
    print(str(e))

try:
    url = 'http://www.google.com/search?q=test'
    headers = {}
    headers = {"User-Agent":"Mozilla/4.0"}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    response = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close
except Exception as e:
    print(str(e))
