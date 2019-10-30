# 集合
# 无序唯一的, 不能索引
set1 = {1, 2, 2, 3, 1, 5, 3}
print(set1)

set2 = set((1, 3, 2, 4, 5, 5, 6, 6))
print(set2)

# 去重操作
number = [1, 2, 2, 3, 6, 6, 8, 9]

# 方法一
temp = []
for each in number:
    if each not in temp:
        temp.append(each)
print("去重前", number)
print("去重后", temp)

# 方法二
temp2 = list(set(number))
print(temp2)

# 不可变集合
# 一般集合可以进行增删操作
ss = {1, 2, 3}
ss.add(6)
ss.add(2) # 重复的不会增加
ss.remove(1)
print(ss)
# 不可变集合不能进行增删操作
fs = frozenset({1, 2, 3})
# fs.add(4) 报错