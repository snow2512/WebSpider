import urllib.request
#构建response类的实例response
response = urllib.request.urlopen('https://www.baidu.com')

#查看response类的类型
print(type(response))

#调用response类方法。read()来获取网页内容
#print(response.read().decode('utf-8'))

#打印状态码
print(response.status)

#打印响应的头信息
print(response.getheaders())
# response.getheaders()返回对象是一个列表：[('Server', 'nginx'), ('Content-Type', 'text/html; charset=utf-8'), ('X-Frame-Options', 'SAMEORIGIN'),   
#     ('X-Clacks-Overhead', 'GNU Terry Pratchett'), ('Content-Length', '47397'), ('Accept-Ranges', 'bytes'),   
#     ('Date', 'Mon, 01 Aug 2016 09:57:31 GMT'), ('Via', '1.1 varnish'), ('Age', '2473'), ('Connection', 'close'),   
#     ('X-Served-By', 'cache-lcy1125-LCY'), ('X-Cache', 'HIT'), ('X-Cache-Hits', '23'), ('Vary', 'Cookie'),   
#     ('Strict-Transport-Security', 'max-age=63072000; includeSubDomains')] 
#提取列表中服务器的信息
print(response.getheader('Server'))

#
