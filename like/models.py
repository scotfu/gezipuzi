#coding=utf8
from django.db import models
from items.models import Item
from django.contrib.auth.models import User

class Like(models.Model):
    item=models.ForeignKey(Item)
    user=models.ForeignKey(User)
    create_time=models.DateTimeField(auto_now_add=True)
    
    
    def __unicode__(self):
        return self.item.name+':'+self.user.username

    
    class Meta:
       verbose_name_plural=u'like'
