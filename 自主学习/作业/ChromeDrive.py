import json

from selenium import webdriver
'''
此方法用于创建chrome 对象，启动crome ,反爬
chromeoptions 是一个方便控制 chrome 启动时属性的类。

chromeoptions 功能：
（1）设置 chrome 二进制文件位置 (binary_location)
（2）添加启动参数 (add_argument)
（3）添加扩展应用 (add_extension, add_encoded_extension)
（4）添加实验性质的设置参数 (add_experimental_option)
（5）设置调试器地址 (debugger_address)

'''
def create_chrome_drive(*,headless=False):
    chrome_options=webdriver.ChromeOptions()
    if headless:
        #--headlessss是不显示浏览器启动执行车过程,浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
        chrome_options.add_argument('--headless')
        # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--incognito')  # 无痕模式

    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错

    chrome_options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false')# 不加载图片, 提升速度
    # 禁用浏览器弹窗
        # 设置lang和User-Agent信息，防止反爬虫检测
    chrome_options.add_argument('lang=zh_CN.utf-8')

        # user-agent用来模拟移动设备
    UserAgent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

    chrome_options.add_argument('User-Agent=' + UserAgent)



    #反爬
    # 设置开发者模式启动，该模式下webdriver属性为正常值  模拟真正浏览器
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # # 禁用浏览器弹窗
    # prefs = {
    #     'profile.default_content_setting_values': {
    #         'notifications': 2
    #     }
    # }
    # chrome_options.add_experimental_option('prefs', prefs)

    browser = webdriver.Chrome(chrome_options=chrome_options)

    #破解selenium 反爬
    browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                            {"source": """
                            Object.defineProperty(navigator, 'webdriver', {
                            get: () => undefined
                            })""" })

    # # 动态调整useragent
    # browser.execute_cdp_cmd('Network.setUserAgentOverride', {
    #                 "userAgent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    #                 "platform": "Windows"})
    return browser
def add_cookies(browser,cookie_file):
    '''
     向浏览器对象写入指定的cookie信息
    '''
    with open(cookie_file,'r')as file:
        cookie_list=json.load(file)
        for cookie_dic in cookie_list:
            if cookie_dic['secure']:
                browser.add_cookie(cookie_dic)



# browser.find_element(By.CSS_SELECTOR, '#fm-login-id').send_keys(number)# 添加账号

# browser.find_element(By.CSS_SELECTOR, '#fm-login-password').send_keys(password)# 添加密码


# options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" # 手动指定使用的浏览器位置


   # browser.set_window_size(1200, 800)         # 控制浏览器大小
    # browser.back()                           # 浏览器后退
    # browser.forward()                        # 浏览器前进

'''
middlewares中设置cookie
request.cookies={
'':'',
'':'',
}

  # 重载start_requests方法
  def start_requests(self):
    headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"}
    # 指定cookies
    cookies = {
          'uuid': '66a0f5e7546b4e068497.1542881406.1.0.0',
          '_lxsdk_cuid': '1673ae5bfd3c8-0ab24c91d32ccc8-143d7240-144000-1673ae5bfd4c8',
          '__mta': '222746148.1542881402495.1542881402495.1542881402495.1',
          'ci': '20',
          'rvct': '20%2C92%2C282%2C281%2C1',
          '_lx_utm': 'utm_source%3DBaidu%26utm_medium%3Dorganic',
          '_lxsdk_s': '1674f401e2a-d02-c7d-438%7C%7C35'}

        # 再次请求到详情页，并且声明回调函数callback，dont_filter=True 不进行域名过滤，meta给回调函数传递数据
    yield Request(detailUrl, headers=headers, cookies=cookies, callback=self.detail_parse, meta={'myItem': item}, dont_filter=True)
ROBOTSTXT_OBEY=False  #同时还要在setting中设置
'''




'''

 # chrome_options.add_argument("--proxy-server=http://" + ip_port)
#附赠添加代理方法
 
from selenium import webdriver
PROXY = "proxy_host:proxy:port"
options = webdriver.ChromeOptions()
desired_capabilities = options.to_capabilities()
desired_capabilities['proxy'] = {
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "noProxy":None,
    "proxyType":"MANUAL",
    "class":"org.openqa.selenium.Proxy",
    "autodetect":False
}
driver = webdriver.Chrome(desired_capabilities = desired_capabilities)
 
#指定driver地址
 
from selenium import webdriver

driver = webdriver.Chrome(executable_path='..drivers\chromedriver.exe')
#这个地方的executable_path，可以是一个相对路径或一个绝对路径
    

'''

'''
  
 
#image
 
#其他配置项目参数
 
# –user-data-dir=”[PATH]”
# 指定用户文件夹User Data路径，可以把书签这样的用户数据保存在系统分区以外的分区
 
　　–disk-cache-dir=”[PATH]“ 
# 指定缓存Cache路径
 
　　–disk-cache-size= 
# 指定Cache大小，单位Byte
 
　　–first run 
# 重置到初始状态，第一次运行
 
　　–incognito 
# 隐身模式启动
 
　　–disable-javascript 
# 禁用Javascript
 
　　--omnibox-popup-count="num" 
# 将地址栏弹出的提示菜单数量改为num个
 
　　--user-agent="xxxxxxxx" 
# 修改HTTP请求头部的Agent字符串，可以通过about:version页面查看修改效果
 
　　--disable-plugins 
# 禁止加载所有插件，可以增加速度。可以通过about:plugins页面查看效果
 
　　--disable-javascript 
# 禁用JavaScript，如果觉得速度慢在加上这个
 
　　--disable-java 
# 禁用java
 
　　--start-maximized 
# 启动就最大化
 
　　--no-sandbox 
# 取消沙盒模式
 
　　--single-process 
# 单进程运行
 
　　--process-per-tab 
# 每个标签使用单独进程
 
　　--process-per-site 
# 每个站点使用单独进程
 
　　--in-process-plugins 
# 插件不启用单独进程
 
　　--disable-popup-blocking 
# 禁用弹出拦截
 
　　--disable-plugins 
# 禁用插件
 
　　--disable-images 
# 禁用图像
 
　　--incognito 
# 启动进入隐身模式
 
　　--enable-udd-profiles 
# 启用账户切换菜单
 
　　--proxy-pac-url 
# 使用pac代理 [via 1/2]
 
　　--lang=zh-CN 
# 设置语言为简体中文
 
　　--disk-cache-dir 
# 自定义缓存目录
 
　　--disk-cache-size 
# 自定义缓存最大值（单位byte）
 
　　--media-cache-size 
# 自定义多媒体缓存最大值（单位byte）
 
　　--bookmark-menu 
# 在工具 栏增加一个书签按钮
 
　　--enable-sync 

# 启用书签同步

    '''