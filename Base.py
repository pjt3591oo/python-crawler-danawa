''''''

import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Base():
    def __init__(self):
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.browser = webdriver.Chrome('chromedriver.exe')

    def page_parse(self):
        res = rq.get(self.url, headers=self.headers)
        soup = BeautifulSoup(res.text, 'lxml')

        return soup

    def click(self, tag):
        self.browser.find_element_by_css_selector(tag).click()

    def hover(self, tag):
        hover = ActionChains(self.browser).move_to_element(self.browser.find_element_by_css_selector(tag))
        hover.perform()