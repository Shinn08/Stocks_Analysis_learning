
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import akshare as akshare
import mplfinance as mplfinance
from matplotlib.pyplot import ylabel

# list_a = np.array([1,2,3,4,5])
# plt.plot(list_a)

Stock_A = akshare.stock_zh_a_hist(symbol = '002085',period='daily',start_date='20250201',end_date='20250909')


#通过mplfinance绘制K线图
#将akshare的数据类型转换为mplfinance支持的数据类型
Stock_A_reserve = Stock_A[['日期','开盘','最高','最低','收盘','成交量']]
Stock_A_reserve_date = Stock_A_reserve.copy()
Stock_A_reserve_date['日期'] = pd.to_datetime(Stock_A_reserve_date['日期'])
Stock_A_reserve_new = Stock_A_reserve_date.rename(columns={
    '日期':'Date',
    '开盘':'Open',
    '最高':'High',
    '最低':'Low',
    '收盘':'Close',
    '成交量':'Volume'
    })
Stock_A_reserve_index = Stock_A_reserve_new.set_index('Date')
print(Stock_A_reserve_index)

#设计新的K线颜色图，继承YAHOO风格
my_color = mplfinance.make_marketcolors(
    up ='#fe3032',
    down = '#00b060',
    edge = 'inherit',
    wick = 'inherit',
    volume ={'up':'#fd6b6c','down':'#4dc790'}

)

my_mplfinance_style = mplfinance.make_mpf_style(
    base_mpf_style = 'yahoo',
    marketcolors = my_color
)

mplfinance.plot(Stock_A_reserve_index.tail(30),type = 'candle',style = my_mplfinance_style,mav=(5,10,20),ylabel_lower = 'Quant', volume = True)
# mplfinance.plot(Stock_A_reserve_index.tail(30),type = 'candle',style = 'yahoo',mav=(5,10,20),volume = True)