"crawl chinese novel from internet"
import urllib
from bs4 import BeautifulSoup
from abstractcrawler import *

def getArticleInfoFunc(ele):
    '''pass in soup element'''
    return

def getChapterInfoFunc(ele):
    '''pass in soup element'''
    return

def getChapterContentFunc(ele):
    '''pass in soup element'''
    return

def crawlBooks():
    crawler = ArticleListGetter(args)
    crawler.storeArticles()

args['url'] = "http://www.cnnovels.com/wx/jingyong/index.html"
args['articleFolder'] = "jingyong"
args['articleId'] = "body > center:nth-of-type(4) > table a"
args['getArticleInfoFunc'] = getArticleInfoFunc
args['chapterId'] = ""
args['getChapterInfoFunc'] = getChapterInfoFunc
args['getChapterContentFunc'] = getChapterContentFunc

#test
# print("start crawling...")
# crawlBooks()
# print("crawl finished")

args['getArticleInfoListFunc'](getHtmlFromUrl(args['url']))