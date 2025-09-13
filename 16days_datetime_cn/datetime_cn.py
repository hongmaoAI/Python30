# Python有一个 datetime 模块用于处理日期和时间

# 获取datetime信息
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)  # 2025-09-13 17:49:23.243140
year = now.year  # 2025
month = now.month  # 9
day = now.day  # 13
hour = now.hour  # 17
minute = now.minute  # 54
second = now.second  # 23
timestamp = now.timestamp()  # 53

print(second)
print(f'{year}/{month}/{day},{hour}:{minute}:{second}')  # 2025/9/13,19:1:58

# 使用 strftime 方法格式化日期时间
t = now.strftime("%H:%M:%S")
print('时间：', t)  # 19:05:33
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# 时间以 mm/dd/YY H:M:S 格式输出
print('时间一：', time_one)
time_two = now.strftime("%d/%m/%Y,%H:%M:%S")
print('时间二：', time_two)
# 使用 strptime 将字符串转换为时间
date_string = '13 September,2025'
print('data_string:', date_string)  # data_string: 13 September,2025
date_object = datetime.strptime(date_string, '%d %B,%Y')
print('date_object:', date_object)  # date_object: 2025-09-13 00:00:00

# 计算两个时间点之间的差异
today = now.today()
today_year = today.year
today_month = today.month
today_day = today.day
today_hour = today.hour
today_minute = today.minute
today_second = today.second
today_now = date(year=today_year, month=today_month, day=today_day)
new_year = date(year=2026,
                month=2,
                day=16)
diff = new_year - today_now
print(diff)  # 156

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)  # t3 = 86 days, 22:56:50
