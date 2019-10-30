# 递归
# 递归求阶乘
def fun1(x):
    if x == 0:
        return 1
    return x*fun1(x-1)

# 非递归求阶乘
def fun2(x):
    result = x
    for i in range(1,x):
        result *= i
    return result

print("递归：",fun1(5),"\n非递归：",fun2(5))

# 汉诺塔
def hanoi(n, x, y, z):
    if n==1:
        print(x, "--->", z)
    else:
        hanoi(n-1, x, z, y)
        print(x, "--->", z)
        hanoi(n-1, y, x, z)

hanoi(3, "X", "Y", "Z")