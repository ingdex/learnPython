#!/usr/bin/python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令:
from_addr = '871958943@qq.com'
password = 'rrtjpmjjybaobffc'
# 输入收件人地址:
to_addr = '871958943@qq.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.qq.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

try:
    server = smtplib.SMTP(smtp_server, 587) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    print ("sucess!")
except smtplib.SMTPException:
    print ("failed!")