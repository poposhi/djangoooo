#-*- coding: UTF-8 -*-
#好奇怪喔為什麼是Import view的func
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views
from musics.views import hello_view #要記得Import  func in view
from musics.views import homepage
from musics.views import showpost
from musics.views import mplimage

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls), #^代表配對開始 &配對結束
    url(r'^api/', include(router.urls)),
    url(r'^hello/', hello_view),
    url(r'^$', homepage),
    url(r'^post/(\w+)$', showpost),
    url(r'mplimage.png', mplimage),
    #url(r'^admin/', include(admin.site.urls)),
]
