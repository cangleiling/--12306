import requests
import re
import json
url = 'https://www.12306.cn/index/script/core/common/station_name_v10184.js'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}
resp = requests.get(url, headers= headers)
resp.encoding='utf-8'
stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)',resp.text)
station = dict(stations)
# print(station)
# # station_d = {}
# # for item in station:
# #     station_d[station[item]] = item
# # print(station_d)
#               #在dumps时 如果文件中有中文汉字需要添加ensure_ascii= False
json_data = json.dumps(station,ensure_ascii=False)
with open('city.json','w',encoding='utf-8')as fp:
    fp.write(json_data)



