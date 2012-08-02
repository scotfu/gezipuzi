#coding=utf8
from django.db import models
from puzi.models import Puzi
from django.contrib.auth.models import User

class Like(models.Model):
    puzi=models.ForeignKey(Puzi)
    user=models.ForeignKey(User)
    create_time=models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.puzi.name+':'+self.user.username
    
    class Meta:
       verbose_name_plural=u'like'
