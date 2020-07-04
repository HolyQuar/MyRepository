"""
--序列化对象使用pickle包
--wb-二进制写出
import cPickle as pickle
d = {url='index.html',title='主题',content='主页'}
pickle.dumps(d)
"""
#encoding=utf-8
import pickle
# 使用pickle写入
d = dict(url='index.html',title='主题',content='主页')
#使用dump方法--将序列化的对象直接写入文件
f = open('D:/Pycharm/Workspace/123/test1.txt','wb')
pickle.dump(d,f)
f.close()

import struct

# 读取二进制写入的数据--读取之后需要将二进制进行解码
with open('D:/Pycharm/Workspace/123/test1.txt', 'rb') as f:
    for line in f.readlines():
        data = line.strip()
        print(data.decode('utf8','ignore'))
