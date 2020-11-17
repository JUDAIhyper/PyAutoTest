import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送人
sender=""
#收件人
recevier=""

#不用密码发送而是用授权码
auth_code="JSQBKHTDERDCGXOH"
#主题
subject="自动化测试报告"

msg=MIMEText("<html><h2>使用python发送测试用例邮件</h2></html>",_subtype="html",_charset="utf-8")
msg["Subject"]=subject
msg["from"]=sender
msg["to"]=recevier

smtp=smtplib.SMTP()
smtp.connect("smtp.163.com")
smtp.login(sender,auth_code)
smtp.sendmail(sender,recevier,msg.as_string())
smtp.quit()