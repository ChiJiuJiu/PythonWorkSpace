#匿名函数 lambda表达式
g = lambda x,y : x ** y

print(g(2,3))

# filter()过滤器
test = list(filter(None, [1, 0, False, True, 100, None]))
print(test)
# 过滤出偶数
num = list(filter(lambda x : not (x % 2), range(10)))
print(num)

# map()
powx = list(map(lambda x : x ** 2, range(0, 11)))
print(powx)


