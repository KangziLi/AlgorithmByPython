# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 16:42:21 2017

@author: KangziLi
@source: lintcode - 376. Binary Tree Path Sum
"""
import requests
import re,json
import pandas


class base():
    def __init__(self,url):
        self.url = url

    def all_url(self):
        return [self.url + "%s" % i for i in range(1,100)]

    def loads_jsonp(self,_jsonp):
        try:
            return json.loads(re.match(".*?({.*}).*",_jsonp,re.S).group(1))
        except:
            raise ValueError('Invalid Input')

    def url_req(self,url):
        content = requests.get(url).text
        aa = self.loads_jsonp(content)
        return aa

    def taobao_comment(self,data):
        for i in data['comments']:
            data = {}
            data['昵称']=i['user']['nick']
            data['评论']=i['content']
            info_list.append(data)

    def tianmao_comment(self,data):
        for i in data['rateList']:
            data = {}
            data['昵称']=i['displayUserNick']
            data['评论']=i['rateContent']
            info_list.append(data)

    def comment(self,url):
        data = self.url_req(url)
        self.tianmao_comment(data) if 'tmall' in url else self.taobao_comment(data)
            

def main(url):
    data = base(url)
    for i in data.all_url():
        data.comment(i)
        print(len(info_list))


if __name__ == "__main__":
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=39258348512&spuId=250685252&sellerId=2106913388&order=3&currentPage='
    info_list = []
    main(url)
    df =pandas.DataFrame(info_list)
    df.to_excel('comments.xlsx',index=False)