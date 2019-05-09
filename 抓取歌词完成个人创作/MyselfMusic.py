# encoding: utf-8
'''
@author: fengding
@email: 924070845@qq.com
@software: PyCharm
@file: MyselfMusic.py
@time: 2018/8/22 10:24
@desc:
'''

import requests
import  jieba
import re
from xpinyin import Pinyin

p = Pinyin()

RhymeIndex = [('1', ['a', 'ia', 'ua']),
              ('2', ['ai', 'uai']),
              ('3', ['an','ian','uan']),
              ('4', ['ang','iang','uang']),
              ('5', ['ao','iao']),
              ('6', ['e','o','uo']),
              ('7', ['ei','ui']),
              ('8', ['en','in','un']),
              ('9', ['eng','ing','ong','iong']),
              ('10', ['er']),
              ('11', ['i']),
              ('12', ['ie','ye']),
              ('13', ['ou,''iu']),
              ('14', ['u']),
              ('15', ['qu','xu','yu']),
              ('16', ['ue'])
              ]

RhymeDct = {
    'a':'1',
    'ia':'1',
    'ua':'1',
    'ai':'2',
    'uai':'2',
    'an':'3',
    'ian':'3',
    'uan':'3',
    'ang':'4',
    'iang':'4',
    'uang':'4',
    'ao':'5',
    'iao':'5',
    'e':'6',
    'o':'6',
    'uo':'6',
    'ei':'7',
    'ui':'7',
    'en':'8',
    'in':'8',
    'un':'8',
    'eng':'9',
    'ing':'9',
    'ong':'9',
    'iong':'9',
    'er':'10',
    'i':'11',
    'ie':'12',
    'ye':'12',
    'ou':'13',
    'iu':'13',
    'u':'14',
    'qu':'15',
    'xu':'15',
    'yu':'15',
    'ue':'16',

}

def _analysis_words(words):
    word_py = p.get_pinyin((u'{}'.format(words)))
    lst_words = word_py.split('-')
    r = []
    for i in lst_words:
        while True:
            if not i:
                break
            token = RhymeDct.get(1, None)
            if token:
                r.append(token)
                break
            i = i[1:]
    if len(r) == len(words):
        return '-'.join(r)


def Getkeyword():
    tracks = ["431795900", '33850315', '430053482']
    with open('keyword.txt', 'a') as f:
        f.write("[")
        for i in tracks:
            print(111)

            lrcurl = "http://music.163.com/api/song/lyric?os-pc&id"+str(i)+"&lv=-1&tv=-1"
            lrcurl = requests.get(lrcurl)
            dt = lrcurl.json()
            lrc = re.sub(u'\\[.*?]]', '', dt['lrc']['lyric'])

            seg_list = list(jieba.cut(lrc, cut_all=True))
            for i in seg_list:
                if len(i) == 2:
                    if _analysis_words(i) != None:
                        f.write("{'"+_analysis_words(i)+"':'"+i+"'},")
        f.write("]")
        f.close()




def Findkey():
    result = {}
    with open('keyword.txt', 'r') as f:
        list = eval(f.readlines()[0])
        for item in list:
            if item.get(str):
                key = item.get(str)
                number = result.get(key)
                if number != None and number>=1:
                    result[key] = number+1
                else:
                    result.update({key:1})
        f.close()
            # print(result)

key = input("请输入关键词：")
str = _analysis_words(key)
print("匹配押韵词：")
Findkey(str)