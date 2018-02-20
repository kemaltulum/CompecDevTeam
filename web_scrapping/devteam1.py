from urllib import request 
from bs4 import BeautifulSoup
import re

class URL:
    urlString = ""
    params = {}
    def __init__(self, urlStringParam):
        self.urlString = urlStringParam
    def __str__(self):
        return self.urlString
    def addQueryParam(self, paramName, paramValue):
        self.params[paramName] = paramValue;
        if(len(self.params.keys()) > 0):
            self.urlString += "?" + paramName + "=" + str(paramValue)
        else:
            self.urlString += "&" + paramName + "=" + str(paramValue)

def readUrl(url):
    response = request.urlopen(url)
    return response.read().decode("utf-8")

url = URL("https://www.hurriyetemlak.com/konut-satilik/istanbul-sariyer-rumeli-hisari/listeleme")
url.addQueryParam("page", 2)
print(url)

responseString = readUrl(str(url))
print(responseString)