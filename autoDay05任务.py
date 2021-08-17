# 自动刷抖音
import time
from appium import webdriver

server = "http://localhost:4723/wd/hub"  # Appium Server, 端口默认为4723
param = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "appPackage": "com.ss.android.ugc.aweme",
    "appActivity": "com.ss.android.ugc.aweme.splash.SplashActivity",
    "deviceName": "127.0.0.1∶62001"
}

driver = webdriver.Remote(server, param)  # 连接手机和APP


def getSize():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


x, y = getSize()

while True:
    driver.swipe(x * 0.5, y * 0.9, x * 0.5, y * 0.2)
    time.sleep(15)
