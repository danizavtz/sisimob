#coding: utf-8
from django.db import models

class Imovel(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Imóvel"
        verbose_name_plural = "Imóveis"
    def __unicode__(self):
    	return self.nome