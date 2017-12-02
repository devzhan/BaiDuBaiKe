# coding:utf-8
import requests
 # 下载页面
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        User_Agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        headers={'User-Agent':User_Agent}
        r=requests.get(url,headers=headers)
        if r.status_code==200:
            r.encoding='utf-8'
            return r.text
        return None
