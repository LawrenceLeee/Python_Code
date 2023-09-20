# 单词逆序
# python中思路是根据空格切分单词
# 字符串split方法可以指定分隔符，把字符串分成多部份放到一个list里
# 针对刚才的切分结果列表进行逆序
# 再把逆序后的列表组合起来，join

def reverse_words(s: str):   # 声明参数类型
    tokens = s.split(' ')         #  按空格切分
    tokens.reverse()            # 对列表内容进行逆序
    return ' '.join(tokens)     # 借助空格作为分隔符，重新拼接元素

print(reverse_words("I am a student"))




