import random
import time

from selenium import webdriver
from lxml import etree

# 无头浏览器
# from conn_object.conn_db import Conn

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)


def get_page(url):
    browser.get(url)
    time_out = random.randint(1, 3)
    time.sleep(time_out)
    page_source = browser.page_source
    return page_source


def parse_page(page_source):
    etree_html = etree.HTML(page_source)
    info = {}
    title = etree_html.xpath('normalize-space(//div[@class="sku-name"]/text())')
    price = etree_html.xpath('normalize-space(//div[@class="summary-price-wrap"]//span[2]/text())')
    percent_con = etree_html.xpath('normalize-space(//div[@class="percent-con"]/text())')
    info['title'] = title
    info['price'] = price
    info['percent_con'] = percent_con
    return info


def main():
    url = input(">>>")
    html = get_page(url)
    info = parse_page(html)
    info_print = f"商品名称：{info['title']} \n商品价格：￥{info['price']} \n商品好评率：{info['percent_con']}%"
    print(info_print)


if __name__ == '__main__':
    main()