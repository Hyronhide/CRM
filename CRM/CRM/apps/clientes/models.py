#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.conf import settings
import os

from django.db import models

TIPO =(
	('Paciente','Paciente'),
	('Interesado','Interesado'),
	)

GENERO =(
	('Masculino','Masculino'),
	('Femenino','Femenino'),
	)

SANGRE =(
	('A+','A+'),
	('B+','B+'),
	)

INTERES = (
	('5: Muy alto','5: Muy alto'),
	('4: Alto','4: Alto'),
	('3: Medio','3: Medio'),
	('2: Bajo','2: Bajo'),
	('1: Sin interes','1: Sin Interes'),
	)

class User_profile(models.Model):	

	user     = models.OneToOneField(User)	
	empresa  = models.CharField(max_length = 30)	
	
	def __unicode__(self):
		return "Nombre: %s %s; Usuario: %s" % (self.user.first_name, self.user.last_name, self.user.username)


class Persona(models.Model):

	nombres = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length = 50)
	cedula = models.CharField(max_length = 11,unique=True)
	correo = models.CharField(max_length = 50)
	movil = models.CharField(max_length = 30)	
	telefono = models.CharField(max_length = 30)	
	departamento = models.CharField(max_length = 30)
	ciudad = models.CharField(max_length = 30)	
	direccion = models.CharField(max_length = 50)
	empresa = models.CharField(max_length = 30, null=True)
	tipo = models.CharField(max_length = 30)
	
	#fecha = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return "%s %s"  % (self.nombres,self.apellidos) 

class Paciente(models.Model):	

	persona = models.OneToOneField(Persona)	
	genero = models.CharField(max_length = 10,choices = GENERO)
	grupo_sanguineo = models.CharField(max_length = 4,choices = SANGRE)
	fecha_nacimiento = models.DateField(auto_now=False)

	def __unicode__(self):
		return "%s %s"  % (self.persona.nombres,self.persona.apellidos) 

class Interesado(models.Model):	

	persona = models.OneToOneField(Persona)	
	procedencia = models.CharField(max_length = 50)
	nivel_interes = models.CharField(max_length = 30,choices = INTERES)
	

	def __unicode__(self):
		return "%s %s"  % (self.persona.nombres,self.persona.apellidos) 		