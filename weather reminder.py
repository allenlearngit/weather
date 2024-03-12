## 發送請求到url 參數

# import requests as req
#
# ## 傳入參數要用字典 並用字串格式
# params ={
#     "Authorization":"CWA-BE008C4E-DC34-4ABB-BDAE-FE897CB1AB90",
#     "locationName":"新北市",
#     "elementName":"PoP"
# }
# res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
# print(res.text)


## 測驗一
# import requests as req
# import pandas as pd
# ## 傳入參數要用字典 並用字串格式
# params ={
#     "Authorization":"CWA-BE008C4E-DC34-4ABB-BDAE-FE897CB1AB90",
#     "locationName":"新北市",
#     "elementName":"PoP"
# }
# res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
# df = (res.json()["records"]["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"])
# print(df)



## 發送email
# import smtplib
# import email.message
# # ruiq uzfm lyrf lbsd
#
# my_email = "appl510@gmail.com"
# password = "ruiq uzfm lyrf lbsd"
#
# msg = email.message.EmailMessage()
# msg["from"] = my_email
# msg["to"] = "appl510@gmail.com"
# msg["Subject"] = "你好"
# msg.set_content("第三封信件")
#
# connection = smtplib.SMTP_SSL("smtp.gmail.com")
# connection.login(my_email, password)
# connection.send_message(msg)
# connection.close()


## 測驗二
#
# import smtplib
# import email.message
# import schedule
# from datetime import datetime
# import time
#
# my_email = "appl510@gmail.com"
# password = "ruiq uzfm lyrf lbsd"
#
# num = 1
# def send_meessage():
#     global num
#     current_datetime = datetime.now()
#     formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
#     msg = email.message.EmailMessage()
#     msg["from"] = my_email
#     msg["to"] = "appl510@gmail.com"
#     msg["Subject"] = f"第{num}封信件" # 標題
#     msg.set_content(formatted_datetime) #內容
#
#     connection = smtplib.SMTP_SSL("smtp.gmail.com")
#     connection.login(my_email, password)
#     connection.send_message(msg)
#     connection.close()
#     print(f"第{num}封信件 {formatted_datetime} 發送成功")
#     num += 1
#
# schedule.every(5).seconds.do(send_meessage)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)



## 自動發信
# import requests as req
# import pandas as pd
# import smtplib
# import email.message
# import schedule
# import time
#
# #帳號資訊
# my_email = "appl510@gmail.com"
# password = "ruiq uzfm lyrf lbsd"
#
# #取得資料
# params ={
#     "Authorization":"CWA-BE008C4E-DC34-4ABB-BDAE-FE897CB1AB90",
#     "locationName":"新北市",
# }
# res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
# Wx = (res.json()["records"]["location"][0]["weatherElement"][0]["time"][0]["parameter"]["parameterName"])
# Pop = float((res.json()["records"]["location"][0]["weatherElement"][1]["time"][0]["parameter"]["parameterName"]))
# MinT = float((res.json()["records"]["location"][0]["weatherElement"][2]["time"][0]["parameter"]["parameterName"]))
# CI = (res.json()["records"]["location"][0]["weatherElement"][3]["time"][0]["parameter"]["parameterName"])
# MaxT = (res.json()["records"]["location"][0]["weatherElement"][4]["time"][0]["parameter"]["parameterName"])
# print(CI)
#
# def chech_weather():
#   if Pop >= 20:
#     if MinT <= 15:
#       return ("開車上班 穿羽絨衣")
#     elif MinT <= 20:
#       return("開車上班 穿長袖+外套")
#     elif MinT <= 25:
#       return("開車上班 穿長袖")
#     else:
#       return("開車上班 穿短袖")
#   else:
#     if MinT <= 15:
#       return("騎機車 穿羽絨衣")
#     elif MinT <= 20:
#       return("騎機車 穿長袖+外套")
#     elif MinT <= 25:
#       return("騎機車 穿長袖")
#     else:
#       return("騎機車 穿短袖")
#
# def send_meessage():
#   msg = email.message.EmailMessage()
#   msg["from"] = my_email
#   msg["to"] = "appl510@gmail.com"
#   msg["Subject"] = "氣象預報" # 標題
#   msg.set_content(chech_weather()) #內容
#
#   connection = smtplib.SMTP_SSL("smtp.gmail.com")
#   connection.login(my_email, password)
#   connection.send_message(msg)
#   connection.close()
#   print(f"Wx {Wx}")
#   print(f"PoP {Pop}")
#   print(f"MinT {MinT}")
#   print(f"CI {CI}")
#   print(f"MaxT {MaxT}")
#   if Pop >=20:
#     if MinT<=15:
#       print("開車上班 穿羽絨衣")
#     elif MinT<=20:
#       print("開車上班 穿長袖+外套")
#     elif MinT<=25:
#       print("開車上班 穿長袖")
#     else:
#       print("開車上班 穿短袖")
#   else:
#       if MinT <= 15:
#         print("騎機車 穿羽絨衣")
#       elif MinT <= 20:
#         print("騎機車 穿長袖+外套")
#       elif MinT <= 25:
#         print("騎機車 穿長袖")
#       else:
#         print("騎機車 穿短袖")
#   print("發送成功")
#
# send_meessage()

