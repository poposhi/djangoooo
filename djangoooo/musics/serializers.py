#-*- coding: UTF-8 -*-
from rest_framework import serializers
from musics.models import Music

'''serializer from model import form struct and trans them to another form??'''


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created')
