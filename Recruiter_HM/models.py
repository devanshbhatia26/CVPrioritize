# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.validators import MinLengthValidator


EXPERIENCE_CHOICES = (
    ('1-3','1-3'),
    ('3-6','3-6'),
    ('6-9','6-9'),
    ('9-12','9-12'),
    ('12-15','12-15')
)
class JobPost(models.Model):
    title= models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    responsibilities = models.TextField(max_length=2000,validators=[MinLengthValidator(30)])
    qualification = models.TextField(max_length=2000,validators=[MinLengthValidator(30)])
    overall_experience = models.CharField(max_length=6, choices=EXPERIENCE_CHOICES, default='1-3')
    primary_skills=TaggableManager(help_text='comma separted tags')
    secondary_skills=models.CharField(max_length=8,blank=True,validators=[MinLengthValidator(1)])
    tertiary_skills=models.CharField(max_length=8,blank=True,validators=[MinLengthValidator(1)])
    status=models.IntegerField()
    created_timestamp=models.DateTimeField()
    updated_timestamp=models.DateTimeField(null=True, blank=True)
    deleted_timestamp=models.DateTimeField(null=True, blank=True)
    


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    AID=models.CharField(max_length=7,validators=[MinLengthValidator(7)])
    role=models.CharField(max_length=17,validators=[MinLengthValidator(9)])
    updated_timestamp=models.DateTimeField(null=True, blank=True)





    



