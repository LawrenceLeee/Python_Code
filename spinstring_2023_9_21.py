# 旋转字符串，把最左侧字符放到最右侧，判断经旋转后 s 能否变成 goal
# 字符串+字符串，可以在其中找到，旋转过程中任意一种情况
def rotate_string(s, goal):
    if len(s) != len(goal):
        return False
    return goal in (s + s)


print(rotate_string("abcde", "edcab"))
print(rotate_string("abcde", "bcdea"))


