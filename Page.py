from bs4 import BeautifulSoup
import time


class Page:
    product_tag = '.prod_main_info'
    thumbnail_img_tag = '.thumb_image img'
    name_tag = 'p.prod_name a'
    spec_tag = '.prod_spec_set .spec_list a'
    price_tag = '.prod_pricelist p.price_sect strong'

    def __init__(self, cate_list, browser):
        self.cate_list = cate_list
        self.browser = browser

    def page_crawler(self):
        for url in self.cate_list:

            self.browser.get(url["url"])
            self.browser.find_element_by_css_selector(self.name_tag)
            soup = BeautifulSoup(self.browser.page_source, 'lxml')

            page_count = 1

            while not self.__is_last_page(soup.select(self.product_tag)):
                self.next_page(page_count)

                soup = BeautifulSoup(self.browser.page_source, 'lxml')

                # 데이터 긁기
                for product in soup.select(self.product_tag):
                    print(product.select(self.thumbnail_img_tag)[0].get('src'))
                    print(product.select(self.name_tag)[0].text.strip().replace('\u2013', ''))
                    print(self.get_product_spec_info(product))
                    print(product.select(self.price_tag)[0].text.strip().replace('\u2013', ''))

                time.sleep(1)

                page_count += 1

    def next_page(self, pagination):
        self.browser.execute_script('movePage(' + str(pagination) + ')')

    def get_product_spec_info(self, product):
        spec = ''
        for i in product.select(self.spec_tag):
            spec += i.text.replace('\u2022', '').replace('\ufffd', '') + '/'
        return spec

    @staticmethod
    def __is_last_page(product):
        if len(product) < 1:
            return True
        return False