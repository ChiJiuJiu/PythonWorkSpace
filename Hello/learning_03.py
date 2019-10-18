# 列表
empty = []
empty.append(123)
empty.append("zyj")
empty.append([1])
# 用列表扩展列表
empty.extend([2, 3, 4])
empty.insert(0, 'first')
print(empty, '\n', empty[2], end='\n')

# 删除元素
empty.remove('first')
print(empty)
del empty[0]
print(empty)
member = empty.pop(0)
print(member, end='\n')
print(empty, end='\n')

# 分片
print('分片', end='\n')
list01 = [1, 2, 3, 4, 5, 6]
list02 = list01[1:4]
list03 = list01[:4]
list04 = list01[0:]
list05 = list01[:]
print(list02, '\n', list03, end='\n')

# 比较
list1 = [123, 999]
list2 = [234, 0]
print(list1 > list2)

# 拼接, 类似extend()
list3 = list1 + list2
print(list3, end='\n')
list3 *= 3
print(list3)

# 成员操作
print(123 in list3, 'zyj' not in list3, end='\n')

list4 = [1, 2, [4, 5, 6], 3]
# 成员操作只影响一层，但可以人为干涉
print(4 in list4, 4 in list4[2])
# 列表中的列表的值
print(list4[2][0])

# 反转列表
list4.reverse()
list4[1].reverse()
print(list4)

# 排序
# 正序
list5 = [2, 5, 1, 3, 9, 99, 82, 12]
list5.sort()
print(list5)

# 倒序
# 1. 排序再翻转
list5.sort()
list5.reverse()
print(list5)

# 2. reverse=True
list5 = [2, 5, 1, 3, 9, 99, 82, 12]
list5.sort(reverse=True)
print(list5)