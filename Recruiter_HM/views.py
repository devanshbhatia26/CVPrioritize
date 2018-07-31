# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .forms import JobPostForm,LoginForm
from .models import JobPost,Profile
from django import forms
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


@login_required
def job_post(request):
    if request.method=="POST":
         form=JobPostForm(request.POST)
         if form.is_valid():
             tags=list(request.POST['primary_skills'])
             print(tags)
             for i in range(len(tags)):
                if(tags[i]==request.POST['secondary_skills']):
                    return render(request,'job_post.html',{'form':form,'messages':'You cant have same primary and secondary skills'})
             u=form.save(commit=False)
             u.created_timestamp=timezone.now()
             u.save()
             form.save_m2m()
    form=JobPostForm() 
    return render(request,'job_post.html',{'form':form})

def dashboard(request):
    if request.session.get('access')=='Hiring Manager':
        access=request.session.get('access')
        re_c = request.session.get('re_c')
        req_c = request.session.get('req_c')
        pub_c = request.session.get('pub_c')
        Recieved = request.session.get('Recieved')
        Requested = request.session.get('Requested')
        Published = request.session.get('Published')
        data_dict = {'re_c': re_c,'req_c':req_c,'pub_c':pub_c,'Received':Recieved,'Requested':Requested,'Published':Published,'access':access}
    else:
        access=request.session.get('access')
        re_c = request.session.get('re_c')
        req_c = request.session.get('req_c')
        pub_c = request.session.get('pub_c')
        Recieved = request.session.get('Recieved')
        Requested = request.session.get('Requested')
        Published = request.session.get('Published')
        data_dict = {'re_c': re_c,'req_c':req_c,'pub_c':pub_c,'Received':Recieved,'Requested':Requested,'Published':Published,'access':access}
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
                        jobs=JobPost.objects.all()
                        if jobs:
                            recieved_count=JobPost.objects.get(status=2).count()
                            requested_count=JobPost.objects.get(status=1).count()
                            published_count=JobPost.objects.get(status=3).count()
                            request.session['re_c'] = recieved_count
                            request.session['req_c'] = requested_count
                            request.session['pub_c'] = published_count
                            request.session['Recieved'] = 'Received'
                            request.session['Requested'] = 'Requested'
                            request.session['Published'] = 'Published'

                        else:
                            request.session['access']=access
                            request.session['re_c'] = 0
                            request.session['req_c'] =0
                            request.session['pub_c'] = 0
                            request.session['Recieved'] = 'Received'
                            request.session['Requested'] = 'Requested'
                            request.session['Published'] = 'Published'

                        return redirect("/portal/dashboard")

                    else:
                        access="Recruiter"
                        jobs=JobPost.objects.all()
                        if jobs:
                            pending_count=JobPost.objects.get(status=1).count()
                            sent_count=JobPost.objects.get(status=2).count()
                            published_count=JobPost.objects.get(status=3).count()
                            request.session['access']=access
                            request.session['re_c'] = pending_count
                            request.session['req_c'] = sent_count
                            request.session['pub_c'] = published_count
                            request.session['Recieved'] = 'Sent'
                            request.session['Requesteed'] = 'Pending'
                            request.session['Published'] = 'Published'
                        else:
                            request.session['access']=access
                            request.session['re_c'] = 0
                            request.session['req_c'] =0
                            request.session['pub_c'] = 0
                            request.session['Recieved'] = 'Sent'
                            request.session['Requested'] = 'Pending'
                            request.session['Published'] = 'Published'

                        return redirect("/portal/dashboard")
                else:
                    messages.error(request,'Incorrect Username or Password')
                    
        else:
            form=LoginForm()
            return render(request,'login.html',{'form':form})
