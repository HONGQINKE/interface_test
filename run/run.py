# -*- coding:utf-8 -*-  


from core.GetToken import *
hhlist = []
def HRunner():
    pass
    #AdminTestCase_01.test_1add_admin()#添加管理员
    #AdminTestCase_01.test_2del_admin()#删除管理员

    #TestReportData = AdminTestCase_01.hlist#返回测试结果，不用模块的测试结果在这里用+号连接合并成一个。


    #hhlist.extend(TestReportData)


if __name__ =="__main__":
    print('------------测试开始------------')
    test_get_token()
    print('------------测试结束------------')

