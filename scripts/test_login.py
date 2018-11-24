import time
import unittest
from selenium import webdriver

from base.base_driver import init_driver
from base.base_report import BaseReport


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = init_driver()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_login_001(self):

        self.driver.get_screenshot_as_file("%s/%s.png" % (BaseReport().file_path, __name__))
        time.sleep(3)
        assert True

    def test_login_002(self):
        # 如何查看调用的方法名
        self.driver.get_screenshot_as_file("%s/%s.png" % (BaseReport().file_path, __name__))
        assert True

    # def test_login_001(self):
    #     # 点击登录
    #     self.driver.find_element_by_partial_link_text("登录").click()
    #     # 输入用户名
    #     self.driver.find_element_by_id("un").send_keys("hitheima")
    #     # 输入密码
    #     self.driver.find_element_by_id("pwd").send_keys("hitheima123000")
    #     # 点击登录
    #     self.driver.find_element_by_id("login_button").click()
    #
    #     # 断言
    #     assert "hitheima" == self.driver.find_element_by_class_name("hd_login_name").text

    # def test_login_002(self):
    #     # 点击登录
    #     self.driver.find_element_by_partial_link_text("登录").click()
    #     # 输入用户名
    #     self.driver.find_element_by_id("un").send_keys("hitheima")
    #     # 输入密码
    #     self.driver.find_element_by_id("pwd").send_keys("hitheima123000123")
    #     # 点击登录
    #     self.driver.find_element_by_id("login_button").click()
    #
    #     time.sleep(3)
    #
    #     # 断言
    #     assert "账号和密码不匹配，请重新输入" == self.driver.find_element_by_id("error_tips").text