# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator
from Recruiter_HM.models import JobPost

class Candidate(models.Model):
    name= models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email= models.EmailField()
    address= models.TextField(max_length=100, validators=[MinLengthValidator(3)])
    pincode = models.IntegerField()
    experience = models.IntegerField()
    phone= models.IntegerField()
    cv_path = models.FileField()
    created_timestamp = models.DateField()

class Application(models.Model):
    candidateid= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    jobid = models.ForeignKey(JobPost)
    score = models.IntegerField()
