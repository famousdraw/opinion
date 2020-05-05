from bs4 import BeautifulSoup
import re
import requests
def crawler():
    url='https://news.163.com'
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    def has_no_class(tag):
        return not tag.has_attr('class') and not tag.has_attr('em')
    news_links=soup.find_all(has_no_class,href=re.compile("https://news.163.com/20"))
    news=[]
    for i in news_links:
        #print(i.text)
        news.append(i.text)
    #print(news)
    return(news)

