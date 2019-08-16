# -*- coding: utf-8 -*-
import tushare as ts

df = ts.get_industry_classified()
# // TODO 保存成"stock_industry_prep.csv"
print(df)
# 直接保存
# df.to_csv('data_analysis/stock_industry_prep.csv', encoding='utf_8_sig')  #, encoding='utf_8_sig'
df.to_csv('data_analysis/stock_industry_prep.csv', columns=['code', 'name', 'c_name'], encoding='gbk')
# 类似的，可以通过以下的代码即可以获得股票概念信息，并把它们存储在 “stock_concept_prep.csv”文件里。
df = ts.get_concept_classified()
# //  TODO 保存成“stock_concept_prep.csv”
# 直接保存
df.to_csv('data_analysis/stock_concept_prep.csv', columns=['code', 'name', 'c_name'], encoding='gbk')
