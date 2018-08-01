# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import JobPostForm,LoginForm
from .models import JobPost,Profile
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout





def Send_jobpost(request):
    if request.method=="POST":
        access=request.session.get('access')
        form=JobPostForm(request.POST)
        if form.is_valid():
            tags=list(request.POST['primary_skills'])
            print(tags)
            for i in range(len(tags)):
                if(tags[i]==request.POST['secondary_skills']):
                    return render(request,'job_post.html',{'form':form,'messages':'You cant have same primary and secondary skills'})
            u=form.save(commit=False)
            u.created_timestamp=timezone.now()
            u.status=1
            print u.status
            u.save()
            form.save_m2m()
            request.session['access']=access
            return redirect("/portal/dashboard")



def job_post(request):
    if request.method=="POST":
         access=request.session.get('access')
         form=JobPostForm(request.POST)
         if form.is_valid():
             tags=list(request.POST['primary_skills'])
             for i in range(len(tags)):
                if(tags[i]==request.POST['secondary_skills']):
                    return render(request,'job_post.html',{'form':form,'messages':'You cant have same primary and secondary skills'})
             u=form.save(commit=False)
             u.created_timestamp=timezone.now()
             u.status=1
             u.save()
             form.save_m2m()
             request.session['access']=access
             return redirect("/portal/dashboard")

             
    form=JobPostForm() 
    return render(request,'job_post.html',{'form':form})


def job_post_details(request,status):
    if(status==6):
        jobs=JobPost.objects.all()
    else:
        jobs=JobPost.objects.filter(status=status)
    return render(request,'job_post_list.html',{status:'status'})


def dashboard(request):
    jobs=JobPost.objects.all()
    if jobs:
        if request.session.get('access')=='Hiring Manager':
            access=request.session.get('access')
            try:
                recieved_count=JobPost.objects.filter(status=2).count()
            except JobPost.DoesNotExist:
                recieved_count=0
            try:
                requested_count=JobPost.objects.filter(status=1).count()
            except JobPost.DoesNotExist:
                requested_count=0
            
            try:
                published_count=JobPost.objects.filter(status=2).count()
            except JobPost.DoesNotExist:
                published_count=0


            data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Recieved','Requested':'Requested','Published':'Published','access':access}
            
        else:
             access=request.session.get('access')
             try:
                 recieved_count=JobPost.objects.filter(status=2).count()
             except JobPost.DoesNotExist:
                 recieved_count=0

             try:
                 requested_count=JobPost.objects.filter(status=1).count()
             except JobPost.DoesNotExist:
                 requested_count=0
             
             try:
                 published_count=JobPost.objects.filter(status=2).count()
             except JobPost.DoesNotExist:
                 published_count=0

             data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Sent','Requested':'Pending','Published':'Published','access':access}
        return render(request,'firstpage.html',data_dict)
    
    else:

        if request.session.get('access')=='Hiring Manager':
            access=request.session.get('access')
            recieved_count=0
            requested_count=0
            published_count=0
            data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Recieved','Requested':'Requested','Published':'Published','access':access}
    
        else:
            access=request.session.get('access')
            recieved_count=0
            requested_count=0
            published_count=0
            data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Sent','Requested':'Pending','Published':'Published','access':access}
        return render(request,'firstpage.html',data_dict)



def signin(request):
        if(request.method=="POST"):
            form=LoginForm(request.POST)
            if form.is_valid():
                AID=form.cleaned_data['AID']
                password=form.cleaned_data['Password']
                u=Profile.objects.get(AID=AID)
                print u.user
                username=str(u.user)
                users=authenticate(request,username=username,password=password)
                if users is not None:
                    login(request,users)
                    if u.role=='Hiring Manager':
                        access="Hiring Manager"            
                        request.session['access'] = access                                
                        return redirect("/portal/dashboard")

                    else:
                        access="Recruiter"
                        request.session['access'] = access
                        return redirect("/portal/dashboard")
                else:
                    messages.error(request,'Incorrect Username or Password')
                    
        else:
            form=LoginForm()
            return render(request,'login.html',{'form':form})
