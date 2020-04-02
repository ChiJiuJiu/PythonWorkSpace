import pandas as pd
import matplotlib.pyplot as plt
# 数据文件路径
file_path = 'is_support_chinese_top.csv'

# 指标和在线人数峰值
data = pd.read_csv(file_path,header=0,encoding="utf-8", dtype = {'平均在线玩家数' : int})
#print(data)
plt.style.use('fivethirtyeight')
plt.figure(figsize=(15,7.5), dpi= 80)
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False



labels = data['是否支持中文'].tolist()
players = data['平均在线玩家数'].tolist()
plt.title('游戏是否支持中文玩家数对比')
plt.ylabel('平均玩家数')
plt.xlabel('是否支持中文')
plt.bar(labels, players, width=0.7, alpha=0.5, color='#00BFFF')
plt.ylim(500, 4000)
for a,b in zip(labels,players):
 plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=12)


plt.savefig("游戏是否支持中文玩家数对比.jpg")
plt.show()

