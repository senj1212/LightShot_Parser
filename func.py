import requests
import random, pygame
from bs4 import BeautifulSoup as bs
import time

headers = {
'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36'
}

class Img():
    def go_to_url(self, proxies):
        url_two = ''
        url_one = "https://prnt.sc/"
        for i in range(0, 6):
            url_two += random.choice('1234567890qwertyuiopasdfghjklzxcvbnmMNBVCXZLKJHGFDSAOPIUYTREWQ')
        url_last = url_one + url_two
        page_r = requests.get(url_last, headers = headers)
        return page_r.text, url_two
    def download_and_save(self, page, url_two):
        # скачивание картинки
        img_page = requests.get(page)
        name = 'img/img_{0}.png'.format(url_two)
        if not '<!--[if lt IE 7]> <html class="no-js ie6 oldie" lang="en-US"> <![endif]-->' in img_page.text:
            img = open(name, 'wb')
            img.write(img_page.content)
            img.close()
            time.sleep(2)
    def find_img(self, page_r):
        content = bs(page_r, 'lxml')
        try:
            url_img = content.find('img', class_='no-click screenshot-image').get('src')
            if 'https:' in url_img:
                return url_img
            else:
                return None
        except:
            return None
