# coding : utf-8
from bs4 import BeautifulSoup
import urllib.parse as UP
import re
# 分析下载下来的页面
class HtmlParser(object):
    def parser(self,page_url,html_cont):
        '''

        :param page_url: 下载页面的url
        :param html_cont: 下载页面的内容
        :return:
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

        pass

    def _get_new_urls(self,page_url,soup):
        new_urls=set()
        # 正则表达可能会需要根据百度百科的更新对应修改
        links = soup.find_all('a',href=re.compile(r'/item/*?'))
        print(links)
        for link in links:
            new_url= link['href']
            new_full_url =UP.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        data={}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title']=title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        data['summary']=summary.get_text()
        return data
