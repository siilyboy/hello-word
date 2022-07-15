# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行。
# coding = utf-8

# 2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2021-03-18
@author: Gang Yang
Project:使用unittest框架编写测试用例思路
'''

# 3.导入unittest模块以及其他需要用到的模块
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import time

# 4.定义测试类，父类为unittest.TestCase。
# 可继承unittest.TestCase的方法，如setUp和tearDown方法，不过此方法可以在子类重写，覆盖父类方法。
# 可继承unittest.TestCase的各种断言方法。
class Test(unittest.TestCase):

    # 5.定义setUp()方法用于测试用例执行前的初始化工作。
    # 注意，所有类中方法的入参为self，定义方法的变量也要“self.变量”
    # 注意，输入的值为字符型的需要转为int型

    @classmethod
    def setUpClass(cls) -> None:
        print('开始执行初始化工作...')
        cls.driver = webdriver.Chrome()
        cls.driver.get('https://www.baidu.com/')
        cls.wait = WebDriverWait(webdriver, 10)
        cls.original_window = cls.driver.current_window_handle
        print('初始窗口句柄为 %s' %(cls.original_window))

    # 6.定义测试用例，以“test_”开头命名的方法
    # 注意，方法的入参为self
    # 可使用unittest.TestCase类下面的各种断言方法用于对测试结果的判断
    # 可定义多个测试用例
    # 最重要的就是该部分
    def test_case1(self):
        print('开始执行test_case1')
        self.driver.find_element_by_id('kw').clear()
        self.driver.find_element_by_id('kw').send_keys('四大妖姬')
        time.sleep(3)
        self.driver.find_element_by_id('kw').submit()
        time.sleep(3)
        print('您当前访问的地址为: %s' %(self.driver.current_url))
        self.title = self.driver.title
        print(self.driver.title)

        for window_handle in self.driver.window_handles:
            if window_handle != self.driver.current_window_handle:
                self.driver.switch_to_window(window_handle)
                break

        print('当前浏览器的句柄是：%s' % (self.driver.current_window_handle))
        self.assertEqual(self.title, '四大妖姬_百度搜索', msg='你搜索的内容为：四大妖姬_百度搜索')

    def test_case2(self):
        print('开始执行test_case2')
        # self.number
        # self.assertEqual(self.number, 20, msg='Your input is not 20')

    @unittest.skip('暂时跳过用例3的测试')
    def test_case3(self):
        print('开始执行test_case3')
        # self.number
        # self.assertEqual(self.number, 30, msg='Your input is not 30')

    # 7.定义tearDown()方法用于测试用例执行之后的善后工作。
    # 注意，方法的入参为self

    @classmethod
    def tearDownClass(cls) -> None:
        print('正在进行测试收尾工作...')
        cls.driver.close()
        cls.driver.quit()

# 8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    # 8.1执行测试用例方案一如下：
    # unittest.main()方法会搜索该模块下所有以test开头的测试用例方法，并自动执行它们。
    # 执行顺序是命名顺序：先执行test_case1，再执行test_case2
    unittest.main()

'''
#8.2执行测试用例方案二如下：
#8.2.1先构造测试集
#8.2.1.1实例化测试套件
    suite=unittest.TestSuite()
#8.2.1.2将测试用例加载到测试套件中。
#执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    suite.addTest(Test('test_case2'))
    suite.addTest(Test('test_case1'))
#8.2.2执行测试用例
#8.2.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(suite)
'''

'''
#8.3执行测试用例方案三如下：
#8.3.1构造测试集（简化了方案二中先要创建测试套件然后再依次加载测试用例）
#执行顺序同方案一：执行顺序是命名顺序：先执行test_case1，再执行test_case2
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#8.3.2执行测试用例
#8.3.2.1实例化TextTestRunner类
    runner=unittest.TextTestRunner()
#8.3.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)   
'''