## 自動發送天氣預報 老師寫法 手動發
# import requests as req
# import smtplib
# import email.message
# import schedule
# import time
#
# #帳號資訊
# my_email = "appl510@gmail.com"
# password = "ruiq uzfm lyrf lbsd"
#
# def send_email(content):
#   msg = email.message.EmailMessage()
#   msg["from"] = my_email
#   msg["to"] = "appl510@gmail.com"
#   msg["Subject"] = "氣象預報" # 標題
#   msg.set_content(content) #內容
#
#   connection = smtplib.SMTP_SSL("smtp.gmail.com")
#   connection.login(my_email, password)
#   connection.send_message(msg)
#   connection.close()
#   print("發送成功")
#
# #取得資料
# params ={
#     "Authorization":"CWA-BE008C4E-DC34-4ABB-BDAE-FE897CB1AB90",
#     "locationName":"新北市",
# }
# res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
#
#
# weather = {}
# for i in range(0, 5):
#   name = (res.json()["records"]["location"][0]["weatherElement"][i]["elementName"])
#   vaule = (res.json()["records"]["location"][0]["weatherElement"][i]["time"][0]["parameter"]["parameterName"])
#   weather[name] = vaule
#   print(name, vaule)
#
# weather["PoP"] = int(weather["PoP"])
# weather["MinT"] = int(weather["MinT"])
#
#
# if weather["PoP"] >= 20:
#   vehicle = "開車上班"
# else:
#   vehicle = "騎機車"
#
# if weather["MinT"] <= 15:
#   cloth = "穿羽絨衣"
# elif weather["MinT"] <= 20:
#   cloth = "穿長袖+外套"
# elif weather["MinT"] <= 25:
#   cloth = "穿長袖"
# else:
#   cloth = "穿短袖"
#
# text = f"{vehicle} {cloth}"
# print(text)
# send_email(text)


## 自動發送天氣預報 老師寫法 定時發
# import requests as req
# import smtplib
# import email.message
# import schedule
# import time
#
# #帳號資訊
# my_email = "appl510@gmail.com"
# password = "ruiq uzfm lyrf lbsd"
#
# def send_email():
#     content = grt_weather()
#     msg = email.message.EmailMessage()
#     msg["from"] = my_email
#     msg["to"] = "appl510@gmail.com"
#     msg["Subject"] = "氣象預報" # 標題
#     msg.set_content(content) #內容
#
#     connection = smtplib.SMTP_SSL("smtp.gmail.com")
#     connection.login(my_email, password)
#     connection.send_message(msg)
#     connection.close()
#     print("發送成功")
#
# def grt_weather():
#     #取得資料
#     params ={
#         "Authorization":"CWA-BE008C4E-DC34-4ABB-BDAE-FE897CB1AB90",
#         "locationName":"新北市",
#     }
#     res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)
#
#     weather = {}
#     for i in range(0, 5):
#       name = (res.json()["records"]["location"][0]["weatherElement"][i]["elementName"])
#       vaule = (res.json()["records"]["location"][0]["weatherElement"][i]["time"][0]["parameter"]["parameterName"])
#       weather[name] = vaule
#       print(name, vaule)
#
#     weather["PoP"] = int(weather["PoP"])
#     weather["MinT"] = int(weather["MinT"])
#
#     if weather["PoP"] >= 20:
#       vehicle = "開車上班"
#     else:
#       vehicle = "騎機車"
#
#     if weather["MinT"] <= 15:
#       cloth = "穿羽絨衣"
#     elif weather["MinT"] <= 20:
#       cloth = "穿長袖+外套"
#     elif weather["MinT"] <= 25:
#       cloth = "穿長袖"
#     else:
#       cloth = "穿短袖"
#
#     text = f"{vehicle} {cloth}"
#     print(text)
#     return text
#
# schedule.every().day.at("06:00:00").do(send_email)
# # schedule.every(5).seconds.do(send_email)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)




## 天氣預報 使用line發送
#小徐個人
# # OE0PZ2t2HhEpivsICOgIi5RzYDNSCin7x1HRPMU0UR1
#小徐群組
# p9vfJu0JKDS5I6WLZBPmvgieW3pptjQO6A0eWrvoACp

import requests as req
import schedule
import time

def grt_weather():
#取得資料
    params ={
        "Authorization":"CWA-BE008C4E-DC34-4ABB-BDAE-FE897CB1AB90",
        "locationName":"新北市",
    }
    res = req.get("https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001", params=params)

    weather = {}
    for i in range(0, 5):cd
      name = (res.json()["records"]["location"][0]["weatherElement"][i]["elementName"])
      vaule = (res.json()["records"]["location"][0]["weatherElement"][i]["time"][0]["parameter"]["parameterName"])
      weather[name] = vaule
      print(name, vaule)

    weather["PoP"] = int(weather["PoP"])
    weather["MinT"] = int(weather["MinT"])

    if weather["PoP"] >= 50:
      vehicle = "超過50%會下雨喔"
    else:
      vehicle = "高機率不下雨 不帶傘了"

    if weather["MinT"] <= 15:
      cloth = "超冷 一定要厚外套"
    elif weather["MinT"] <= 20:
      cloth = "還行 薄外套即可"
    elif weather["MinT"] <= 25:
      cloth = "不穿外套"
    else:
      cloth = "短袖出發"

    text = f"今日天氣為{weather["CI"]}\n{cloth}\n{vehicle}"
    print(text)
    return text

#line推播
def lineNotify():
    # url = "https://notify-api.line.me/api/notify"
    url = "https://httpbin.org/post"
    token = "p9vfJu0JKDS5I6WLZBPmvgieW3pptjQO6A0eWrvoACp"
    headers = {
      "Authorization":"Bearer " + token #設定權杖
    }
    data ={
      "message": grt_weather()
    }
    r=req.post(url, headers=headers, data=data)

# schedule.every().day.at("06:00:00").do(lineNotify)
schedule.every(5).seconds.do(lineNotify)

while True:
    schedule.run_pending()
    time.sleep(1)






