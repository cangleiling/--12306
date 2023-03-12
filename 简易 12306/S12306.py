import requests
import prettytable as pt
from start import *
from seleium_12306 import seleium_start_QP


# f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={data}&leftTicketDTO.from_station={from_data}&leftTicketDTO.to_station={to_data}&purpose_codes=ADULT'
url = f'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={data}&leftTicketDTO.from_station={url_from_data}&leftTicketDTO.to_station={url_to_data}&purpose_codes=ADULT'.format(data,from_data,to_data)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Cookie': 'JSESSIONID=7F67D0FB3EBA426A5553A22A2D450965; _jc_save_wfdc_flag=dc; BIGipServerotn=2129133834.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=837288202.50215.0000; RAIL_EXPIRATION=1673566972665; RAIL_DEVICEID=eqEIrMPxOFDnO0V0zkLITaiHOH4uAXOkvU3HQjDiemIZAdteT4OxW-CBKjwRKOhY5E009QsNObapO2dM0VJ-jGa286kzSnHwcpkGBzWBbKY7HdyckN_f7krAVkLQZFnYg9l6x1HKrTwD7VHF7BFxa8Z-pQPleUqs; route=6f50b51faa11b987e576cdb301e545c4; fo=k89z2x52rfevcjd8JsQozoY_SSv7S6k--daEjiXUrrPHcioEeGMUGwoR6sAY1EsVJyJzVioMXEhvIZXjP0jn1OAxAkZhfqhJTjeMx-zMHcjt9Nhmebajny5liQ20gq6poKsZkGx-QDGF6qwGh9WXb2RTLOdcP7MOIbteGBmU-PvyXW33HWe9PkI6zOQ; _jc_save_fromStation=%u5B89%u9633%2CAYF; _jc_save_toStation=%u82CF%u5DDE%2CSZH; _jc_save_fromDate=2023-01-14; _jc_save_toDate=2023-01-09; current_captcha_type=Z',
}

resp = requests.get(url=url,headers=headers,)
resp.encoding = 'UTF-8'
tb= pt.PrettyTable()
tb.field_names = [
        '车次',
        '出发时间',
        '到达时间',
        '耗时',
        '软卧',
        '无座',
        '硬卧',
        '硬座',
        '二等座',
        '一等座',
        '特等座',
]
json_data1 = resp.json()
data_list = json_data1['data']['result']
for item in data_list:
    info = item.split('|')
    num = info[ 3 ]  # 车次
    start_time = info[ 8 ]  # 出发时间
    end_time = info[ 9 ]  # 到达时间
    use_time = info[ 10 ]  # 到达时间
    soft_slpeer = info[ 23 ]  # 软卧
    no_seat = info[ 26 ]  # 无座
    hard_slpeer = info[ 28 ]  # 硬卧
    hard_seat = info[ 29 ]  # 硬座
    second_class = info[ 30 ]  # 二等
    fiarst_class = info[ 31 ]  # 一等
    topGrade = info[ 32 ]  # 特等
    dit = {
        '车次': num,
        '出发时间': start_time,
        '到达时间': end_time,
        '耗时': use_time,
        '软卧': soft_slpeer,
        '无座': no_seat,
        '硬卧': hard_slpeer,
        '硬座': hard_seat,
        '二等座': second_class,
        '一等座': fiarst_class,
        '特等座': topGrade,

    }

    tb.add_row([
        num,
        start_time,
        end_time,
        use_time,
        soft_slpeer,
        no_seat,
        hard_slpeer,
        hard_seat,
        second_class,
        fiarst_class,
        topGrade,
    ])
print(tb)
sub = input('是否进行抢票:(y/n)')
if not sub == 'n':
    seleium_start_QP()





