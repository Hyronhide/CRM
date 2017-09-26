#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User 
from CRM.apps.clientes.models import *

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

class Login_form(forms.Form):

	usuario = forms.CharField(label="Cedula",widget = forms.TextInput())	
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))	

class Register_Persona_Form(forms.ModelForm):

	class Meta:
		model = Persona
		fields = '__all__'
		exclude = ['empresa','tipo']
	
	nombres = forms.CharField(label="Nombres",widget=forms.TextInput())
	apellidos = forms.CharField(label="Apellidos",widget=forms.TextInput())
	cedula = forms.CharField(label="Cedula",widget=forms.TextInput())
	correo  = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput())
	movil = forms.CharField(label="Movil",widget=forms.TextInput())
	telefono = forms.CharField(label="Teléfono",widget=forms.TextInput())
	departamento = forms.CharField(label="Departamento",widget=forms.TextInput())
	ciudad = forms.CharField(label="Ciudad",widget=forms.TextInput())
	direccion = forms.CharField(label="Direccion",widget=forms.TextInput())


class Register_Persona_Paciente_Form(forms.ModelForm):

	class Meta:
		model = Paciente
		fields = ['genero','grupo_sanguineo','fecha_nacimiento']	
		
	#grupo_sanguineo = forms.CharField(label="Grupo Sanguineo",widget=forms.TextInput())	
	fecha_nacimiento = forms.CharField(label="Fecha de nacimiento",widget=forms.DateInput())

class Register_Persona_Interesado_Form(forms.ModelForm):

	class Meta:
		model = Interesado
		fields = ['procedencia','nivel_interes']	
		
	procedencia = forms.CharField(label="Procedencia",widget=forms.TextInput())	
	#nivel_interes = forms.CharField(label="Nivel de interes",widget=forms.TextInput())
	#

class Interesado_Form(forms.ModelForm):

	class Meta:
		model = Interesado
		fields = ['nivel_interes']			
		
	#nivel_interes = forms.CharField(label="Nivel de interes",widget=forms.TextInput())						

class Interesado_a_Paciente_Form(forms.ModelForm):

	class Meta:
		model = Persona
		fields = ['tipo']	

class UserForm(forms.ModelForm):	

	first_name = forms.CharField(label="Nombres",widget=forms.TextInput())
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())
	#telefono = forms.CharField(label="Telefono",widget=forms.TextInput())	
	#password = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = User
		fields = ['first_name','last_name','email']	
		
'''
class User_profile_Form(forms.ModelForm):
	class Meta:
		model = User_profile
		fields = '__all__'	

	telefono = forms.CharField(label="Teléfono",widget=forms.TextInput())
'''
class PasswordForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['password']

	password = forms.CharField(label="Nuevo Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))	
		
	
	def clean_password_two(self):
		password = self.cleaned_data['password']			
		password_two = self.cleaned_data['password_two']

		if password == password_two:	
			pass 
		else:
			raise forms.ValidationError('Password no coinciden')				