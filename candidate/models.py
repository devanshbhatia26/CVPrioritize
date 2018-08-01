# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator
from Recruiter_HM.models import JobPost

EXPERIENCE_CHOICES = (
    ('1-3','1-3'),
    ('3-6','3-6'),
    ('6-9','6-9'),
    ('9-12','9-12'),
    ('12-15','12-15')
)

class Candidate(models.Model):
    name= models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    email= models.EmailField()
    address= models.TextField(max_length=100, validators=[MinLengthValidator(3)])
    pincode = models.IntegerField()
    experience = models.CharField(max_length=6, choices=EXPERIENCE_CHOICES, default='1-3')
    phone= models.IntegerField()
    cv_path = models.FileField()
    created_timestamp = models.DateField()

class Application(models.Model):
    candidateid= models.ForeignKey(Candidate, on_delete=models.CASCADE)
    jobid = models.ForeignKey(JobPost)
    score = models.IntegerField()