# -*- coding:utf-8 -*-
import json
import requests
import re
import xlrd
from xlutils.copy import copy
from data.readFile import *

file_name = 'TestData.xls'
file_data = read(file_name).get_filedata()
table = file_data.sheets()[0]#选择sheet
hurl = table.cell(7,1).value#读取URL
def test_get_token():
    '''登陆'''
    husername = table.cell(3,1).value
    hpassword = table.cell(4,1).value
    hotp = table.cell(5,1).value
    hcontent_type = table.cell(6,1).value
    hdata = {
        "username":husername,
        "password":hpassword,
        "otp":hotp
        }
    headers = {
        'content-type': hcontent_type
        }
    r = requests.get(hurl,headers=headers)
    code = str(r.status_code)
    print('请求返回状态为：'+ code)
    if code == table.cell(9,1).value:
        res_tr = r"<input type='hidden' name='csrfmiddlewaretoken' value='(.*?)' />"
        token = re.findall(res_tr, r.text, re.S | re.M)[0]
        print('当前token为：'+token)
        #将获取的TOKEN保存到testdata中
        new_file_data = copy(file_data)
        sheet = new_file_data.get_sheet(0)
        sheet.write(9, 1, token)
        sheet.write(8, 1, token)
        print ("Token写入成功")
        new_file_data.save('TestData.xls')
        print ("TestdDate保存成功")

    else:
        print('登陆失败，程序退出')
        exit()



