# 日期计算器
# 根据日期构造出 datetime 类型的变量
# 把两个变量进行相减即为所求

# 法一
import datetime

date1 = datetime.datetime(2005, 8, 28)  # 两个datetime先是模块名，后是里面具体的类型
date2 = datetime.datetime(2023, 9, 20)
print(date2 - date1)


# 法二
from datetime import  datetime # 从 datetime 模块 import datetime

date1 = datetime(2005, 8, 28)
date2 = datetime(2023, 9, 20)
print(date2 - date1)


# 法三
import datetime as dt

date1 = dt.datetime(2005, 8, 28)
date2 = dt.datetime(2023, 9, 20)
print(date2 - date1)
