# 对\没有进行转义
str = "c:\now"
print(str)

# 对\进行转义
str = "c:\\now"
print(str)

# 不转移也可以正常输出
str = r"c:\now"
print(str);