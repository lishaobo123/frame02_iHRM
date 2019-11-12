"""
    测试套件:
        按照需求组合被执行的测试函数


"""
# 1.导包
import unittest
from case.Test_iHRM_Emp import Test_Emp
from case.Test_iHRM_Login import Test_Login

# 2.实例化套件对象，组织被执行的测试函数
suite = unittest.TestSuite()
suite.addTest(Test_Login("test_login_success"))  # 组织登录成功的测试函数
suite.addTest(Test_Emp("test_add"))  # 组织员工新增的测试函数
suite.addTest(Test_Emp("test_update"))  # 组织员工修改的测试函数
suite.addTest(Test_Emp("test_get"))  # 组织查询的测试函数
# 3.执行套件，生成测试报告

ruuner = unittest.TextTestRunner()
ruuner.run(suite)
