# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cliente(models.Model):
	DPI = models.IntegerFlied();
	Nombre = models.CharField(max_length=150)
	NIT = models.IntegerField();
	Correo = models.CharField(max_length=200)
	Telefono = models.IntegerField()
	id_Genero = models.IntegerField()
	Edad = models.IntegerField()
	id_Dep = models.IntegerField()
	Direccion = models.TextField(max_length=1000)
	id_tipoSangre = models.IntegerField()
	Sintomas = models.TextField(max_length=1000)
	Alergias = models.TextField(max_length=1000)
	Numero_As= models.IntegerField()
	Foto = models.TextField(max_length=5000)

	def __unicode__(self):
        return self.DPI
class Genero(models.Model):
	id_Genero = models.IntegerField()
	Genero = models.CharField(max_length=10)

	def __unicode__(self):
        return self.id_Genero
class Tipo_sangre(models.Model):
	id_tipoSangre = models.IntegerField()
	tipo_sangre = models.CharField(max_length=10)

	def __unicode__(self):
        return self.id_tipoSangre

class Aseguradora(models.Model):
	Numero_As = models.IntegerField()
	aseguradora = models.CharField(max_length=10)

	def __unicode__(self):
        return self.Numero_As

class Departamento(models.Model):
	id_Dep= models.IntegerField()
	departamento = models.CharField(max_length=10)

	def __unicode__(self):
        return self.id_Dep





