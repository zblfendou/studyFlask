# 1.将python内置模块导入
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 2.构建邮件内容
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')  # 邮件正文
msg['From'] = formataddr(["my", "zhangbinlei2023@126.com"])  # 发件人
msg['to'] = 'zhangbinlei@xinnet.com'  # 收件人
msg['subject'] = '360 days'  # 邮件主题

# 3.连接发送邮件
server = smtplib.SMTP('smtp.126.com', 25)  # 发件人邮箱中的SMTP服务器，端口是25
server.login("zhangbinlei2023@126.com", "RBemgPeqbNshKzgL")  # 发件人邮箱账号密码
server.sendmail('zhangbinlei2023@126.com', 'zhangbinlei@xinnet.com', msg.as_string())  # 发送邮件
server.quit()

if __name__ == '__main__':
    print('发送成功')
