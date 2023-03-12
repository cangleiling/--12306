'''
useranme
password
from_station
to_station
data
'''
import json
from_data = input('出发地:')
to_data = input('目的地:')
data_time = input('日期:(格式:2022-12-12):')
username = '17610386097'
password = 'Hyf123456hyf'


f= open('city.json',encoding='utf-8')
txt= f.read()
json_data = json.loads(txt)
url_from_data = json_data[from_data]
url_to_data = json_data[to_data]
data= data_time
# print(from_data)
# print(to_data)
