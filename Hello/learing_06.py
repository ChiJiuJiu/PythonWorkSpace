# format方法示例
formatString1 = "one {0}, one {1}".format("world", "dream")
print(formatString1)
formatString2 = "one {a}, one {b}".format(a = "world", b = "dream")
print(formatString2)
formatString3 = "one {a}, one {0}".format("world", a = "dream")
print(formatString3)
# 此时format不起作用
formatString4 = "{{5}}".format("不打印")
print(formatString4)
# 格式化符号
formatString5 = "{0:.1f}{1}".format(27.658,"GB")
print(formatString5)

# 格式化字符及其ascii码
fs6 = "%c" % 97
print(fs6)
fs7 = "%c %c %c" % (97, 98, 99)
print(fs7)
# 格式化整数
fs8 = "%d + %d = %d" % (4, 5, 4 + 5)
print(fs8)
# 10进制转8进制
fs9 = "%o" % 10
print(fs9)
# 10进制转16进制(小写)
fs10 = "%x" % 10
print(fs10)
# 10进制转16进制(大写)
fs11 = "%X" % 10
print(fs11)
# 定点数, 默认精确6位
fs12 = "%.2f" % 66.666
print(fs12)