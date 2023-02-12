"""

目标：360图片数据

网址：https://image.so.com/i?q=python&src=&inact=0

需求：根据给定的关键字获取图片，获取3也数据
 分析： 该网站为动态加载数据
 数据为ajax数据
 资源地址：
https://image.so.com/j?callback=jQuery183010444334201530037_1675521258884&q=python&qtag=&pd=1&pn=60&correct=python&adstar=0&tab=all&sid=e298feb2879ddc77fe686779195d0631&ras=6&cn=0&gn=0&kn=13&crn=0&bxn=0&cuben=0&pornn=0&manun=34&src=&sn=73&ps=75&pc=75&_=16755212720
https://image.so.com/j?callback=jQuery183010444334201530037_1675521258884&q=python&qtag=&pd=1&pn=60&correct=python&adstar=0&tab=all&sid=e298feb2879ddc77fe686779195d0631&ras=6&cn=0&gn=0&kn=13&crn=0&bxn=0&cuben=0&pornn=0&manun=34&src=&sn=73&ps=75&pc=75&_=1675521272043

"""
import time
from queue import Queue
import threading

import requests
import pymysql

index=0
class Imgspider():
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='spiders')
        self.cursor = self.conn.cursor()
        self.url='https://image.so.com/j?'
        self.heardes={
            'authority': 'image.so.com',
            'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'cache-control': 'no-cache',
            # Requests sorts cookies= alphabetically
            # 'cookie': 'QiHooGUID=CEBF46694C364C8E3851B10314E1F903.1675581952147; __guid=16527278.3065186308674325000.1675581952151.9714; tracker=; __huid=11T6tyTojV82Skix%2BDprGWjOC7HTmXgOuGQGCZuLoZT0c%3D; gtHuid=1; opqopq=95c2316ff9fd75da97d42aab4616ad73.1675584728; _S=8368e69df573f29f7007895c83af8f18; test_cookie_enable=null; erules=p1-23%7Cecr-1%7Cp4-4%7Cp3-18%7Cp2-34',
            'pragma': 'no-cache',
            'referer': 'https://image.so.com/i?q=python&src=&inact=0',
            'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
            'x-requested-with': 'XMLHttpRequest',
        }

        self.json_queue=Queue()
        self.content_list_queue=Queue()

    def get_data(self):
        while True:
            for i in range(1,6):
                params = {
                    # 'callback': 'jQuery1830437844868981478_1675585030560',
                    'q': 'python',
                    'qtag': '',
                    'pd': '1',
                    'pn': '60',
                    'correct': 'python',
                    'adstar': '0',
                    'tab': 'all',
                    'sid': '8cafc902d9dea4216b354f5174945786',
                    'ras': '6',
                    'cn': '0',
                    'gn': '0',
                    'kn': '12',
                    'crn': '0',
                    'bxn': '0',
                    'cuben': '0',
                    'pornn': '0',
                    'manun': '34',
                    'src': '',
                    'sn': 72+((i-1)*26),
                    # 'ps': '1793',
                    # 'pc': '50',
                    # '_': '1675585051241',
                }
                # print(params['sn'])
                response=requests.get(self.url,headers=self.heardes,params=params)
                self.json_queue.put(response)

    def parse_data(self,data):
        while True:
            self.json_queue.get()
            datalist=data['list']
            # print(datalist)
            for node in datalist:
                item={}
                item['title']=node['title']
                item['img_url']=node['img']
                # self.save_data(item)
                print(item)
                self.content_list_queue.put(item)
            self.json_queue.task_done()

    def save_data(self,item):
       while True:

            self.content_list_queue.get()
            for node in item:
               print(node)

            sql='insert into bizhi(id, title, imgurl) values(%s, %s, %s)'
            try:
                self.cursor.execute(sql,(0, item['title'],item['img_url']))
                self.conn.commit()
                print('插入数据成功')
            except Exception as e:

                print("插入数据失败:{}".format(e))
                self.conn.rollback()
            self.content_list_queue.task_done()
    def main(self):

           # 存放线程
           thread_list = []
           #创建发送请求的线程  耗时任务
           for i  in range(3):
             t_parse=threading.Thread(target=self.get_data)
             thread_list.append(t_parse)
           #创建提取数据的线程
           t_content=threading.Thread(target=self.parse_data)
           thread_list.append(t_content)
           # #创建保存数据的线程
           t_save=threading.Thread(target=self.save_data)
           thread_list.append(t_save)
           # 启动 线程
           for t in  thread_list:
               #守护主线程
               t.daemon=True
               #启动线程
               t.start()
           index_threading=threading.currentThread()
            #当 队列任务为0是,主线程接受
           for i in [self.json_queue,self.content_list_queue]:
              if i is index_threading:
                  continue
              i.join() # 阻塞  等待技术为0


if __name__ == '__main__':

    t1=time.time()
    img=Imgspider()
    img.main()
    print('总耗时:',time.time()-t1)