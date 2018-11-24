import os
import time
from base.HTMLTestRunner import HTMLTestRunner


class BaseReport:

    __instance = None
    __is_init = False

    file_path = ""

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__is_init:
            return
        self.__is_init = True

        # 初始化
        time_name = time.strftime("%y-%m-%d_%H_%M_%S")
        BaseReport.file_path = "./report/%s" % time_name

    def run_suite_with_report(self, suite):
        # 判断某一个文件夹是否存在
        if not os.path.exists(self.file_path):
            # 创建和时间关联的文件夹
            os.mkdir(self.file_path)

        file_name = "%s/report.html" % self.file_path
        with open(file_name, "wb") as f:
            HTMLTestRunner(f, 2, "这是一号店的登录", "mac os 10.13").run(suite)