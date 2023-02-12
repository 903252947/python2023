import requests

# cookies = {
#     'cna': 't7BuHGnj5ToCASQ/zGBrH/nz',
#     '_m_h5_tk': 'c367ac3026d702ccfa9a7788f57268d7_1676142767577',
#     '_m_h5_tk_enc': '1372db560d3ff194c6e55f961000248b',
#     'xlly_s': '1',
#     '_samesite_flag_': 'true',
#     'cookie2': '189ba169c1d413916faf98dcdba7be78',
#     't': '95873057ee44a964c252d0d21a20a363',
#     '_tb_token_': '7f8ef3a7b4e65',
#     'sgcookie': 'E1007CH1U87tDg%2FwaBy5d%2Bd30mxcZr0jqve37QvhwQ9Zh4847sQyvZbCj2Ou17dK%2Bsj37fzIY2P6uX6BEYW0IRBfERSvP3MgUYYn3C6e%2FsRRBsQ%3D',
#     'unb': '817314576',
#     'uc3': 'lg2=URm48syIIVrSKA%3D%3D&vt3=F8dCvj0pvjaOJ%2BnI5qI%3D&nk2=EFYx0ohCb0KoirznlpY%3D&id2=W8g0yuX%2FlINE',
#     'csg': '3c5808c9',
#     'lgc': 'sheng903252947',
#     'cancelledSubSites': 'empty',
#     'cookie17': 'W8g0yuX%2FlINE',
#     'dnk': 'sheng903252947',
#     'skt': '3b4da7fa2fe86225',
#     'existShop': 'MTY3NjEzMzA5Ng%3D%3D',
#     'uc4': 'id4=0%40WeuT%2FdQYuzCog%2BGwquha8MsY%2BC8%3D&nk4=0%40Eo9P%2Bv5cpcEu8CCEw1vsXC3o5fR9r%2B3b%2FA%3D%3D',
#     'publishItemObj': 'Ng%3D%3D',
#     'tracknick': 'sheng903252947',
#     '_cc_': 'VFC%2FuZ9ajQ%3D%3D',
#     '_l_g_': 'Ug%3D%3D',
#     'sg': '76d',
#     '_nk_': 'sheng903252947',
#     'cookie1': 'Vqh0l8%2B6mWNN4wPhR%2BZ7lt6SUwMvMQq4NOSyaWgCA4A%3D',
#     'mt': 'ci=127_1',
#     'thw': 'cn',
#     'uc1': 'cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0&cookie21=UIHiLt3xSift4ZS1K%2FrTYQ%3D%3D&existShop=false&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie14=UoezSc5PZyD0oQ%3D%3D',
#     'JSESSIONID': 'B5C871A5ED6DB6FD855BAC745E28CB6A',
#     'alitrackid': 'www.taobao.com',
#     'lastalitrackid': 'www.taobao.com',
#     'l': 'fBro0YKqT8DCFmywBO5alurza77OCIdb8sPzaNbMiIEGa1lhtMvhYNCeq0peSdtjgT54MetPDzejAdEk77aLRxgKqelyRs5mpbpw8eM3N7AN.',
#     'tfstk': 'cxeGB7GuJ5l6ai6YRPM1E-mXT3CRafpqr-PzLMNa2pAja1wEbsAkTQ8ZzMmAPNRf.',
#     'isg': 'BGRk0OfB2zA5Qi_87M05UnXmNWJW_Yhnl_UioX6EHS8YKQXzpg7A9znP6YEx8cC_',
# }
# with open('file.json')as f:
#     cookies=f.read()
# print(cookies)

cookies1= open('file.json').read()
cookies={item.split('=')[0]: item.split('=')[1] for item in cookies1.split('; ')}

