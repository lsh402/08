import os
import time
import unittest
from base.base_report import BaseReport


if __name__ == '__main__':

    # 获取所有的要运行的方法（scripts文件夹下的所有继承TestCase的test开头的方法）
    suite = unittest.defaultTestLoader.discover("./scripts", "test_*.py")
    # 运行！
    BaseReport().run_suite_with_report(suite)
