#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import traceback,time,math
LOGFILE="elec.log"
LOGLEVEL=("DEBUG","INFO","WARNING","ERROR","FATAL")
def log(msg,l=1,end="\n",logfile=LOGFILE):
    st=traceback.extract_stack()[-2]
    lstr=LOGLEVEL[l]
    now_str="%s %03d"%(time.strftime("%y/%m/%d %H:%M:%S",time.localtime()),math.modf(time.time())[0]*1000)
    if l<3:
        tempstr="%s [%s,%s:%d] %s%s"%(now_str,lstr,st.name,st.lineno,str(msg),end)
    else:
        tempstr="%s [%s,%s:%d] %s:\n%s%s"%(now_str,lstr,st.name,st.lineno,str(msg),traceback.format_exc(limit=3),end)
    print(tempstr,end="")
    if l>=1:
        with open(logfile,"a") as f:
            f.write(tempstr)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random,sys,json

SLEEP_LOW=0.5
SLEEP_HIGH=1.5

def get_elec(username,password,chrome_version):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    #https://stackoverflow.com/questions/64992087/webdriverexception-unknown-error-devtoolsactiveport-file-doesnt-exist-while-t
    chrome_options.add_argument('--remote-debugging-port=9222')
    if isinstance(chrome_version,int):
        driver=webdriver.Chrome(executable_path="./chromedriver%s"%(chrome_version),options=chrome_options)
    elif isinstance(chrome_version,str):
        driver=webdriver.Chrome(executable_path=chrome_version,options=chrome_options)
    else:
        driver=webdriver.Chrome(options=chrome_options)
    driver.get("http://myhome.tsinghua.edu.cn/")

    time.sleep(random.uniform(SLEEP_LOW,SLEEP_HIGH))
    user_name=driver.find_element_by_id("net_Default_LoginCtrl1_txtUserName")
    user_name.send_keys(username)
    log("filled in UserName")

    time.sleep(random.uniform(SLEEP_LOW,SLEEP_HIGH))
    user_pwd=driver.find_element_by_id("net_Default_LoginCtrl1_txtUserPwd")
    user_pwd.send_keys(password)
    log("filled in UserPwd")

    #竟然有一个“你对家园网满不满意”藏在下面每次登陆都有一个非常满意，去偷袭，去骗，我这样一个不会往下翻的只想交电费的人
    time.sleep(random.uniform(SLEEP_LOW,SLEEP_HIGH))
    vote=driver.find_element_by_id("Home_Vote_InfoCtrl1_Repeater1_ctl01_rdolstSelect_4")
    vote.click()

    time.sleep(random.uniform(SLEEP_LOW,SLEEP_HIGH))
    btn_login=driver.find_element_by_id("net_Default_LoginCtrl1_lbtnLogin")
    btn_login.click()
    log("logged in")

    time.sleep(random.uniform(SLEEP_LOW,SLEEP_HIGH))
    driver.get("http://myhome.tsinghua.edu.cn/Netweb_List/Netweb_Home_electricity_Detail.aspx")
    log("opened electricity page")

    elec_detail=driver.find_element_by_id("Netweb_Home_electricity_DetailCtrl1_lblele")
    log("electricity remain: %s"%(elec_detail.text))
    elec_time=driver.find_element_by_id("Netweb_Home_electricity_DetailCtrl1_lbltime")
    log("%d, %s, %s"%(time.time(),elec_detail.text,elec_time.text),logfile="elec_remain.log")
    with open("elec_remain.html","w") as f:
        f.write("%s"%(elec_detail.text))

if __name__ == '__main__':
    try:
        with open("config.json","r") as f:
            config=json.load(f)
        username=config["username"]
        password=config["password"]
        chrome_version=config["chrome_version"]
    except:
        log("load config.json failed. copy config.example.json to config.json then modify username and password",l=3)
        sys.exit(1)

    try:
        get_elec(username,password,chrome_version)
    except:
        log("unknown error in get_elec",l=3)
