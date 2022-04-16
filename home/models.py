from django.db import models


class Ticket(models.Model):
    content = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    has_purchased = models.BooleanField(default=False, help_text="是否已经购买")
    gmt_purchased = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0, help_text="奖金金额")
    got_lottery = models.BooleanField(default=False, help_text="是否中奖")



class Settings(models.Model):
    config_key = models.CharField(max_length=50)
    config_value = models.CharField(max_length=200)