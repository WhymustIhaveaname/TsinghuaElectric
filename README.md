# 清华电费余额

爬取清华家园网 (http://myhome.tsinghua.edu.cn/) 获得电量余额。

### 使用方法

复制 `config.example.json` 至 `config.json` 并更改相关配置后即可 `python3 elec.py`.

其中 `chrome_version` 字段有些迷惑, 它可以是:
* 字符串, 表示 chromedriver 的路径
* 数字, 表示 chromedriver 是 "chromedriverxx"
* null, 表示 chromedriver 在 PATH 中
相关代码是
```
if isinstance(chrome_version,int):
    driver=webdriver.Chrome(executable_path="./chromedriver%s"%(chrome_version),options=chrome_options)
elif isinstance(chrome_version,str):
    driver=webdriver.Chrome(executable_path=chrome_version,options=chrome_options)
else:
    driver=webdriver.Chrome(options=chrome_options)
```

release 里有 chromedriver 89 和 87 但愿你能用上. 下载的官方网站是 (https://chromedriver.chromium.org/downloads).

可以通过注释 `chrome_options.add_argument("--headless")` 来获得有头(有GUI)的网页.

### 定时执行

Linux 下可以使用 crontab 定时执行脚本: [使用crontab重复执行脚本](https://github.com/WhymustIhaveaname/TsinghuaTunet#%E4%BD%BF%E7%94%A8crontab%E9%87%8D%E5%A4%8D%E6%89%A7%E8%A1%8C%E8%84%9A%E6%9C%AC).
Windows 和 MacOS 一定有类似工具.
