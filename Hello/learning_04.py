# 元祖
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
print(tuple1[2])
tuple2 = tuple1[:]
print(tuple2)

tuple3 = 1, 2, 3, 4
print(type(tuple3))
# 空元祖
empty = ()
print(type(empty))
print(empty)
# 创建只有一个元素的元祖
single = 1,
print(type(single))
single2 = (1,)
print(type(single2))
print(single, single2, len(single))
# 运算
# 重复操作符 *
tuple4 = (1,)
tuple5 = tuple4 * 8
print(tuple5)

# 更新
tuple6 = ('zyj1', 'zyj2', 'zyj3', 'zyj4', 'zyj6')
tuple6 = tuple6[:4] + ('zyj5',) + tuple6[4:]
print(tuple6)

# 删除
# del tuple6
# 利用分片
tuple6 = tuple6[:4]+tuple6[5:]
print(tuple6)