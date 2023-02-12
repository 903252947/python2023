"""
此方法模拟登录，获取cookie
"""
import json
import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from ChromeDrive import  create_chrome_drive

from selenium.webdriver.support.ui import WebDriverWait

browser=create_chrome_drive()
browser.get('https://www.taobao.com/')
#隐藏等待
browser.implicitly_wait(10)
#获取页面元素模拟用户登录输入点击行为
login_href=browser.find_element(By.CSS_SELECTOR,'#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-sign > a.h').click()

username_input=browser.find_element(By.CSS_SELECTOR,'#fm-login-id')
username_input.send_keys('903252947@qq.com')
password_input=browser.find_element(By.CSS_SELECTOR,'#fm-login-password')
password_input.send_keys('shengzhigang1993')
login_button=browser.find_element(By.CSS_SELECTOR,'#login-form > div.fm-btn > button')
login_button.click()
#显示 等待
# locator=(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div[5]/div/div[1]/a/span/strong')
# WebDriverWait(browser,timeout=20,poll_frequency=0.5,ignored_exceptions=None).until((EC.presence_of_element_located(locator)))
time.sleep(10)


# 配合until()使用（等待元素可见）
# 5表示 最长超时时间，默认以秒为单位； 1表示检测的间隔步长，在等待期间，每隔一定时间(默认0.5秒)，调用until或until_not里的方法，直到它返回True或False.
# WebDriverWait(browser, 20,0.5).until(lambda el:browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[2]/div[5]/div/div[1]/a/span/strong'))

# 配合until_not()使用（等待元素不可见）
# WebDriverWait(browser, 5, 1).until_not(EC.visibility_of_element_located(By.LINK_TEXT,'sheng903252947'))

# 在类中封装为一个函数
# def wait_eleLocated(self, loc, timeout=30, poll_frequency=0.5, model=None):
#         """
#         :param loc:元素定位表达;元组类型,表达方式(元素定位类型,元素定位方法)，示例：(By.ID, "kw")
#         :param timeout:超时时间
#         :param poll_frequency:轮询频率
#         :param model:等待失败时,截图操作,图片文件中需要表达的功能标注
#         :return:None
#         """
#         self.logger.info(f'等待"{model}"元素,定位方式:{loc}')
#         try:
#             start = datetime.now()
#             WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
#             end = datetime.now()
#             self.logger.info(f'等待"{model}"时长:{end - start}')
#         except TimeoutException:
#             self.logger.exception(f'等待"{model}"元素失败,定位方式:{loc}')
#             # 截图
#             self.save_webImgs(f"等待元素[{model}]出现异常")
#             raise
#设置等待
# wait = WebDriverWait(browser,10,0.5)
#使用匿名函数
# wait.until(lambda diver:browser.find_element_by_id('kw'))

# 获取cookie 数据写入文件
with open('file.json','w')as file:
    json.dump(browser.get_cookies(),file)


