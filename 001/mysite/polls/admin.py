#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/17 19:48:11.540743
#+ Editado:	2022/01/17 19:50:10.544351
# ------------------------------------------------------------------------------
from django.contrib import admin
from .models import Question, Choice
# ------------------------------------------------------------------------------
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
# ------------------------------------------------------------------------------
