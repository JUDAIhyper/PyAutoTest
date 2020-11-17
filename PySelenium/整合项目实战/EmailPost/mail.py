from email.mime.multipart import MIMEMultipart
import smtplib
import os,time,datetime
from email.mime.text import MIMEText
from email.header import Header

#收件人
sender = ""
recevier = ""

#不用密码发送而是用授权码
auth_code = "JSQBKHTDERDCGXOH"
#主题
subject = "自动化测试报告"
#读取文件内容
f = open("PySelenium\\整合项目实战\\EmailPost\\result.html", "rb")
mail_body=f.read()
f.close()

#html形式的文件内容
html=MIMEText(mail_body,_subtype="html",_charset="utf-8")
html["Subject"]=subject
html["from"]=sender
html["to"]=recevier

#html附件 将测试报告放在附件中发送
att1=MIMEText(mail_body,"base64","gb2312")
att1["Content-Type"]="application/octet-stream"
att1["Content-Disposition"]='attachment; filename="TestReport.html"'

msg=MIMEMultipart()
msg["Subject"]="测试报告主题" #邮件标题
msg.attach(html)
msg.attach(att1)

#连接 登录 smtp服务器
smtp=smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login(sender,auth_code)

#发送邮件
smtp.sendmail(sender,recevier,msg.as_string())
smtp.quit()
