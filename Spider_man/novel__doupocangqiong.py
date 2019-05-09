# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: novel__doupocangqiong.py
@time: 2018/8/1 11:22
@desc:
'''
# 导入模块
import requests
import re

def get_chapter_data(data_url):
    # 模拟浏览器发送get请求
    response = requests.get(data_url)
    #显示的制定编码字符
    response.encoding = 'utf-8'
    #获取文本模式
    html = response.text
    #提取我们需要的数据
    #第一个参数是我们的正则，第二个参数的是涛提取的对象
    #第三个参数是固定的，没坐解释
    #返回值是一个列表，所以要取出列表的第一个值[0]
    chapter_data = re.findall(r'id="htmlContent">(.*?)class="text-center pt10">', html, re.S)[0]

    #清洗数据
    #第一步去除两端空格

    chapter_data = chapter_data.strip()
    #然后在取到其他的干扰字符，全局替换
    chapter_data = chapter_data.replace("<br>", '')
    chapter_data = chapter_data.replace("</div>", '')
    chapter_data = chapter_data.replace("<p", '')
    chapter_data = chapter_data.replace("</p>", '')
    chapter_data = chapter_data.replace(">", '')
    chapter_data = chapter_data.replace("<br", '')
    chapter_data = chapter_data.replace("/<br", '')
    chapter_data = chapter_data.replace("/", '')

    return (chapter_data)

def get_chapter_title(title_url):
    response = requests.get(title_url)
    response.encoding = "utf-8"
    html = response.text
    # print(html)
    chapter_title = re.findall(r'<dd class="col-md-3">.*?<a href="(.*?)">(.*?)<', html, re.S)
    # chapter_title = chapter_title.replace("《斗破苍穹》首次曝光的主人物形象</a>  </dd>  ", '')
    print(chapter_title)



    return chapter_title


if __name__ == '__main__':
    # chapter_data_url = "http://www.jingcaiyuedu.com/book/7504/20.html#"
    chapter_title_url = "http://www.jingcaiyuedu.com/book/7504.html"
    # chapter_data = get_chapter_data(chapter_data_url)
    chapter_title = get_chapter_title(chapter_title_url)
    #打开文件，没有文件时创建一个出来
    # fbb = open("斗破苍穹", 'w', encoding='utf-8')
    for chapter in chapter_title:
        if chapter[1] == "第五十章 帮?":
            pass
        else:
            fbb = open("斗破苍穹/{}.doc".format(chapter[1]), 'w', encoding='utf-8')
            # 写入文件
            chapter_data = get_chapter_data("http://www.jingcaiyuedu.com%s" % chapter[0])
            fbb.write('\n')
            fbb.write(chapter[1])
            fbb.write('\n')
            fbb.write(chapter_data)
            fbb.write('\n')
            print(chapter[1])
            fbb.close()






    # print(chapter_data)
    print(chapter_title)