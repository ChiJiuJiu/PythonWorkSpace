# 函数
def myFun(a, b):
    print("%d + %d = %d" % (a, b, a+b))
    print("{a} + {b} = {c}".format(a=a, b=b, c=a+b))


def myFun2(i):
    return i


myFun(1, 2)
print(myFun2(1))

# 函数文档
def myFun3():
    '这是myFun3的函数文档'
    print(123)

print(myFun3.__doc__)

# 关键字参数, 默认参数
def myFun4(str1="这是参数1", str2="这是参数2"):
    print(str1 + str2)

myFun4()
myFun4("xiaozhao")
myFun4(str2="xiaozhao")
myFun4(str2="123", str1="xiaozhao")

# 收集参数(可变参数)
def myFun5(*para):
    print("参数长度：", len(para))
    print("第二个参数", para[1])

myFun5(1, 2, 3, 4, 5, 6)

# 即使一个函数没有写明返回值，其默认返回值是None
def myFun6():
    print("该函数返回None")
result = myFun6()
print(result)

# 多返回值
def myFun7(a, b):
    return a, b, a+b, "xiaozhao123"
print(myFun7(1, 2))

# 全局变量
count = 10
print("全局变量count：", count)
def myFun8():
    count = 5
    print("fun8中的count：", count)
myFun8()
def myFun9():
    global count
    count = 6
    print("fun9中的count:", count)
myFun9()
print("全局变量count：", count)

# 函数闭包, 即内部函数对外部作用域的变量进行引用
def funX(x):
    def funY(y):
        return  x ** y
    return  funY
print(funX(2)(3))

def myFun10(x):
    def myFun11():
        # 声明x不是内部函数的局部变量
        nonlocal x
        x *= x
        return  x
    return myFun11()
print(myFun10(5))