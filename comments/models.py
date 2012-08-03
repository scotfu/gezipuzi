#coding =utf-8
from django.db import models
from django.contrib.auth.models import User
from puzi.models import Puzi

class Comment(models.Model):

    title=models.CharField(max_length=30)
    content=models.TextField(max_length=512)
    create_time=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User)
    puzi=models.ForeignKey(Puzi)
    delete=models.SmallIntegerField(default=1)

    class Meta:
        verbose_name_plural=u'comments'

    def __unicode__(self):
        return self.title
