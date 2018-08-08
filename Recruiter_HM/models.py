# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.validators import MinLengthValidator


EXPERIENCE_CHOICES = (
    ('0-2','0-2'),
    ('3-5','3-5'),
    ('6-8','6-8'),
    ('9-12','9-12'),
    ('13-15','13-15'),
    ('15+','15+')
)

class JobPost(models.Model):
    title= models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    responsibilities = models.TextField(max_length=2000,validators=[MinLengthValidator(30)])
    mand_qualification = models.CharField(max_length=2000,validators = [MinLengthValidator(2)])
    opt_qualification = models.CharField(max_length=2000,null=True,blank=True,validators = [MinLengthValidator(2)])
    overall_experience = models.CharField(max_length=6, choices=EXPERIENCE_CHOICES, default='0-2')
    primary_skills=models.CharField(max_length=30,blank=True,validators=[MinLengthValidator(1)])
    secondary_skills=models.CharField(max_length=30,blank=True,validators=[MinLengthValidator(1)])
    tertiary_skills=models.CharField(max_length=30,blank=True,validators=[MinLengthValidator(1)])
    status=models.IntegerField()
    team= models.CharField(max_length=100,validators=[MinLengthValidator(3)])
    people=models.IntegerField()
    created_timestamp=models.DateTimeField(null=True,blank=True)
    updated_timestamp=models.DateTimeField(null=True, blank=True)
    deleted_timestamp=models.DateTimeField(null=True, blank=True)

    def __int__(self):
        return self.id
    


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    AID=models.CharField(max_length=7,validators=[MinLengthValidator(7)])
    role=models.CharField(max_length=17,validators=[MinLengthValidator(9)])
    updated_timestamp=models.DateTimeField(null=True, blank=True)





    



