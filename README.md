# AUTOBJMF
班级魔方自动签到，虚拟定位

**仅支持GPS签到部分**

### 相关功能
* 自动打卡签到
* 虚拟定位（自定义经纬度、海拔）
* 定时打卡

### data.json
```
{
    "classID" : "",   //班级魔方的班级ID号
    "x" : "",         //经度
    "y" : "",         //纬度
    "h" : "",         //海拔
    "time" : 100,     //发送间隔
    "cookie" : "",
    "settime" : "",   //预设打卡时间
    "sendkey" : ""    //自动打卡消息推送sendkey
}
```

### 获取班级ID和cookie
* **step1** 下载Fiddler
* **step2** 打开微信中的班级魔方，注意要打开到打卡界面里
* **step3** 在Fiddler中找到网址[http://k8n.cn/student/course/]()，这个网址后面跟着的五位数字就是班级ID
* **step4** 在Fiddler中点击这个网址[http://k8n.cn/student/course/‘你的班级ID’/punchs]()，在右侧界面找到Raw选项，点击即可看见cookie

### 获取经纬度和海拔
通过高德地图坐标拾取器获取：https://lbs.amap.com/tools/picker
