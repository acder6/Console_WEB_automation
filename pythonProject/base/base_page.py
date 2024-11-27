import os
import re

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    # 定位元素关键字
    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    # 定义值关键字
    def set_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    # 定义点击元素关键字
    def click(self,loc):
        self.locator_element(loc).click()

    def wait(self,loc):
        alert_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(loc)
        )
        return alert_element

    def wait_click(self,loc):
        alert_element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(loc)
        )
        return alert_element

    def clear(self,loc):
        self.locator_element(loc).clear()

    def get_value(self,loc):
        element = self.locator_element(loc)
        return element.text

    def get_number_value(self,loc):
        element = self.locator_element(loc)
        text = element.text
        numbers = re.findall(r'\d+', text)
        return numbers[0]

    def sx(self):
        self.driver.refresh()

    def get_bx_value(self,loc):
        element = self.locator_element(loc)
        input1 = element.get_attribute('value')

        return input1

    def gd_loc(self,loc):
        element = self.locator_element(loc)
        gd_element = self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return gd_element

    def clear_downlode_file(self,download_path, specific_filename):
        # 构建完整的文件路径
        specific_file_path = os.path.join(download_path, specific_filename)

        # 检查文件是否存在
        if os.path.isfile(specific_file_path):
            # 如果文件存在，则删除
            os.remove(specific_file_path)
            print(f"文件 {specific_filename} 已被删除。")
        else:
            # 如果文件不存在，打印消息
            print(f"文件 {specific_filename} 不存在，无需删除。")