print(cookies)
headers = {
    'authority': 's.taobao.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',

    # Requests sorts cookies= alphabetically
    # 'cookie': 'cna=t7BuHGnj5ToCASQ/zGBrH/nz; _m_h5_tk=c367ac3026d702ccfa9a7788f57268d7_1676142767577; _m_h5_tk_enc=1372db560d3ff194c6e55f961000248b; xlly_s=1; _samesite_flag_=true; cookie2=189ba169c1d413916faf98dcdba7be78; t=95873057ee44a964c252d0d21a20a363; _tb_token_=7f8ef3a7b4e65; sgcookie=E1007CH1U87tDg%2FwaBy5d%2Bd30mxcZr0jqve37QvhwQ9Zh4847sQyvZbCj2Ou17dK%2Bsj37fzIY2P6uX6BEYW0IRBfERSvP3MgUYYn3C6e%2FsRRBsQ%3D; unb=817314576; uc3=lg2=URm48syIIVrSKA%3D%3D&vt3=F8dCvj0pvjaOJ%2BnI5qI%3D&nk2=EFYx0ohCb0KoirznlpY%3D&id2=W8g0yuX%2FlINE; csg=3c5808c9; lgc=sheng903252947; cancelledSubSites=empty; cookie17=W8g0yuX%2FlINE; dnk=sheng903252947; skt=3b4da7fa2fe86225; existShop=MTY3NjEzMzA5Ng%3D%3D; uc4=id4=0%40WeuT%2FdQYuzCog%2BGwquha8MsY%2BC8%3D&nk4=0%40Eo9P%2Bv5cpcEu8CCEw1vsXC3o5fR9r%2B3b%2FA%3D%3D; publishItemObj=Ng%3D%3D; tracknick=sheng903252947; _cc_=VFC%2FuZ9ajQ%3D%3D; _l_g_=Ug%3D%3D; sg=76d; _nk_=sheng903252947; cookie1=Vqh0l8%2B6mWNN4wPhR%2BZ7lt6SUwMvMQq4NOSyaWgCA4A%3D; mt=ci=127_1; thw=cn; uc1=cookie15=V32FPkk%2Fw0dUvg%3D%3D&pas=0&cookie21=UIHiLt3xSift4ZS1K%2FrTYQ%3D%3D&existShop=false&cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie14=UoezSc5PZyD0oQ%3D%3D; JSESSIONID=B5C871A5ED6DB6FD855BAC745E28CB6A; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; l=fBro0YKqT8DCFmywBO5alurza77OCIdb8sPzaNbMiIEGa1lhtMvhYNCeq0peSdtjgT54MetPDzejAdEk77aLRxgKqelyRs5mpbpw8eM3N7AN.; tfstk=cxeGB7GuJ5l6ai6YRPM1E-mXT3CRafpqr-PzLMNa2pAja1wEbsAkTQ8ZzMmAPNRf.; isg=BGRk0OfB2zA5Qi_87M05UnXmNWJW_Yhnl_UioX6EHS8YKQXzpg7A9znP6YEx8cC_',
    'pragma': 'no-cache',
    'referer': 'https://s.taobao.com/search?q=python&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.jianhua.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
}
# 页面分析 看控制页数有data-vale sn  当data-vale=1 sn=44 为第一页
params = {
    'data-key': 's',
    'data-value': '1',
    'ajax': 'true',
    '_ksTS': '1676133203406_796',
    # 'callback': 'jsonp797',
    'q': 'python',
    'commend': 'all',
    'ssid': 's5-e',
    'search_type': 'item',
    'sourceId': 'tb.index',
    'spm': 'a21bo.jianhua.201856-taobao-item.2',
    'ie': 'utf8',
    'initiative_id': 'tbindexz_20170306',
    'bcoffset': '1',
    'ntoffset': '7',
    'p4ppushleft': '2,48',
    'sn':'44'
}

response = requests.get('https://s.taobao.com/search', params=params,cookies=cookies,headers=headers)
for  data  in  response.json()['mods']['itemlist']['data']['auctions']:
    print(data['raw_title'],data['item_loc'],data['view_price'])
