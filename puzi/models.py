#coding=utf8 
from django.db import models
from django.contrib.auth.models import User

class Puzi(models.Model):
    name=models.CharField(max_length=256,null=True)
    user=models.ForeignKey(User)
    #logo=models.ImageField()
    address=models.CharField(max_length=256)
    latitue=models.CharField(max_length=15)
    longtitue=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    mcc_type=models.CharField(max_length=25)
    city=models.CharField(max_length=15)
    openhour=models.CharField(max_length=15)
    weibo=models.CharField(max_length=256)
    create_time=models.DateTimeField(auto_now_add=True)
    last_modify=models.DateTimeField(auto_now=True)
    order_weight=models.DecimalField(max_digits=5, decimal_places=2)
    like_count=models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural=u'铺子'

