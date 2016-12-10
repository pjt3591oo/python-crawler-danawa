'''
해당 페이지는 uase-agent를 웹브라우저로 설정을 해준다. 해주지 않을 경우 서버에서 정상적인 페이지 응답을 하지 않는다.
카테고리가 4단계로 구성이 되있지만 2단계로 압축을 하였다.

페이지에 접속 후 좌측에 전체 카테고리를 펼친다. 이때 카테고리가 상위카테고리와 하위 카테고리가 나타난다.
상위 카테고리에 hover를 하면 브라우저는 모든 상위카테고리에 대하여 모든 하위 카테고리 리스트들을 웹에 띄운다.

여기서 하위 카테고리를 접속을 한다.
이미지, 이름, 가격을 수집 해당 카테고리의 페이지를 확인 마지막이면 다음 카테고리 접속.
반복
'''

from Base import Base
from Page import Page
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


class Danawa(Base):

    browser = webdriver.Chrome('chromedriver.exe')

    def __init__(self):
        super().__init__()
        self.url = "http://www.danawa.com"

        self.category_view = 'a.nav_menu01'
        self.category_nav = 'a.nav_menu02'
        self.category_sub = 'div.wrap_height li a'

    def crawler(self):
        self.browser.get(self.url)
        self.__click(self.category_view)
        self.category_nav_hover()

    def category_nav_hover(self):
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        self.__hover(self.category_nav)
        self.collect_category()

    def collect_category(self):
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        cate_list = []
        for a in soup.select(self.category_sub):
            temp = {"url": '', "title": ''}
            temp['url'] = a.get('href')
            temp['title'] = a.text.replace('\t', '')
            cate_list.append(temp)

        Page(cate_list, self.browser).page_crawler()

    def __click(self, tag):
        self.browser.find_element_by_css_selector(tag).click()

    def __hover(self, tag):
        hover = ActionChains(self.browser).move_to_element(self.browser.find_element_by_css_selector(tag))
        hover.perform()