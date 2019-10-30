# 字典
dict1 = {"键1":"值1", "键2":"值2", "键3":"值3"}
print(dict1['键1'])
# 利用dick()创建字典
# ps:dict()方法只有一个入参，所以如果有多个项(键值对，这里可以用元组也可以用列表表示，
# 只要构建映射关系即可)就要在外套一层括号，当作一个参数传入。
dict2 = dict((("键1", 1), ("键2", 2)))
print(dict2)
# 用关键字的方式创建字典
dict3 = dict(xiaozhao1=1, xiaozhao2=2)
print(dict3)
# 修改键对应的值
dict3['xiaozhao1'] = "xiaozhao1"
print(dict3)
# 如果修改的键不存在, 则会增加
dict3['xiaozhao3'] = "3"
print(dict3)

# 批量操作键
dict4 = {}
dict4 = dict4.fromkeys((1, 2, 3), "key")
print(dict4)

# 打印键、值和项
for eachKey in dict4.keys():
    print(eachKey)
for eachValue in dict4.values():
    print(eachValue)
for eachItem in dict4.items():
    print(eachItem)

# 用get()方法更宽松的访问键
print(dict4.get(4))
# 成员资格操作符
print(4 in dict4)
print(3 in dict4)

# update()方法
dict5 = {}
dict5.setdefault(5, "five")
dict5.setdefault(4, "four")
print(dict5)
dict4.update(dict5)
print(dict4)

