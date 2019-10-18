import random
# 对\没有进行转义
string1 = "c:\now"
print(string1)

# 对\进行转义
string2 = "c:\\now"
print(string2)

# 不转移也可以正常输出
string3 = r"c:\now"
print(string3)

# 随机数
num = random.randint(1, 100)

# 布尔值运算
a = True
b = False

print(a + b)
print(a - b)
print("a=", a.__int__(), "\nb=", b.__int__())

# 类型转换
a = "123"
print(int(a))
a = 5.523
print(int(a))

a = "123"
b = float(a)
print(b)
a=123
b=float(a)
print(b)

a = 123
print(str(a))

# 变量类型的判断
print(type(a))
print(isinstance(a, str))

# 运算
# 除法
print(10 // 2)
print(2.5 // 2)
print(2.5 / 2)

# 幂运算
print(3 ** (1+1))

# 取余
print(3 % 2)

# 优先级
# 单目运算符比左边优先级低比右边优先级高
print(-3 ** 2)
print(3 ** -2)

print(3 < 4 > 0) # 相当于 3 < 4 and 4 > 0

# 分支结构
number = input("input a number")
number = int(number)
if number == 1:
    print("yes")
elif number == 2:
    print("not 2")
else:
    if number == 3:
        print("not 3")
    else:
        print("bye")


# 三元操作符
x, y = 4, 5
if x < y:
    small = x
else:
    small = y

# 可以简化为
small = x if x < y else y

# 断言
assert 3 > 4