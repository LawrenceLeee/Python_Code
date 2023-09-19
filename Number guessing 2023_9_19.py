import random
def menu():
    print('###################')
    print('#      猜数字小游戏欢迎你      #')
    print('###################')
    return input('输1开始游戏，输0退出游戏：')

def __bool__(flag):
    if flag == 1:
        return True
    else:
        return False


flag = menu()
__bool__(flag)
while bool(flag):
    num = random.randint(1,100)
    guess = int(input('1-100随机数已生成，你猜是多少：'))
    while guess != 0:
        if guess == num :
            print('真他妈聪明，猜对了:)')
            break
        elif guess < num:
            print('猜小了傻逼')
        else:
            print('猜大了弱智')
        guess = int(input('再试个数吧傻逼：'))
    break
print('游戏结束')