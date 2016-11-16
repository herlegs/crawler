"crawl chinese novel from internet"
import urllib

__domain = "http://www.cnnovels.com"
category = {
	"JinYong": "/wx/jingyong/index.html"
}

def getHtmlFromUrl(url):
    url = urllib.urlopen(url)
    content = url.read()

    url.close()
    return

def writeToFile(content, filename):
    out = open(filename, "w")
    out.write(content)
    out.close()

print(category)
