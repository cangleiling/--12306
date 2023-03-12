import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from start import *

def seleium_start_QP():
    cc_type = input('选择你需要的列车(如:快车/特快/直达/动车/高铁:k/t/z/d/g):')
    url = 'https://kyfw.12306.cn/otn/resources/login.html'

    driver = webdriver.Chrome()
    #跳过selenium检测滑块验证码无法识别的问题
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                           {'source':'''Object.defineProperty(navigator,'webdriver',{get:() => undefined})'''})
    driver.get(url=url)
    driver.find_element('xpath','//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()
    driver.find_element('xpath','//*[@id="J-userName"]').send_keys(username)
    driver.find_element('xpath','//*[@id="J-password"]').send_keys(password)
    driver.implicitly_wait(5)
    driver.find_element('xpath','//*[@id="J-login"]').click()
    driver.implicitly_wait(10)
    driver.find_element('xpath','//*[@id="link_for_ticket"]').send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    driver.find_element('xpath','//*[@id="fromStationText"]').click()# 出发地
    driver.find_element('xpath','//*[@id="fromStationText"]').clear()
    driver.find_element('xpath','//*[@id="fromStationText"]').send_keys(from_data)
    driver.find_element('xpath','//*[@id="fromStationText"]').send_keys(Keys.ENTER)

    driver.find_element('xpath','//*[@id="toStationText"]').click()# 目的地
    driver.find_element('xpath','//*[@id="toStationText"]').clear()
    driver.find_element('xpath','//*[@id="toStationText"]').send_keys(to_data)
    print(to_data + ' ' * 50)
    driver.find_element('xpath','//*[@id="toStationText"]').send_keys(Keys.ENTER)

    driver.find_element('xpath','//*[@id="train_date"]').click()# 日期
    driver.find_element('xpath','//*[@id="train_date"]').clear()
    driver.find_element('xpath','//*[@id="train_date"]').send_keys(data)

    if cc_type == 'g':
        driver.find_element('xpath','/html/body/div[1]/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[1]/input').click()# 高铁
    elif cc_type == 'd':
        driver.find_element('xpath','/html/body/div[1]/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[2]/input').click()#动车
    elif cc_type == 'z':
        driver.find_element('xpath','/html/body/div[1]/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[3]/input').click()#直达
    elif cc_type == 't':
        driver.find_element('xpath','/html/body/div[1]/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[4]/input').click() #特快
    elif cc_type == 'k':
        driver.find_element('xpath','/html/body/div[1]/div[7]/div[5]/div[2]/div[2]/div[2]/ul/li[5]/input').click()# 快车
    driver.find_element('xpath','/html/body/div[1]/div[7]/div[4]/form/div[3]/div/a').click()# 查询

    time.sleep(5)
    driver.find_element('xpath','/html/body/div[2]/div[7]/div[8]/table/tbody/tr[1]/td[13]/a').click() # 选择第一趟车次的预订按钮
    time.sleep(5)
    driver.find_element('xpath','/html/body/div[1]/div[10]/div[3]/div[2]/div[1]/div[2]/ul/li/input').click() # 选择乘车人
    time.sleep(10)
    driver.find_element('xpath','//*[@id="submitOrder_id"]').click() # 点击订单提交按钮
    time.sleep(5)
    try:
        driver.find_element('xpath','/html/body/div[5]/div/div[5]/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[2]/ul[1]/li[1]/a').click() #可选的座位号
    except Exception as ex:
        print('没有可选的座位号')
    time.sleep(20)#测试等待 为了演示点击了确认按钮
    driver.find_element('xpath','//*[@id="qr_submit_id"]').click()

    driver.find_element('xpath','//*[@id="insurance_buy_and_agree"]').click()
    driver.implicitly_wait(5)
    driver.find_element('xpath','//*[@id="ins_select_all"]').click()
    driver.find_element('xpath','//*[@id="payButton"]').click()
    driver.quit()