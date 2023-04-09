import tushare as ts


def saveStockByTS(code):    # 定义获取并保存指定股票交易数据的方法
    start = '2019-01-01'
    end = '2019-01-31'
    ts.set_token('05699d68a4c3b2b514c2752c8b5e980999f6de0fa3c12611c368e4d0')
    ts.pro_bar(ts_code=code,
               asset='I',
               start_date=start, end_date=end).to_csv(
        'D:\\EvanPro\\PyStu\\S05\\data\\1\\'+code+'.csv',
        columns=['open', 'high', 'close', 'low', 'volume'])


# 开始调用
code = '600895.SH'       # 股票“张江高科”
saveStockByTS(code)
# 也可以去掉下面的注释，在获取股票代码的同时获取该股票的信息
# stockList=ts.get_stock_basics()
# for code in stockList.index:
# saveStockByTS(code)
