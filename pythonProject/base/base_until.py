import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseUntil(unittest.TestCase):
    def setUp(self) -> None:
        global driver

        # 设置 Chrome 测试版的路径
        chrome_path = "C:\\Program Files\\Google\\chrome-test\\chrome-win64\\chrome.exe"
        # 设置 Chrome 测试版的选项
        option = Options()
        # 设置 Chrome 测试版的路径
        option.binary_location = chrome_path
        # 初始化 WebDriver，指定 Chrome 测试版选项
        option.add_argument('--headless')
        # option.add_argument("--disable-gpu")  # 禁用GPU加速
        option.add_argument("--window-size=1920,1080")  # 设置窗口大小
        option.add_argument("--force-device-scale-factor=1")  # 设置设备缩放因子
        # 设置 webdriver.ChromeOptions 对象
        # 保持浏览器不关闭
        option.add_experimental_option("detach", True)

        option.add_experimental_option('prefs', {
            'download.default_directory': 'D:\\test_downlode\\',  # 设置下载路径
            'download.prompt_for_download': False,  # 禁止下载时弹出提示框
            'download.directory_upgrade': True  # 允许下载路径存在多个文件
        })
        # 初始化 WebDriver
        self.driver = webdriver.Chrome(options=option)
        # 最大化浏览器
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(10)
        # 打开测试页面
        self.driver.get("http://58.210.177.75:8088")

    def tearDown(self) -> None:
        self.driver.quit()