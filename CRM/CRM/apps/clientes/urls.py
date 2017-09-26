#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url 
from .views import *

urlpatterns = [	
	url(r'^$',login_view, name = 'vista_login'),
	url(r'^index/$',index_view , name = 'vista_index'),
	url(r'^logout/$',logout_view , name = 'vista_logout'),
	#### PACIENTES ####
	url(r'^registrar_paciente/$',registrar_paciente_view , name = 'vista_registrar_paciente'),
	url(r'^pacientes/page/(?P<pagina>.*)/$',pacientes_view, name = 'vista_pacientes'),
	url(r'^ver_paciente/(?P<id_paciente>.*)/$',ver_paciente_view, name = 'vista_paciente'),
	url(r'^editar_paciente/(?P<id_paciente>.*)/$',editar_paciente_view, name = 'vista_editar_paciente'),
	url(r'^eliminar_paciente/(?P<id_paciente>.*)/$',eliminar_paciente_view , name = 'vista_eliminar_paciente'),
	url(r'^confirmar_eliminar_paciente/(?P<id_paciente>.*)/$',confirmar_eliminar_paciente_view , name = 'vista_confirmar_eliminar_paciente'),
	#### INTERESADOS ####
	url(r'^registrar_interesado/$',registrar_interesado_view , name = 'vista_registrar_interesado'),
	url(r'^interesados/page/(?P<pagina>.*)/$',interesados_view, name = 'vista_interesados'),
	url(r'^ver_interesado/(?P<id_interesado>.*)/$',ver_interesado_view, name = 'vista_interesado'),
	url(r'^editar_interesado/(?P<id_interesado>.*)/$',editar_interesado_view, name = 'vista_editar_interesado'),
	url(r'^eliminar_interesado/(?P<id_interesado>.*)/$',eliminar_interesado_view , name = 'vista_eliminar_interesado'),
	url(r'^confirmar_eliminar_interesado/(?P<id_interesado>.*)/$',confirmar_eliminar_interesado_view , name = 'vista_confirmar_eliminar_interesado'),
	url(r'^interesado_a_paciente/(?P<id_interesado>.*)/$',interesado_a_paciente_view, name = 'vista_interesado_a_paciente'),
	### REPORTES ###
	url(r'^reporte_exel_pacientes/$',reporte_exel_pacientes_view, name = 'vista_reporte_exel_pacientes'),
	url(r'^reporte_exel_interesados/$',reporte_exel_interesados_view, name = 'vista_reporte_exel_interesados'),
	### USUARIOS ###
	url(r'^user/$',user_view, name = 'vista_user'),
	url(r'^edit_user/$',edit_user_view, name = 'vista_edit_user'),
	url(r'^edit_password/$',edit_password_view, name = 'vista_edit_password'),
	url(r'^password_guardado_user/$',password_guardado_user_view, name = 'vista_password_guardado_user'),

]