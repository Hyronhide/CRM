from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from CRM.apps.historial.forms import *
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User ##
from CRM.apps.clientes.models import *
from CRM.apps.historial.models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage#paginator
from django.http.response import HttpResponse
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from openpyxl import Workbook
from django.conf import settings
from django.core.files import File
import os 

# Create your views here.
