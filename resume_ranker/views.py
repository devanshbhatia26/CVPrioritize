# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import JobPostForm
from django import forms

def job_post(request):
    if request.method=="POST":
         form=JobPostForm(request.POST)
         if form.is_valid():
             tags=list(request.POST['primary_skills'])
             print(tags)
             for i in range(len(tags)):
                if(tags[i]==request.POST['secondary_skills']):
                    raise forms.ValidationError('You Cannot enter the same skills again')
             form.save()
    form=JobPostForm() 
    return render(request,'job_post.html',{'form':form})
