"crawl chinese novel from internet"
import urllib
from abstractcrawler import *

url = "http://www.cnnovels.com/wx/jingyong/index.html"

articleFolder = "jingyong"

def getArticleInfoListFunc(html):
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
print("start crawling...")
crawlBooks()
print("crawl finished")
