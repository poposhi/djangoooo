#-*- coding: UTF-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.
class Music(models.Model):
    song = models.TextField(default="song")  # use models.{type_name}Field  tio build  a form
    singer = models.TextField(default="AKB48")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"

class Post(models.Model):
    Vavg = models.FloatField(default=64)  #這個資料是長度200的char
    name = models.CharField(max_length=200)
    body = models.TextField(default="default_value")
    pub_date = models.DateTimeField(default=timezone.now)
    # last_modify_date = models.DateTimeField(auto_now=True) #最後更改日期
    # created = models.DateTimeField(auto_now_add=True) #創造時間

    class Meta: #參考值 除了表格之外的設定
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
#資料庫做完要migrate