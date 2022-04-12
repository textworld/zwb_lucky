from django.db import models


class Ticket(models.Model):
    content = models.CharField(max_length=100)
    identity = models.CharField(max_length=100)
    has_purchased = models.BooleanField(default=False)
    gmt_purchased = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
