import os
from six.moves.urllib.request import urlopen
from bs4 import BeautifulSoup

class ArticleListGetter():
    '''
    needed in args:
    url:
    getArticleInfoListFunc:
    articleFolder:
    '''
    def __init__(self, args):
        self.args = args
        self.url = args['url']
        self.getArticleListFunc = args['getArticleInfoListFunc']
        self.articleFolder = dict.get(args, 'articleFolder', self.url)

    def getArticleInfoList(self):
        html = getHtmlFromUrl(self.url)
        return self.getArticleListFunc(html, self.url)

    def storeArticles(self):
        articleInfoList = self.getArticleInfoList()
        if articleInfoList is not None and len(articleInfoList) > 0:
            os.makedirs(self.articleFolder)
        for articleInfo in articleInfoList:
            articleTitle = articleInfo['title']
            articleUrl = articleInfo['url']
            articleGetter = ArticleGetter(articleInfo, self.args, folder=self.articleFolder)
        return



class ArticleGetter():
    '''
    needed in args:
    getChapterInfoListFunc:
    '''
    def __init__(self, articleInfo, args, folder=None):
        self.args = args
        self.title = articleInfo['title']
        self.url = articleInfo['url']
        self.getChapterInfoListFunc = args['getChapterInfoListFunc']
        self.articleFilename = self.title + ".txt"
        if folder is not None:
            self.articleFilename = folder + "/" + self.articleFilename

    def storeArticle(self):
        articleContent = self.title + "\n"
        chapterInfoList = self.getChapterListInfo()
        if chapterInfoList is not None and len(chapterInfoList) > 0:
           for chapterInfo in chapterInfoList:
               chapterContent = Chapter(chapterInfo, self.args).getContent()
               articleContent += chapterContent + "\n"
        else:
            chapterInfo = {'url': self.url}
            chapterContent = Chapter(chapterInfo, self.args).getContent()
            articleContent += chapterContent + "\n"
        articleFile = open(self.articleFilename, "w+")
        articleFile.write(articleContent)
        articleFile.close()

    def getChapterListInfo(self):
        html = getHtmlFromUrl(self.url)
        return self.getChapterInfoListFunc(html, self.url)



class Chapter():
    '''
    needed in args:
    getChapterContentFunc:
    '''
    def __init__(self, chapterInfo, args):
        self.args = args
        self.url = chapterInfo['url']
        self.title = dict.get(chapterInfo, 'title', None)
        self.getContentFunc = args['getChapterContentFunc']

    def getContent(self):
        html = getHtmlFromUrl(self.url)
        content = ""
        if self.title is not None:
            content += self.title + "\n"
        content += self.getContentFunc(html)
        return content

def getHtmlFromUrl(url):
    connection = urlopen(url)
    content = connection.read()
    connection.close()
    return content

def getArticleInfoListFunc(html, url):
    '''return list of article info:
    {'url': required, 'title':required}'''
    selector = settings['articleId']
    soup = BeautifulSoup(html, 'html.parser')
    articleElementList = soup.select(selector)
    articleInfoList = []
    for ele in articleElementList:
        articleInfo = settings['getArticleInfoFunc'](ele, url)
        articleInfoList.append(articleInfo)
    return articleInfoList

def getChapterInfoListFunc(html, url):
    '''return list of article info:
    {'url': required, 'title':optional}'''
    selector = settings['chapterId']
    soup = BeautifulSoup(html, 'html.parser')
    chapterElementList = soup.select(selector)
    chapterInfoList = []
    for ele in chapterElementList:
        chapterInfo = settings['getChapterInfoFunc'](ele, url)
        chapterInfoList.append(chapterInfo)
    return chapterInfoList

settings = {
    # REQUIRED: article list url
    'url': None,
    # OPTIONAL: folder to store all articles under the article list url
    # if None is passed then it will use url as folder name
    'articleFolder': None,
    # OPTIONAL: function to extract list of article info from the article list page
    # By default it will use 'articleId' to get article element
    # and use getArticleInfoFunc(element=ele, url=article list url) to get article info object
    # Can be overrided
    'getArticleInfoListFunc': getArticleInfoListFunc,
    # OPTIONAL: function to extract list of chapter info from the article page
    # similar to getArticleInfoListFunc
    # use 'chapterId' and 'getChapterInfoFunc'
    'getChapterInfoListFunc': getChapterInfoListFunc,
    # REQUIRED: article object css selector
    'articleId': None,
    # REQUIRED
    # Parameter:
    # 1. article object fetched by 'articleId'
    # 2. url of article list page
    'getArticleInfoFunc': None,
    # REQUIRED: chapter object css selector
    'chapterId': None,
    # REQUIRED
    # Parameter:
    # 1. chapter object fetched by 'chapterId'
    # 2. url of article page
    'getChapterInfoFunc': None,
    # REQUIRED: function to extract content from chapter page
    # Parameter:
    # 1. html of chapter page
    'getChapterContentFunc': None,
}


