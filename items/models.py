#coding=utf8
from django.db import models
from puzi.models import Puzi

class Item(models.Model):
    name=models.CharField(max_length=256,null=True)
    puzi=models.ForeignKey(Puzi) 
    detail=models.CharField(max_length=256,null=True)
    create_time=models.DateTimeField(auto_now_add=True)
    last_modify=models.DateTImeField(auto_now=True)
   #image=models.ImageField()
 
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural=u'wuping'


