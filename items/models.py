#coding=utf8
from django.db import models
from puzi.models import Puzi

class Item(models.Model):
    name=models.CharField(max_length=256,null=True)
    puzi=models.ForeignKey(Puzi) 
   
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural=u'wuping'


