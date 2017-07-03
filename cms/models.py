#coding: utf-8
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.safestring import mark_safe

fs = FileSystemStorage(location='/media')

class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='documents/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % (self.photo.url))

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
    def __unicode__(self):
    	return self.nome