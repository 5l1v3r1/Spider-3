from WindPy import w
import datetime

w.start()

# data=w.torder("6000123.SH","buy",9.8,100)
#股票当天收盘价 -  对应合约的收盘 wsd取日数据 基差

  #
# 合约
start_time='2018-02-14' #开始时间

end_time='2018-03-05'#结束时间
tdays=w.tdays(start_time,end_time)
husheng300=['000300','IF']
zhongzheng500=['000905','IC']
shangzheng50=['000016','IH']




def wsd(name,method,start,end):
    Share_close = w.wsd(name,method , start, end, "TradingCalendar=SZSE;PriceAdj=F")
    return  Share_close.Data[0]
def calculate(name):
    Share_code=name[0]
    agreement=name[1]
    Share_close=w.wsd("{}.SH".format(Share_code), "close",start_time , end_time, "TradingCalendar=SZSE;PriceAdj=F") #股票的价格
    Contract_closing_price=w.wsd("IF00.CFE", "settle", start_time, end_time, "TradingCalendar=SZSE;PriceAdj=F") #对应合约的收盘价格
    Contract_volume=w.wsd("IF00.CFE", "volume", start_time, end_time, "TradingCalendar=SZSE;PriceAdj=F")
    daylist=[]
    for i in tdays.Data[0]: #创建一个新的列表将时间格式转换下 转换为正常的日期
        # print(i.strftime("%Y-%m-%d"))
        daylist.append(i.strftime("%Y-%m-%d"))

    Share_close=Share_close.Data[0]
    Contract_closing_price=Contract_closing_price.Data[0]
    Contract_volume=Contract_volume.Data[0]
    for ever_day,ever_day_Share,ever_day_Contract_closing_price,ever_day_Contract_volume in  zip(daylist,Share_close,Contract_closing_price,Contract_volume):
        print(ever_day_Contract_closing_price- float(ever_day_Share))

def mymain():
    calculate(husheng300)

if __name__ == '__main__':
    mymain()