import urllib
import os

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
        return self.getArticleListFunc(html)

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
    getChapterListFunc:
    '''
    def __init__(self, articleInfo, args, folder=None):
        self.args = args
        self.title = articleInfo['title']
        self.url = articleInfo['url']
        self.getChapterListFunc = args['getChapterListFunc']
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
        return self.getChapterListFunc(html)



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
    connection = urllib.urlopen(url)
    content = connection.read()
    connection.close()
    return content