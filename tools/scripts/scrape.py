from bs4 import BeautifulSoup
import urllib.request
import requests
import re

def getFilename(url):
	name = url.split("/")
	return name[4]
li = [""]
html_page = urllib.request.urlopen("https://posoco.in/reports/daily-reports/daily-reports-2018-19/")
soup = BeautifulSoup(html_page, "html.parser")
for link in soup.findAll('a'):
    li.append(link.get('href'))

listToStr = ' '.join([str(elem) for elem in li])
urls = re.findall('http[s]?://posoco.in/download/[0-3][0-9]\-0[4-6]\-18(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', listToStr)
print (urls)
print(len(urls))


for url in urls:
	r = requests.get(url, allow_redirects=True)
	filename = getFilename(url)
	open("../2018/pdfs/{}.pdf".format(filename), 'wb').write(r.content)
