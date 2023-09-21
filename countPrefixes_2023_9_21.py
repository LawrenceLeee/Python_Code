# 遍历words，取出每个字符串，判断字符串是否是s的前缀
# 用startswith方法
def count_prefixes(words: list, s: str):
    count = 0
    for word in words:
        if s.startswith(word):
            # s 是以 word 开头
            count += 1
    return count


print(count_prefixes(['a', 'b', 'c', 'ab', 'bc', 'abc'],'abc'))

# 还有endswith方法，还可用in判断是不是字符串一部分
