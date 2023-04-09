# coding=utf-8
# import pandas_datareader

# import pandas
from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()

code = 'IBM'
stock = pdr.get_data_yahoo(code, '2019-01-01', '2019-01-20')
print(stock)    # 输出内容
# 保存为excel和csv文档
stock.to_excel('D:\\EvanPro\\PyStu\\S05\\data\\1\\'+code+'.xlsx')
stock.to_csv('D:\\EvanPro\\PyStu\\S05\\data\\1\\'+code+'.csv')
