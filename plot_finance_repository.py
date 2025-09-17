import mplfinance as mplfinance
import pandas as pandas

import pandas as pd
import matplotlib.pyplot as plt


def plot_daily_from_akshare(Stock_from_akshare, my_mplfinance_style):
    '''

    :param Dataframe: 输入的股票数据 Dataframe 格式为Akshare 东方财富token
    :return:Dataframe :处理后的股票数据 Dataframe 符合mplfinance plot的格式
    '''
    #1 选取Dataframe中有效列数据
    Stock_Column_reserve = Stock_from_akshare[['日期', '开盘', '最高', '最低', '收盘', '成交量']]
    Stock_Column_reserve_copy = Stock_Column_reserve.copy()

    #2将日期一列的数据格式转换为Datetime格式
    Stock_Column_reserve_copy['日期'] = pd.to_datetime(Stock_Column_reserve_copy['日期'])

    #3将Dataframe中的列名字修改为mplfinance支持的列名字
    Stock_rename = Stock_Column_reserve_copy.rename(columns={
        '日期': 'Date',
        '开盘': 'Open',
        '最高': 'High',
        '最低': 'Low',
        '收盘': 'Close',
        '成交量': 'Volume'
    })

    #4 将Dataframe中的Date（日期）设置为索引
    Stock_re_index = Stock_rename.set_index('Date')
    return Stock_re_index

def get_my_mplfinance_style:
    my_color = mplfinance.make_marketcolors(
        up='#fe3032',
        down='#00b060',
        edge='inherit',
        wick='inherit',
        volume={'up': '#fd6b6c', 'down': '#4dc790'}

    )

    my_mplfinance_style = mplfinance.make_mpf_style(
        base_mpf_style='yahoo',
        marketcolors=my_color
    )

    return my_mplfinance_style



