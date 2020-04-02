# 截取类型
import re
import pandas as pd
def getTypes(type_list):
    result = []
    res_type = r'[.*a-zA-Z.*]|多人|单人|免费|独立|抢先体验'
    for type in type_list:
        # 匹配去除不需要的type
        re_type = re.findall(res_type, type)
        if len(re_type) == 0:
            result.append(type)
    # 取三个
    if len(result) == 0:
        return '其他'
    return str(result[0])

def getDev(dev_list):
    if len(dev_list) == 0:
        return '其他'
    return dev_list[0]

def cast_type(data,indicator):
    cnt = 0
    to_copy = []
    for i in data[indicator]:
        indicator_list = i.split(',')
        to_copy.append(getTypes(indicator_list))
        cnt += 1
    # 替换列的类型为Series
    return pd.Series(to_copy)

def cast_dev(data, indicator):
    cnt = 0
    to_copy = []
    for i in data[indicator]:
        indicator_list = i.split(',')
        to_copy.append(indicator_list[0])
        cnt += 1
    # 替换列的类型为Series
    return pd.Series(to_copy)

def cast_publisher(data, indicator):
    cnt = 0
    to_copy = []
    for i in data[indicator]:
        indicator_list = i.split(',')
        to_copy.append(indicator_list[0])
        cnt += 1
    # 替换列的类型为Series
    return pd.Series(to_copy)


def indicators_top_write_to_csv(data, indicator, save_path):
    indicator_top = data['历史在线峰值'].groupby(data[indicator]).mean().round(0).to_frame().rename(columns={'历史在线峰值': '平均在线玩家数'}, inplace=False)
    sorted_indicator_top = indicator_top.sort_values(by='平均在线玩家数', ascending=False)
    sorted_indicator_top.to_csv(path_or_buf=save_path, header=True, encoding='utf-8')