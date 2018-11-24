# import time
#
# from selenium import webdriver
#
# driver = webdriver.Firefox()
# driver.get("http://www.yhd.com/")
#
# time.sleep(20)
# print(driver.get_cookies())
#
# driver.quit()
import time

g_time = ""

class A:

    def a_hello(self):
        time_name = time.strftime("%y-%m-%d_%H_%M_%S")
        global g_time
        g_time = time_name
        time.sleep(1)
        print(time_name)

class B:

    def b_hello(self):
        # time_name = time.strftime("%y-%m-%d_%H_%M_%S")
        time.sleep(1)
        print(g_time)


B().b_hello()
A().a_hello()


