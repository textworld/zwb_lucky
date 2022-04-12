import secrets
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import uuid
from celery import shared_task
from celery.utils.log import get_task_logger
from django.template.loader import render_to_string
from django.conf import settings

from .models import Ticket

logger = get_task_logger('schema')


def send_email_with_pic(lucky_str):
    report = render_to_string("email_template.html", context={
        "send_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "lucky_str": lucky_str
    })

    my_sender = settings.EMAIL_CONF.get("SENDER")
    receiver = settings.EMAIL_CONF.get("RECEIVER")
    password = settings.EMAIL_CONF.get("PASSWORD")

    logger.info('start to send mail from %s to %s', my_sender, receiver)

    msg = MIMEMultipart('related')
    msg['From'] = formataddr(["zwb", my_sender])
    # [收件人邮箱昵称、收件人邮箱账号], 昵称随便
    msg['To'] = formataddr(["zwb", "text.zwb@outlook.com"])
    # 邮件的主题，也就是邮件的标题
    msg['Subject'] = "lucky"
    msg.attach(MIMEText(report, 'html', 'utf-8'))

    server = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)

    # server.starttls()
    # Next, log in to the server nAvtxPiekkv6gn86
    server.login(my_sender, password)

    server.sendmail(my_sender, receiver, msg.as_string())
    server.quit()

    logger.info('sent a mail from %s to %s', my_sender, receiver)

@shared_task(bind=True)
def echo_hello(self):
  logger.info("hello")

@shared_task(bind=True)
def make_lucky(self, identity=None):
    if identity is None:
        identity = uuid.uuid4()
    lucky_map = {}
    for i in range(1000000):
        alphabet = [1, 9, 2, 11, 5, 21, 12, 19, 7, 3, 18, 30, 31, 32]
        nums = set()
        while len(nums) < 6:
            nums.add(secrets.choice(alphabet))
        num_list = list(nums)
        num_list.sort()
        lucky_str = ','.join([str(n) for n in num_list])

        tail = 100
        while tail > 16:
            tail = secrets.choice(alphabet)
        lucky_str = lucky_str + ',' + str(tail)
        if lucky_str not in lucky_map.keys():
            lucky_map[lucky_str] = 1
        else:
            lucky_map[lucky_str] = lucky_map[lucky_str] + 1
    max = 0
    max_lucky = ''
    for k in lucky_map.keys():
        if lucky_map[k] > max:
            max = lucky_map[k]
            max_lucky = k
    Ticket.objects.create(content=max_lucky, identity=identity)
    send_email_with_pic(max_lucky)

