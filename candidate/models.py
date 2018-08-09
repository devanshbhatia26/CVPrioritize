# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.core.validators import MinLengthValidator
from Recruiter_HM.models import JobPost
from django.utils import timezone
from os.path import splitext, basename
import os

EXPERIENCE_CHOICES = (
    ('0-2','0-2'),
    ('3-5','3-5'),
    ('6-8','6-8'),
    ('9-12','9-12'),
    ('13-15','13-15'),
    ('15+','15+')
)

class Candidate(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email= models.EmailField()
    address= models.TextField(max_length=100, validators=[MinLengthValidator(3)])
    pincode = models.IntegerField()
    experience = models.CharField(max_length=6, choices=EXPERIENCE_CHOICES, default='0-2')
    skills = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    phone= models.CharField(max_length=15, validators=[MinLengthValidator(10)])
    qualification = models.CharField(max_length=80, validators=[MinLengthValidator(3)])
    cv_path = models.FileField()
    created_timestamp = models.DateField()


class Application(models.Model):
    candidateid= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    jobid = models.ForeignKey(JobPost)
    score = models.FloatField()
    applied = models.BooleanField(default = False)

class UploadFileModel(models.Model):

    # def unique_file_path(self, instance, filename):
    #     instance.original_file_name = filename
    #     base, ext = splitext(filename)
    #     newname = "%s.%s" % (str(timezone.now()), ext)
    #     return os.path.join('resume/',newname)

    file = models.FileField(upload_to="resume/")

