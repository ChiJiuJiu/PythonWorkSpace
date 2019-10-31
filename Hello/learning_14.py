# 文件分类
# 要求：
# task.txt文件中有三段对话，均以"="分隔，且都由xiaozhao1和xiaozhao2两个角色的对话构成。
# 现要求把这三段对话按照对话以及角色分类，分别保存。且去掉对话前的角色名。

# 角色1和角色2的内容列表
xiaozhao1 = []
xiaozhao2 = []
# 文件编号
number = 1


# 分割文件方法
# 入参：文件路径
def splitFile(file_path):
    global number
    f = open(file_path, "r", encoding="utf-8")
    # 遍历文件
    for each_line in f:
        # 判断是不是'===='，只判断前面几个就可以了
        if each_line[:3] != "===":
            # 分割字符串
            (role, speak) = each_line.split(":")
            if role == "xiaozhao1":
                xiaozhao1.append(speak)
            if role == "xiaozhao2":
                xiaozhao2.append(speak)
        else:
            # 文件
            save_path1 = "xiaozhao1_" + str(number) + ".txt"
            save_path2 = "xiaozhao2_" + str(number) + ".txt"
            saveFile(save_path1, xiaozhao1)
            saveFile(save_path2, xiaozhao2)
            # 重置列表
            xiaozhao1.clear()
            xiaozhao2.clear()
            number += 1
    # 最后一段的保存不包括在for循环当中，单独处理
    save_path1 = "xiaozhao1_" + str(number) + ".txt"
    save_path2 = "xiaozhao2_" + str(number) + ".txt"
    saveFile(save_path1, xiaozhao1)
    saveFile(save_path2, xiaozhao2)
    f.close()


# 保存新文件方法
# 入参：文件保存路径，要保存的内容
def saveFile(file_path, toSave):
    f = open(file_path, "w", encoding="utf-8")
    f.writelines(toSave)
    f.close()

# 调用
splitFile("task.txt")