# 函数
def myFun(a, b):
    print("%d + %d = %d" % (a, b, a+b))
    print("{a} + {b} = {c}".format(a=a, b=b, c=a+b))

def myFun2(i):
    return i

myFun(1, 2)
print(myFun2(1))
