# 字符串的一些方法
# capitalize() 把第一个字符大写
str1 = "xiaozhao"
str1 = str1.capitalize()
print(str1)
# casefold() 把所有字符小写
str1 = "XIAOZHAO"
str1 = str1.casefold()
print(str1)
# center(width) 将字符串居中，并使用空格填充至长度width的新字符串
str1 = "xiaozhao"
str1 = str1.center(50)
print(str1)
# count(sub[,start[,end]]) 返回sub在字符串出现的次数，start和end参数表示范围
str1 = "xiaozhao"
print(str1.count('o', 4, 8))
# encode(encoding='utf-8', errors='strict') 以encoding指定的编码格式对字符串进行编码
str1 = "小赵"
str1 = str1.encode(encoding='utf-8', errors='strict')
print(str1)
# endswith(sub[,start[,end]]) 检查字符串是否以sub字符串结束，如果是返回True，否则返回False，start和end参数表示范围，可选
str1 = "xiaozhao"
print(str1.endswith("zhao"))
# expandtabs([tbsize=8]) 把字符串中的tab符号转换为空格，如不指定参数，默认的空格数是tabsize=8
str1 = "xiaozhao\t123"
str1 = str1.expandtabs(tabsize=1)
print(str1)
# find(sub[,start[,end]]) 监测sub是否包含在字符串中，如果有则返回索引值，否则返回-1，start和end参数表示范围，可选
str1 = "xiaozhao"
print(str1.find("x"))
print(str1.find("m"))
# index(sub[,start[,end]]) 跟find方法一样，不过如果sub不在string中会产生一个异常
str1 = "xiaozhao"
print(str1.index("x"))
# isalnum() 如果字符串至少有一个字符并且所有字符串都是字母或数字(即没有除字母或者数字外的字符)则返回True，否则返回False
str1 = "xiaozhao"
str2 = "123"
str3 = "x1123("
str4 = "x123"
str5 = ""
print(str1.isalnum(), str2.isalnum(), str3.isalnum(), str4.isalnum(), str5.isalnum())
# isalpha() 如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
str1 = "xiaozhao"
str2 = "123"
str3 = "x1"
str4 = ""
print(str1.isalpha(), str2.isalpha(), str3.isalpha(), str4.isalpha())
# isdecimal() 如果字符串只包含十进制数字则返回True，否则返回False
str1 = "xiaozhao"
str2 = "123"
str3 = "x1"
str4 = ""
print(str1.isdecimal(), str2.isdecimal(), str3.isdecimal(), str4.isdecimal())
# isdigit() 如果字符串只包含数字则返回True，否则返回False
str1 = "xiaozhao"
str2 = "123"
str3 = ""
print(str1.isdigit(), str2.isdigit(), str3.isdigit())
# islower() 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是小写，则返回True，否则返回False
str1 = "xiaozhao"
str2 = "123"
str3 = "xZ"
print(str1.islower(), str2.islower(), str3.islower())
# isnumeric() 如果字符串中只包含数字字符，则返回True，否则返回False
str1 = "123"
str2 = "x1"
print(str1.isnumeric(), str2.isnumeric())
# isspace()如果字符串中只包含空格，则返回False
str1 = " "
str2 = "    "
str3 = "123xiaozhao"
print(str1.isspace(), str2.isspace(), str3.isspace())
# istitle() 如果字符串是标题化(所有单词都是大写开始，其余小写)返回True，否则返回False
str1 = "Xiao Zhao"
str2 = "xZhao"
print(str1.istitle(), str2.istitle())
# isupper() 如果字符串中至少包含一个区分大小写的字符，并且这些字符都是大写，则返回True，否则返回False
str1 = "XIAOZHAO"
str2 = "xIAOZHAO"
print(str1.isupper(), str2.isupper())