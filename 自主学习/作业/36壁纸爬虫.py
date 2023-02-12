"""
目标：36壁纸

网址：https://www.3gbizhi.com/wallDM/index_2.html

需求：获取当前网址上3也壁纸数据

 思路：
     定义BzSpiseder类
      # 1 初始化获取资源地址和配置信息
      # 2获取数据 通过XPATH(from lxml import etree) Beautifulsuop
      # 3 解析数据
      # 4保存数据

"""
import os.path

import requests
from lxml import etree


class BzSpiders():

# 1 初始化获取资源地址和配置信息
   def __init__(self):

          self.url='https://www.3gbizhi.com/wallDM/index_{}.html'
          self.headers={
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36  '
             }
# 2获取数据 通过XPATH(from lxml import etree) Beautifulsuop
   def get_data(self,page):
          if page == 1:
                first_url='https://www.3gbizhi.com/wallDM/index.html'
                resonpse=requests.get(url=first_url)
                print(resonpse.url)
          else:
                resonpse = requests.get(self.url.format(page))

                print(resonpse.url)

          resonpse.encoding = "utf-8"
        # print(resonpse.text)
          return resonpse
# 3 解析数据
   def parse_date(self,data):
       html_data=etree.HTML(data.text)
       li_list=html_data.xpath('//div[@class="contlistw mtw"]/ul/li')
       for li in li_list:
          item={}
          item['src']=li.xpath('./a/img/@lazysrc')[0]
          item['title']=li.xpath('./a/img/@title')[0]
          self.save_date(item)


# 4保存数据
   def save_date(self,item):

       response=requests.get(item['src'])
       with open('360壁纸/'+item['title']+'-'+'.jpg','wb') as f:
           f.write(response.content)


  # 主函数
   def main(self):
       for page in range(1, 5):
             response=self.get_data(page)


             self.parse_date(response)


if __name__ == '__main__':
    if not os.path.exists("360壁纸"):
        os.mkdir('360壁纸')
    BZ=BzSpiders()
    BZ.main()