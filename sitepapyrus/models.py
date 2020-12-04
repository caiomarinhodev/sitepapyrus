# coding=utf-8
from __future__ import unicode_literals

from base64 import b64encode

import pyimgur
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Item(TimeStamped):
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    titulo = models.CharField(max_length=300, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    foto_arquivo = models.FileField(blank=True, null=True)
    foto_url = models.URLField(blank=True, null=True, default='https://placehold.it/300x300')

    def save(self, *args, **kwargs):
        try:
            CLIENT_ID = "cdadf801dc167ab"
            bencode = b64encode(self.foto_arquivo.read())
            client = pyimgur.Imgur(CLIENT_ID)
            r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': bencode})
            file = r['link']
            self.foto_url = file
        except (Exception,):
            pass
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return u'%s' % (self.titulo)

    def __unicode__(self):
        return u'%s' % (self.titulo)


class Mensagem(TimeStamped):
    class Meta:
        verbose_name = u'Mensagem'
        verbose_name_plural = u'Mensagens'

    nome = models.CharField(max_length=300, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    whatsapp = models.CharField(max_length=300, blank=True, null=True)
    mensagem = models.TextField(blank=True, )

    def __unicode__(self):
        return u'%s' % self.id

    def __str__(self):
        return u'%s' % self.id
