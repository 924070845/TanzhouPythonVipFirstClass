# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: Baidibudejie.py
@time: 2018/8/3 14:15
@desc:
'''
import requests
import re

def getUrlList(url):
    resp = requests.get(url)
    # response.headers('')

    # resp.encoding('utf-8')
    html = resp.text
    print(html)
    reg = r'''
    <div class="j-r-list-c-img">
        
         <a href=".*?">
            <img src=".*?"
                 class="lazy"
                 data-original="(.*?)" title=".*?" alt=".*?"/>
       </a> 
        
    </div>
    '''
    picture = re.findall(reg, html, re.S)
    print(picture)

    # return picture



if __name__ == '__main__':
    url = "http://www.budejie.com/pic/"
    getUrlList(url)