# 文件
# 相对路径
f = open("Hello/file.txt")
# read()方法，若不传入参数，则默认读取整个文件
print(f.read())
# 关闭文件
# python会缓存写入数据，及时关闭文件才能在意外情况下保存下来
f.close()
f = open("Hello/file.txt", "r+")
# 文件指针
print(f.read(7))
# 显示当前文件指针的位置
print(f.tell())
# seek(offset, from)方法，在文件中移动文件指针，从from(0代表文件起始位置，1代表文件当前位置，2代表文件末尾)
# 便宜offset个字节
f.close()
f = open("Hello/file.txt")
# 从头开始，移7个字节
f.seek(8, 0)
# 读取
print(f.readline())
# 直接转换为列表
text = list(f)
print(text)
# 也可以直接用for
# 把文件指针移动到文件开头
f.seek(0, 0)
for each in f:
    print(each)

# 创建一个文件，并写点东西
f2 = open("file2.txt", "w", encoding="utf-8")
# 将字符串写入文件
f2.write("小赵123")
f2.close()
# 追加
f2 = open("file2.txt", "a", encoding="utf-8")
# 向文件写入字符串序列，该序列应是一个返回字符串的可迭代对象
# 元组、列表、字符串都可以
f2.writelines(("1", "2"))
f2.writelines("\n3 4\n")
f2.writelines(['5', '6'])
f2.close()

