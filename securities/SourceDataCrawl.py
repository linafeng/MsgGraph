# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd

soup = BeautifulSoup(open('data/000001.html'), "html.parser")
soup.prettify().encode('gbk', 'ignore').decode('gbk')
code = soup.select_one('body > div.wrapper > div.header > div.bd.clear > div.code.fl > h1 > a')
code = code.text.strip()[len(code.text.strip()) - 6:]


def test1(tr3):
    title = tr3.select_one('.person_table .title a').text
    jobs = tr3.select_one('.person_table .jobs').text
    temp = tr3.select_one('.person_table .intro')
    sex = temp.text[0:1]
    age = temp.text[3:5]
    # print('姓名，性别，年龄，股票代码,职位')
    # print(title, sex, age, code, jobs)
    yield {
        'title': title,
        'sex': sex,
        'age': age,
        'code': code,
        'jobs': jobs,
    }


items = soup.select('#ml_001 > table > tbody > tr> td[class*=tc]')
# with open('dumpjson.txt', 'w') as f:
#     for tr in items:
#         data = test1(tr)
#         # print(next(data))
#         person = next(data)
#         print(type(person))
#         print(person)
#         json.dump(person, f)
#         f.write("\n")

####写入Csv文件中
with open("executive_prep.csv", 'w') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        #设置标题
        # spamwriter.writerow(["游戏账号","用户类型","游戏名称","渠道","充值类型","充值金额","返利金额","单号","日期"])
        #将CsvData中的数据循环写入到CsvFileName文件中
        for tr in items:
            data = test1(tr)
            # print(next(data))
            person = next(data)
            print(type(person))
            print(person)
            # spamwriter.writerow(person)
            fieldnames = ['title', 'sex', 'age', 'code', 'jobs']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(person)



