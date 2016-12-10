import requests as rq
from bs4 import BeautifulSoup


class Base():
    def __init__(self):
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def page_parse(self):
        res = rq.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')

        return soup