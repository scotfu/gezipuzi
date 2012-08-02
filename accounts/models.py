#coding=utf8

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    nickname=models.CharField(max_length=30)
    user_type=models.SmallIntegerField(default=1)
    #avatar=models.ImageField()    
    
    def __unicode__(self):
        return self.nickname

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)

