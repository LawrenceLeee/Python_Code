# import random
#
#
# a = [i for i in range(1, 11)]
# num = random.randint(1, 10)
# print(num)
# sz = len(a)-1
# p = int(len(a)-1)//2
# p = int(p)
# while True:
#     if a[p] == num:
#         print(f'找到了，下标是{num}')
#         break
#     elif a[p] > num:
#         p //= p
#     else:
#         p = (p + sz)/2



sum=0
a=0
while a<5:
    sum+=a
    a+=1
print(f'和为{sum}')