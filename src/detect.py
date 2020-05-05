from crawler import crawler
def detect():
    news=[]
    news=crawler.crawler()
    for i in news:
        print(i)
detect()