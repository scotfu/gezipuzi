#coding=utf8 
from django.db import models
from django.contrib.auth.models import User

class Puzi(models.Model):
    name=models.CharField(max_length=256,null=True)
    user=models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name_plural=u'铺子'

