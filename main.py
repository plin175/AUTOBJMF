import os
import json
import re
import datetime
import requests
from bs4 import BeautifulSoup
import time
import schedule


with open('data.json', 'r') as f:
    data = json.load(f)
    current_directory = os.getcwd()
    classID = data['classID']
    x = data['x']
    y = data['y']
    h = data['h']
    mycookie = data['cookie']
    searchtime = data['time']
    sendkey = data['sendkey']
    
    pattern = r'remember_student_59ba36addc2b2f9401580f014c7f58ea4e30989d=[^;]+'
    search = re.search(pattern, mycookie)
    if search:
        result = search.group(0)
        # print('your cookie: ', result)
    else:
        print('not find your cookie, check it again')
    
    if data['settime'] == "":
        settime = input('please input time: ')
    else:
        settime = data['settime']
        
    print("------------get-information---------------")
    print("班级ID号 : ", classID)
    print("经度(x) : ", x)
    print("纬度(y) : ", y)
    print("海拔(h) : ", h)
    print("cookie :", mycookie)
    print("搜索间隔(time) : ", searchtime)
    print("设定时间(settime) : ", settime)
    print("微信公众号Server酱的SendKey : ", sendkey)
    print("------------------------------------------")
    

# 微信公众号Server酱   获取sendkey：https://sct.ftqq.com/
def send_message(sendkey, message):
    url = 'https://sctapi.ftqq.com/' + sendkey + '.send'
    data = {'title': '班级魔法自动签到任务', 'desp': message}
    response = requests.post(url, json=data)
    return response.text
    
def link_to_BJMF():
    print('现在时间 : ', datetime.now())
    title = '班级魔法自动签到任务'
    url = 'http://k8n.cn/student/course/' + classID + '/punchs'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; AKT-AK47 Build/USER-AK47; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160065 MMWEBSDK/20231202 MMWEBID/1136 MicroMessenger/8.0.47.2560(0x28002F35) WeChat/arm64 Weixin NetType/4G Language/zh_CN ABI/arm64',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/wxpic,image/tpg,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'X-Requested-With': 'com.tencent.mm',
        'Referer': 'http://k8n.cn/student/course/' + classID,
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh-SG;q=0.9,zh;q=0.8,en-SG;q=0.7,en-US;q=0.6,en;q=0.5',
        'Cookie': result
    }

    while True:
        response = requests.get(url, headers)
        print('响应 : ',response)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        pattern = re.compile(r'punch_gps\((\d+)\)')
        matches = pattern.findall(response.text)
        print("找到GPS定位签到 : ", matches)
        
        # send message
        message = f'签到响应: {response.text}'
        result = send_message('SendKey ', message)
        print('result: ', result)
            
        time.sleep(searchtime)
        
if(settime != ''):
    print('waiting...')
    schedule.every().day.at(settime).do(link_to_BJMF)

    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    link_to_BJMF()
                
