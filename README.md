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

仓库中预置了 chromedriver88 但愿你能用上. 下载的官方网站是 (https://chromedriver.chromium.org/downloads).

可以通过注释 `chrome_options.add_argument("--headless")` 来获得有头(有GUI)的网页。