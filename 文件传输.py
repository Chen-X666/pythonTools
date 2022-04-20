!/usr/bin/env python
# coding: utf-8

# 1、建立连接
# 2、客户端client向服务器server请求123.txt文件，客户端open（123.txt）
# 3、编号
# 4、超时重传。用计时器，自己写重传
# 

# 所需接口
# seq = num.to_bytes序号发送 
# 整型转化为字节类型
# int.to_bytes(length,byteorder)
# int.from_bytes(length,byteorder)
# byteorder:little OR big

# In[14]:


a = 10
seq = a.to_bytes(8,"little")#转化为8字节，客户端与服务器要一致
print(seq)
print(type(seq))
f = open("123.txt","rb")#rb以二进制读模式打开
data = f.read(1024)
msg =seq + data


# In[ ]:


msg[0:8]


# In[ ]:


c = int.from_bytes(msg[0:4],"litlle")
print(c)
print(type(c))


# 设置超时：socket.sttimeout(value)
# 如果超时引发OSError

# In[3]:


from socket import*
client = socket(AF_INET,SOCK_STREAM)
client.settimeout(0.1)
count = 5
while count > 0:
    try:
        client.connect(("14.76.89.65",12345))
        flag = 1
        break
    except OSError:#打不通再拨
        print("cannot connect")
        count = count - 1
if flag == 1
while f.read(1024)#不停读1k的数据
    msg = seq + data 
    client.send(msg)
    while True:
        try:
            client.rev(1024)
            if seq == #确认编号
                break
            except:
                client.send(msg)
client.close()
f.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




