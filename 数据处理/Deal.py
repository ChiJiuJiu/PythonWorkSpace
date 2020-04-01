import pandas as pd
import Functions as Utils


# 数据文件路径
file_path = 'data.csv'

# 指标和在线人数峰值
data = pd.read_csv(file_path,header=0,encoding="utf-8", dtype = {'历史在线峰值' : int})
# 去空值
data.dropna(axis=0, how='any', inplace=True)
# 索引重置
data = data.reset_index(drop=True)



# 分组统计
# 类型
data['类型'] = Utils.cast(data, '类型')
Utils.indicators_top_write_to_csv(data, '类型', "type_top.csv")

# 开发商
# 替换列的类型
data['类型'] = Utils.cast(data, '开发商')
Utils.indicators_top_write_to_csv(data, '开发商', "dev_top.csv")


# 发行商
data['发行商'] = Utils.cast(data, '发行商')
Utils.indicators_top_write_to_csv(data, '发行商', "publisher_top.csv")

# 价格
Utils.indicators_top_write_to_csv(data, '价格', "price_top.csv")

# 性质
Utils.indicators_top_write_to_csv(data, '性质', "category_top.csv")

# 是否支持中文
Utils.indicators_top_write_to_csv(data, '是否支持中文', "is_support_chinese_top.csv")

