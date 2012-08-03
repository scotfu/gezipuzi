#coding=utf8 
from django.db import models
from django.contrib.auth.models import User

class Puzi(models.Model):
    name=models.CharField(max_length=256,null=True)
    user=models.ForeignKey(User)
    logo=models.FileField(upload_to='logo', verbose_name='logo')
    address=models.CharField(max_length=256,blank=True)
    latitue=models.CharField(max_length=15,blank=True)
    longtitue=models.CharField(max_length=15,blank=True)
    phone=models.CharField(max_length=15,blank=True)
    mcc_type=models.CharField(max_length=25,blank=True)
    city=models.CharField(max_length=15,blank=True)
    openhour=models.CharField(max_length=15,blank=True)
    weibo=models.CharField(max_length=256,blank=True)
    create_time=models.DateTimeField(auto_now_add=True)
    last_modify=models.DateTimeField(auto_now=True)
    order_weight=models.DecimalField(max_digits=5, decimal_places=2,blank=True)
    like_count=models.IntegerField(max_length=10,blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural=u'铺子'

