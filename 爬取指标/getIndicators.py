# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup
# 正则库
import re
# csv读写
import csv
# 定义请求头
import pandas as pd

# 设置cookie(绕过成人认证)
cookie = {"Steam_Language": "chinese", "birthtime": "725817601", "lastagecheckage": "1-January-1993"}
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'Accept-Language': "zh-CN,zh;q=0.9"
}

# 文件路径
file = 'games.csv'
saveFile = "indicators.csv"


def getSteamUrl(file):
    list = []
    csv_reader = csv.reader(open(file, encoding='utf-8'))
    for row in csv_reader:
        list.append({"name": row[0], "top": row[1], "url": row[2]})
    # 去表头
    return list[1:]


def getGameType(data):
    type = []
    res_type = r'.*多人.*|.*合作.*|.*单人.*'
    for item in data:
        type = re.findall(res_type, str(item))
        if len(type) == 1:
            break
    if len(type) == 0:
        type = ["其他"]
    return type[0]


def isSupportChinese(data):
    support = []
    res_language = r'不支持'
    support = re.findall(res_language, str(data[1]))
    if len(support) == 0:
        return "是"
    return "否"


def getIndicators(data):
    list = []
    cnt = 0
    for game in data:
        cnt += 1
        print(cnt)
        name = game["name"]
        steam_url = game["url"]
        top = game["top"]
        res_game = requests.get(steam_url, cookies=cookie, headers=headers)
        bs_game = BeautifulSoup(res_game.text, 'html.parser')
        # 内容主题/类型
        theme_list = []
        price_list = []
        res_a = r'<a.*?>(.*?)</a>'
        themes_a = bs_game.find_all("a", class_="app_tag")
        themes = re.findall(res_a, str(themes_a), re.S)
        for item in themes:
            theme_list.append(item.strip())
        # 开发商
        dev_publisher = bs_game.find_all("div", class_="dev_row")
        # 有些游戏页面可能已经下线
        if len(bs_game.find_all("div", class_="dev_row")) < 2:
            continue
        dev = re.findall(res_a, str(dev_publisher[0]), re.S)
        # 发行商
        publisher = re.findall(res_a, str(dev_publisher[1]), re.S)
        # 收费
        price_div = bs_game.find("div", class_="game_purchase_price price")
        res_div = r'<div.*?>(.*?)</div>'
        price = re.findall(res_div, str(price_div), re.S)
        for price_item in price:
            price_list.append(price_item.strip().replace("¥ ", ""))
        # 打折影响div标签, 重写匹配
        if len(price) == 0:
            price_div = bs_game.find("div", class_="discount_original_price")
            res_div = r'<div.*?>(.*?)</div>'
            price = re.findall(res_div, str(price_div), re.S)
            for price_item in price:
                price_list.append(price_item.strip().replace("¥ ", ""))
        # 平台
        # 因为steam平台上没有手游，所以都是PC
        platform = "PC"
        # 性质
        # 从内容列表和网页标签里匹配
        category_div = bs_game.find_all('div', class_='game_area_details_specs')
        categorys = re.findall(res_a, str(category_div), re.S)
        category = getGameType(theme_list + categorys)
        # 是否支持中文
        language_list = bs_game.find_all('tr')
        is_support = isSupportChinese(language_list)

        list.append(
            {"name": name, "theme": ",".join(theme_list), "dev": ",".join(dev), "publisher": ",".join(publisher),
             "price": "".join(price_list), "platform": platform, "category": category, "is_support_chinese": is_support,
             "top": top})
        writeToCsv(list)
        list.clear()
    return list


def writeToCsv(data):
    try:
        csv_file = open(saveFile, "a", newline='', encoding='utf-8')
        writer = csv.writer(csv_file)
        for game in data:
            print(game)
            writer.writerow(
                [game['name'], game['theme'], game['dev'], game['publisher'], game['price'], game['platform'],
                 game['category'], game["is_support_chinese"], game['top']])
    except IOError as e:
        print(e)


csvfile = open(saveFile, "w", newline='', encoding='utf-8')
writer = csv.writer(csvfile)
# 表头
writer.writerow(('游戏名', '类型', '开发商', '发行商', '价格', '平台', '性质', '是否支持中文', '历史在线峰值'))
csvfile.close()


# 所有游戏列表以及指标
# game_list = getIndicators(getSteamUrl(file))
# 写入csv

def main():
    # writeToCsv(game_list)
    getIndicators(getSteamUrl(file))


if __name__ == '__main__':
    main()