# Yupoo Downloader 又拍网相册下载器

## Requirements
- Python 3
- Requests
  - ```pip install -r requirements.txt```

## Usage 用法
- 找到 sid
  - 正常登录 [又拍网](http://www.yupoo.com/account/login/) 回到主页
  - 打开 `开发者工具` 或 `网页检查器` ，在 `Application` 或 `储存空间` 里找到 `Cookie` 里面的 `sid` 值并记下来。
    - 或者，右键 `显示网页源代码` ，搜索 `sid:` 记下后面引号内的值。
- 填入 sid
  - 把上一步获取的 `sid` 值填入代码内 `SID =` 引号里面。
    - 类似 `SID = '123defghijklmnopqrstuvw456'` 这样。
- 生成下载列表
  - 运行 ```python yupoo.py > urls.txt```
    - 根据照片的数量，可能需要等一会儿。
- 使用 `aria2` 下载
  - 运行 ```aria2c -iurls.txt```
  - 其他可选参数 `--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.1 Safari/605.1.15" --header "Referer: http://www.yupoo.com/"`
  
### TODO
- 在 Windows 下测试
- 完善文档
- 相册选择性下载
- 内置输出而不是使用输出重定向
- 支持生成非 `aria2` 格式的列表
