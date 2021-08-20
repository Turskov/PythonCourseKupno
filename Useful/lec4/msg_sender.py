from smtplib import SMTP_SSL
from email.mime.text import MIMEText


def send(message):
    user = 'python.course@mail.ru'

    server = SMTP_SSL('smtp.mail.ru', 465)
    server.login(user, 'CVul9R2wTuFbdgomGjGK')
    targets = ['orlov.soft.company@gmail.com']

    msg = MIMEText(message)
    msg['Subject'] = 'Приветствие'
    msg['From'] = user
    msg['To'] = ', '.join(targets)

    server.sendmail(user, targets, msg.as_string())
    server.quit()


send("Пламенный привет")
