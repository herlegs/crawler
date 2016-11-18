"crawl chinese novel from internet"
from bs4 import BeautifulSoup
from abstractcrawler import *

def getArticleInfoFunc(ele, articleListUrl):
    articleInfo = {}
    articleInfo['title'] = ele.get_text()
    articleInfo['url'] = articleListUrl + ele['href']
    return articleInfo

def getChapterInfoFunc(ele, articleUrl):
    chapterInfo = {}
    chapterInfo['title'] = ele.get_text()
    chapterInfo['url'] = articleUrl.replace("index.html", ele['href'].replace("html", "htm"))
    return chapterInfo

def getChapterContentFunc(html):
    selector = "body > center:nth-of-type(4) > table td"
    soup = BeautifulSoup(html, 'html.parser')
    contentElement = soup.select(selector)[0]
    content = contentElement.get_text()
    return content

def crawlBooks():
    crawler = ArticleListGetter(settings)
    crawler.storeArticles()

settings['url'] = "http://www.cnnovels.com/wx/jingyong/"
settings['articleFolder'] = "jingyong"
# settings['getArticleInfoListFunc'] = getArticleInfoListFunc
# settings['getChapterInfoListFunc'] = getChapterInfoListFunc
settings['articleId'] = "body > center:nth-of-type(4) > table a:nth-of-type(6)"
settings['getArticleInfoFunc'] = getArticleInfoFunc
settings['chapterId'] = "body > center:nth-of-type(5) > table a"
settings['getChapterInfoFunc'] = getChapterInfoFunc
settings['getChapterContentFunc'] = getChapterContentFunc

#test list page
# listUrl = "http://www.cnnovels.com/wx/jingyong/"
# settings['getArticleInfoListFunc'](getHtmlFromUrl(listUrl), listUrl)
#test article page
# articleUrl = 'http://www.cnnovels.com/wx/jingyong/eagle/index.html'
# settings['getChapterInfoListFunc'](getHtmlFromUrl(articleUrl), articleUrl)
#test chapter page
# chapterUrl = "http://www.cnnovels.com/wx/jingyong/eagle/001.htm"
# settings['getChapterContentFunc'](getHtmlFromUrl(chapterUrl))

print("start crawling...")
crawlBooks()
print("crawl finished")