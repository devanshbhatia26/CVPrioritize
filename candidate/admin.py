# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Candidate, Application, UploadFileModel

admin.site.register(Candidate)
admin.site.register(Application)
admin.site.register(UploadFileModel)
