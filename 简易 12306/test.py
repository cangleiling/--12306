import requests
url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2023-01-14&leftTicketDTO.from_station=AYF&leftTicketDTO.to_station=SZH&purpose_codes=ADULT'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Cookie': 'JSESSIONID=7F67D0FB3EBA426A5553A22A2D450965; _jc_save_wfdc_flag=dc; BIGipServerotn=2129133834.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpassport=837288202.50215.0000; RAIL_EXPIRATION=1673566972665; RAIL_DEVICEID=eqEIrMPxOFDnO0V0zkLITaiHOH4uAXOkvU3HQjDiemIZAdteT4OxW-CBKjwRKOhY5E009QsNObapO2dM0VJ-jGa286kzSnHwcpkGBzWBbKY7HdyckN_f7krAVkLQZFnYg9l6x1HKrTwD7VHF7BFxa8Z-pQPleUqs; route=6f50b51faa11b987e576cdb301e545c4; fo=k89z2x52rfevcjd8JsQozoY_SSv7S6k--daEjiXUrrPHcioEeGMUGwoR6sAY1EsVJyJzVioMXEhvIZXjP0jn1OAxAkZhfqhJTjeMx-zMHcjt9Nhmebajny5liQ20gq6poKsZkGx-QDGF6qwGh9WXb2RTLOdcP7MOIbteGBmU-PvyXW33HWe9PkI6zOQ; _jc_save_fromStation=%u5B89%u9633%2CAYF; _jc_save_toStation=%u82CF%u5DDE%2CSZH; _jc_save_fromDate=2023-01-14; _jc_save_toDate=2023-01-09; current_captcha_type=Z',
}
resp = requests.get(url = url,headers= headers)
print(resp.json())

