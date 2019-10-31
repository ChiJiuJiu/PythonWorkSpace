# 文件分类
# 要求：
# task.txt文件中有三段对话，均以"="分隔，且都由xiaozhao1和xiaozhao2两个角色的对话构成。
# 现要求把这三段对话按照对话以及角色分类，分别保存。且去掉对话前的角色名。

# 分割文件方法
# 入参：文件路径
# 返回：列表元组
def splitFile(file_path):
    f = open(file_path, "r", encoding="utf-8")
    # 遍历文件
    for each_line in f:
        if 
    f.close()



# 保存新文件方法
# 入参：文件保存路径，要保存的内容
def saveFile(file_path, toSave):
