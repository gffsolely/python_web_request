from urllib import request
import re
import time
import filehandle1

# 获取页面内容
def get_html_page(curl):
    html_str=''
    try:
        #如果需要模拟浏览器请求，则需要在请求时加入headers
        #headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        #    'Accept-Encoding':'gzip, deflate',
        #    'Accept-Language':'zh-CN,zh;q=0.9',
        #    'Cache-Control':'max-age=0',
        #    'Connection':'keep-alive',
        #    'Cookie':'__51cke__=; ASPSESSIONIDQSSQDBBT=EJDBCGOAFDBNGKEHNLAKOAKG; __51laig__=36',
        #    'Host':'www.tingshulou.com',
        #    'Upgrade-Insecure-Requests':'1',
        #    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        #url_req=request.Request(curl,None,headers=headers)

        #正常请求
        url_resp=request.urlopen(curl,timeout=10)
        html_str=url_resp.read().decode('gbk')
    except Exception as err:
        print('打印异常：',err)

    return html_str;
def get_resurl_byhtml(cstr):
    #使用正则表达式从html文本中找到需要的片段
    s_rem=re.search( r'<a class="dlink" title="1号线路" href="(.*?)" target="_blank">本地1线</a>', cstr, re.M|re.I)
    s_resurl=''
    if s_rem and len(s_rem.groups())>=1 :
        s_resurl=s_rem.group(1)
    return s_resurl

def req_main():
    #根据页面规律来循环请求页面，例如 这里的页面是从1.html到497.html
    for num in range(1,497):  
        print('提示：执行位置：'+str(num)+' / 497')
        time.sleep(1)
        html_str =get_html_page("http://www.tingshulou.com/down/?92-"+str(num)+".html")
        #根据通用关键文本 判断页面是否为空
        if  len(html_str.strip())>0 and html_str.index('斗罗大陆有声小说')>0 :
            html_str1=html_str1.replace('\r\n','').replace('\n','').replace('\r','')
            p_s_resurl=get_resurl_byhtml(html_str)
            #指定要保存的文件名称
            p_s_name="douluo1-"+str(num+1)+".mp3" 
            if __name__ == "__main__":
                filehandle1.urllib_download_file(p_s_resurl,'D:/data/douluo1/',p_s_name)
        else:
            print('提示：空页面：'+str(num)+".html")
    print('打印log：全部执行完毕')
    return 1
# 开始执行
req_main()