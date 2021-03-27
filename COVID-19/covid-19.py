import requests
import pandas as pd
import time
pd.set_option('max_rows',500)

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Mobile Safari/537.36 Edg/87.0.664.52'
}

url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'   # 定义要访问的地址
r = requests.get(url, headers=headers)  # 使用requests发起请求

print(r.status_code)  # 查看请求状态
print(type(r.text))
print(len(r.text))


import json
data_json = json.loads(r.text)
data_json.keys()

data = data_json['data'] # 取出json中的数据
data.keys()

data_province = data['areaTree'][2]['children']  # 取出中国各省的实时数据
type(data_province)
data_province[0].keys()
for i in range(len(data_province)): # 遍历查看各省名称、更新时间
    print(data_province[i]['name'],data_province[i]['lastUpdateTime'])
    if i == 5:
        break
pd.DataFrame(data_province).head(200) # 直接生成数据效果并不理想

# 获取id、lastUpdateTime、name
info = pd.DataFrame(data_province)[['id','lastUpdateTime','name']]
info.head()

# 获取today中的数据
today_data = pd.DataFrame([province['today'] for province in data_province ])
today_data.head()