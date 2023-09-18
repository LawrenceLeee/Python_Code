# 输入四个小数，求四个小数平均值
# " " "
# a = input('请输入第一个数字：')
# b = input('请输入第二个数字：')
# c = input('请输入第三个数字：')
# d = input('请输入第四个数字：')
# a = int(a)
# b = int(b)
# c = int(c)
# d = int(d)
# avg = (a + b + c + d) / 4
# print(f'平均值是：{avg}')
# " " "

# 输入一个整数，判断是否是奇数
# a = input('请输入一个正整数：')
# a = int (a)

# a = int(input('请输入一个正整数：))

# if a % 2 == 0 :
#     print('偶数')
# else :
#     print('是奇数')
#

# 输入一个整数，判断是正数还是负数
# a = input('请输入一个整数：')
# a = int (a)
# if a > 0 :
#     print('是正数')
# elif a == 0 :
#     print('非正非负')
# else :
#     print('是负数')


# 判断年份是否是闰年
# a = input('请输入要判断的年份：')
# a = int(a)
# if (a % 100 != 0 and a % 4 == 0) or a % 400 == 0 :      #四年一闰且不是整百年&&世纪闰年被四百整除   #前面可用个小短路减少不必要判定
#     print('闰年')
# else :
#     print('平年')

# 下面两个n是5时的特殊情况
# a = 1
# SUM = 1
# while a < 6 :
#     SUM *= a
#     a += 1
# print(f'SUM = {SUM}')

# a = 1
# i = 5
# Mul = 1
# SUM = 0
# while i > 0:
#     a = 1
#     Mul = 1
#     while a <= i:
#             Mul *= a
#             a += 1
#     SUM += Mul
#     i -= 1
# print(f'SUM = {SUM}')

# 求n的阶乘
# i = int(input('请输入一个正整数：'))
# while i != EOFError:
#     a = 1
#     MUL = 1
#     while a <= i:
#         MUL *= a
#         a += 1
#     print(f'{MUL}')
#     i = int(input('请输入一个正整数：'))
# 求 1! + 2! + 3! + ... + n!
i = 1
n = int(input('请输入n：'))
SUM = 0
while n != 0:
        MUL = 1
        while i <= n:
            MUL *= i
            i += 1
        n -= 1
        SUM += MUL
print(SUM)


# for循环打印1-10
# for i in range(1,11):
#     print(f'{i}')

# for循环打印2，4，6，8，10
# for i in range(2,11,2):
#     print(f'{i}')

# for循环打印10，9，8，7...
# for i in range(10, 0, -1):
#     print(f'{i}')

# for循环求1+2+3+...+100
# a = 0
# for i in range(1, 101):
#     a += i
# print(a)
# a换成i为什么不对


# 吃包子与break，continue练习，第三个有虫子
# flag = 0
# STR = '有虫子不吃这个了'
# for i in range(1,6):
#     flag += 1
#     if i == 3:
#         print(STR)
#         continue
#     print(f'{flag}')

# 若干个数字，求平均值（也不知道几个数字）--------------多组输入求平均值
# if input() != EOFError:



