# -*- coding: utf-8 -*-
"""
by: 老屋
"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE


class SendEmail:
    mailServer = 'smtp.qq.com'
    user_sender = 'num@qq.com'
    password = '*********'
    mail_recv = [user_sender]
    mail_cc = ['**@qq.com']
    port = 465

    def send(self, mail_subject, mail_content, mail_att=None):
        # 多部分邮件方法实例化
        mail = MIMEMultipart()
        mail['From'] = SendEmail.user_sender

        # 多个收件人处理
        mail['To'] = ','.join(SendEmail.mail_recv)
        mail['Cc'] = COMMASPACE.join(SendEmail.mail_cc)
        mail['Subject'] = mail_subject

        # 添加正文
        mail.attach(MIMEText(mail_content))
        print('to: ', mail['To'])

        # 添加附件
        if mail_att is not None:
            with open(mail_att, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(mail_att))
            part['Content-Disposition'] = 'attachment; filename=%s' %os.path.basename(mail_att)
            mail.attach(part)

        try:
            # qq邮箱服务器连接
            smtp = smtplib.SMTP_SSL(SendEmail.mailServer, SendEmail.port)
            # smtp.set_debuglevel(1)
            smtp.login(SendEmail.user_sender, SendEmail.password)
            print('-------sending mail')
            # mail.as_string把对象变成str
            smtp.sendmail(mail['From'], mail['To'].split(','), mail.as_string())
            smtp.quit()
            print('Success')
        except Exception as e:
            print('邮件发送失败，', e)


if __name__ == '__main__':
    mail_content = 'this is test for python, 准备好了吗？'
    mail_subject = 'hello'
    att = sys.argv[0]
    s = SendEmail()
    s.send(mail_subject, mail_content, mail_att=att)