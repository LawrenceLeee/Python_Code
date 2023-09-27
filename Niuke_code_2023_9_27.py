# a = ['s', 'n', 'o', 'w', 'y']
# print(a)
# a.pop()
# print(a)
# a.append('d')
# print(a)

# a = map(int,input().split())
# sum = 0
# for i in range(1,len(a)):
#     sum += a[i]
# print(sum)

# a = list(map(int,input().split()))
# print(max(a))
# print(min(a))
# print(sum(a))

# a = list(map(float,input().split(\n)))
# if a[0] > a[1]:
#     print("Tencent")
# else:
#     print("Alibaba")

# a = []
# for i in range(0,2):
#     a.append(float(input()))             #a.append(map(float,input()))错误！！！
# if a[0] > a[1]:
#     print("Tencent")
# else:
#     print("Alibaba")


# def Cac(x, y):
#     return x+y, x-y
#
#
# x, y = map(int,input().split())
# a, b = Cac(x, y)
# print(f'{a} {b}\n{a*b}')

#上面代码的错误版本
# def Cac(x, y):
#     return x + y, x - y
#
#
# x, y = map(int, input().split())
# a, b = Cac(x, y)
# print(a, b, "\n", a * b, sep=' ')

# a = list(input().split())
# flag, flag2 = 0, 0
# for i in range(0,len(a)):
#     flag3 = False
#     if a[i] == 'NiuNiu':
#         flag += 1
#         flag3 = True
#     if flag == 1 and flag3:
#         flag2 = i
# print(flag,flag2,sep='\n')

#错误的版本
# a = tuple(input().split())
# b = tuple(input().split())
# c = (a(:2) + b(-3:))
# print(a, b, c, sep='\n')

# a = tuple(input().split())
# b = tuple(input().split())
# c = (a[:3] + b[-3:])                       #c = (a[:2] + b[-3:]) 错误代码，不包含后边界值
# print(a, b, c, sep='\n')

# a = ['NiuMei', 'NiuKele', 'NiuNeng']
# b = [3, 4, 5, 8]
# b.pop()
# c = list(zip(a, b))
# print(c)

# a = 3
# while True:
#     num = int(input())
#     if num == a:
#         print("Congratulations!")
#         break
#     if num < 0:
#         print("Give up!")
#         break

# flag = 0
# a = list(input().split())
# for i in range(0, len(a)):
#     print(a[i])
#     flag += 1
# print(flag)

# a = list(input().split())
# for i in range(0,len(a),5):
#     print(a[i])
#
#     n = int(input())
#     a = []
#     for i in range(2, 2 * n + 1, 2):
#         a.append(i)
#     print(a)

# a = list(map(int,input().split()))
# for i in range(0, len(a)):
#     if a[i] == 3:
#         continue
#     if a[i] == 8:
#         break
#     print(a[i])

# a = []
# for i in range(1,3):
#     a.append(input())
# print(f'Happy {a[1]}th birthday to {a[0]}!')

# a = input()
# n = int(input())
# if 0 <= n < len(a)-2:
#     print(a[n], a[:n+2], sep='\n')
