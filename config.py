# coding=utf-8

import time
import datetime

cookie = ''

# 预约叫车时间 （今天 21:10:36）
BookTime = '%Y-%m-%d 21:10:36'

now = datetime.datetime.now()
a = now.strftime(BookTime)
timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
curr_time = int(time.mktime(timeArray))
#curr_ime = str(int(time.time()))  即时叫车

# 上车位置
StartAddr = '天安门'

# 下车位置
EndAddr = '北京站'

# 上车位置经度
StartPointLo = ''

# 上车位置维度
StartPointLa = ''

# 下车位置经度
EndPointLo = ''

# 下车位置维度
EndPointLa = ''
