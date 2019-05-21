import os
from urllib import request
from urllib.parse import quote

#下载文件  @furl 下载地址，@fdir 保存本地路径，  @f_s_name 保存文件名
def urllib_download_file(furl,fdir,f_s_name):
    if not os.path.exists(fdir):
        os.makedirs(fdir)
    #处理url编码 访问请求出错
    rep_furl=quote(furl, safe='";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" | "$" | ","', encoding=None, errors=None)
    r = request.urlopen(rep_furl)
    save_file=fdir+'/'+f_s_name
    with open(save_file, 'wb') as f:
        f.write(r.read())  
    print('提示-保存成功：',save_file)
    return 1
