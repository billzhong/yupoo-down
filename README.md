# Yupoo Downloader 又拍网相册下载器


## Requirements
- Python 3
- Requests
- pyqt5
  - ```pip install -r requirements.txt```

## Usage 用法
- 找到 sid
  - 正常登录 [又拍网](http://www.yupoo.com/account/login/) 回到主页
  - 打开 `开发者工具` 或 `网页检查器` ，在 `Application` 或 `储存空间` 里找到 `Cookie` 里面的 `sid` 值并记下来。
    - 或者，右键 `显示网页源代码` ，搜索 `sid:` 记下后面引号内的值。
- 填入 sid
  - 把上一步获取的 `sid` 值填入代码内 `SID =` 引号里面。
    - 类似 `SID = '123defghijklmnopqrstuvw456'` 这样。
  
- 点击软件页面的输入SID，
- 点击生成aria2文件
- 配置aria2的文件
- 点击使用aria2下载

## Bugs
- 容易卡死，特别是第一次登陆的时候，多试几次就可以了
- 其他未知bugs

## 下载
- 页面右边偏上的地方有个 “Clone or download”按钮，适合动手能力比较强的同学


- [版本发布](https://github.com/xinyu3ru/yupoo-down/releases)，在这个页面下载打包的exe文件（64位系统测试，32位系统未测试）


- Linux的同学自己折腾吧
