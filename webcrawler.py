"crawl chinese novel from internet"
import urllib
from bs4 import BeautifulSoup
from abstractcrawler import *

url = "http://www.cnnovels.com/wx/jingyong/index.html"

articleFolder = "jingyong"

def getArticleInfoListFunc(html):
    selector = "body > center:nth-of-type(4) > table a"
    soup = BeautifulSoup(html, 'html.parser')
    articleElementList = soup.select(selector)
    print(articleElementList)
    return

def getChapterListFunc(html):
    return

def getChapterContentFunc(html):
    return

args = {
    'url': url,
    'articleFolder': articleFolder,
    'getArticleInfoListFunc': getArticleInfoListFunc,
    'getChapterListFunc': getChapterListFunc,
    'getChapterContentFunc': getChapterContentFunc,
}

def crawlBooks():
    crawler = ArticleListGetter(args)
    crawler.storeArticles()

#test
# print("start crawling...")
# crawlBooks()
# print("crawl finished")

getArticleInfoListFunc(getHtmlFromUrl(url))
