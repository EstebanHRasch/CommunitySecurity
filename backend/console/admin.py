# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Camera, Footage, access_instance
#admin.site.register(Question)
admin.site.register(Camera)
admin.site.register(Footage)
admin.site.register(access_instance)
# Register your models here.
