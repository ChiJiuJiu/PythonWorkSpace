# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup
# 正则库
import re
# csv读写
import csv


# 定义请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'}
# 文件路径
file = 'games.csv'
# 爬取数据网页前缀
url_prefix = 'https://steamstats.cn/peak/'


def getOnePageData(url):
    list = []
    res_games = requests.get(url, headers=headers)
    bs_games = BeautifulSoup(res_games.text, 'html.parser')
    # 游戏名、历史在线峰值、steam商店链接
    items = bs_games.find_all('tr', class_='pointer')
    res_td = r'<td>(.*?)</td>'
    prefix = 'https://store.steampowered.com'
    for game in items:
        name = game.find('div')['aria-label']
        top = re.findall(res_td, str(game), re.S | re.M)[3]
        app_url = game.find('a', class_='mw-150 d-block')['href']
        game = {"name": name, "top": top, "app_url": prefix + app_url}
        list.append(game)
    return list


def writeOnePageData(file, data):
    try:
        csvfile = open(file, "a", newline='', encoding='utf-8')
        writer = csv.writer(csvfile)
        for game in data:
            writer.writerow([game['name'], game['top'], game['app_url']])
    except IOError as e:
        print(e)
    finally:
        csvfile.close()


csvfile = open(file, "w", newline='', encoding='utf-8')
writer = csv.writer(csvfile)
# 表头
writer.writerow(('游戏名', '历史在线峰值', 'steam商店链接'))
csvfile.close()

def writeAllPageData(file, begin, end):
    for i in range(begin, end + 1):
        writeOnePageData(file, getOnePageData(url_prefix + str(i)))


writeAllPageData(file, 1, 948)

