import requests  # 导入请求包
import time # 导入定时器包
from lxml import etree
# import sql_insert
# coding=UTF-8
input = input("请输入歌曲")
# 音乐下载地址
wang_url = 'https://music.163.com/song/media/outer/url?id=星辰大海'
# QQ_url = 'https://link.hhtjim.com/qq/002LNOds0rYvpK.m4a'
src = 'C:/Users/雅九老色批/Desktop/789'
# 目标网页
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.top&searchid=60946389168626903&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w='+input+'&_=1627135502555&cv=4747474&ct=24&format=json&inCharset=utf-8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&uin=0&g_tk_new_20200303=5381&g_tk=5381&hostUin=0&loginUin=0'
head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
}
url2='https://y.qq.com/n/ryqq/search?w=%E6%88%91%E4%BB%AC%E7%9A%84%E6%AD%8C&t=song&remoteplace=txt.yqq.top'
# 转换成json格式
response = requests.get(wang_url, headers=head)
data = response.json()
print(data)
# 保存json数据格式 用于分析
# with open('data.json',mode='w',encoding='utf-8') as filt:
#     filt.write(response.text)
# 设置定时器
# def sleeptime(hour, min, sec):
#     return hour * 3600 + min * 60 + sec
# star = sleeptime(0,0,0)
# 获取歌曲列表
# song_list = data["data"]["song"]["list"]
# song_list_len = len(song_list) #获取列表长度
# for song in song_list:
#     mid = song["mid"] # 获取歌曲id
#     name = song["name"] # 获取歌曲名字
#     singer = song["singer"][0]["name"] #获取歌手
#     print(mid,name,singer)
#     new_url = 'https://link.hhtjim.com/qq/'+mid+'.m4a'
#     music = requests.get(new_url,headers=head).content
#     print(type(music))
#     print(bytes.decode(music))
#     # with open(src+'\\'+name+mid+'.m4a','wb') as file:
#     #     i += 1
#     #     print(i)
#     #     file.write(music)
#     print("保存成功")
#     time.sleep(star) #执行定时器
# sql_insert.mysql_insertsong(song_list);
    # print(singer)
# print(song_list_len)
# html_str = etree.HTML(response.text)
# print(html_str)

