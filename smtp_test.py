#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# -*- coding : utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.protonmail.com"
mail_user="whoayou"
mail_pass="1qaz2wsx!@#"
 
 
sender = 'whoayou@protonmail.com'
receivers = ['1183617450@qq.com']
 
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("测试邮件", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
 
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
	smtpObj = smtplib.SMTP() 
	smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
	smtpObj.login(mail_user,mail_pass)  
	smtpObj.sendmail(sender, receivers, message.as_string())
	print ("success! 发送成功")
except smtplib.SMTPException:
	print ("Error! 无法发送邮件")
