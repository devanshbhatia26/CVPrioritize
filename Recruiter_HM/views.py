# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from candidate.models import Candidate,Application
from .forms import JobPostForm,LoginForm
from .models import JobPost,Profile
from django import forms
from itertools import chain
from django.utils import timezone
from taggit.models import Tag
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


@login_required
def show_jd(request,id):
    job=JobPost.objects.get(pk=id)
    job_status=JobPost.objects.get(pk=id)
    print(job_status.status)
    if(job_status.status == 3):
        main_list=job.application_set.filter(score__gt=77).filter()
        return render(request,'show_jd.html',{'main_list':main_list})

    else:
        return render(request,'show_jd.html',{'messages': 'This Job Post Has Been Closed'})

    



@login_required
def job_post(request):
    if request.method=="POST":
         access=request.session.get('access')
         form=JobPostForm(request.POST)
         if form.is_valid():
             tags= [i.lower().strip() for i in request.POST['primary_skills'].split(',')]
             sec_tags = [ i.lower().strip() for i in request.POST['secondary_skills'].split(',')]
             tert_tags = [ i.lower().strip() for i in request.POST['tertiary_skills'].split(',')]
             for i in range(len(tags)):
                if(tags[i] in sec_tags ):
                    return render(request,'job_post.html',{'form':form,'messages':'You cant have same primary and secondary skills'})
                    
                if(tags[i] in tert_tags):
                    return render(request,'job_post.html',{'form':form,'messages':'You cant have same primary and tertiary skills'})
             u=form.save(commit=False)
             u.created_timestamp=timezone.now()
             u.save()
             form.save_m2m()
             request.session['access']=access
             return redirect("/portal/dashboard")
         else:
             return render(request,'job_post.html',{'form':form,'messages':'The Minimum Length for title is 3 characters,for Qualification field is 30 characters and for responsibilities field is 30 characters'})

             
    form=JobPostForm() 
    return render(request,'job_post.html',{'form':form})



@login_required
def job_post_details(request):
    k1=''
    k2=''
    k3=''
    k4=''
    k5=''
    k6=''
    status=request.GET.get('status')
    stat = status.split(',')
    print(stat)
    stats=[]
    access=request.session.get('access')
    if len(stat)==1:
        for i in range(len(stat)):
            val=int(stat[i])
            stats.append(val)
    else:
        for i in range(len(stat)-1):
            val = int(stat[i])
            stats.append(val)
    print(stats)


    if(status == '6'):
        jobs=JobPost.objects.all()
    else:
        jobs=JobPost.objects.filter(status__in=stats)
        for i in range(len(stats)):
            if(stats[i] == 0):
                k1="checked"
            elif(stats[i] == 1):
                k2="checked"
            elif(stats[i] == 2):
                k3="checked"
            elif(stats[i] == 3):
                k4="checked"
            elif(stats[i] == 4):
                k5="checked"
            elif(stats[i] == 5):
                k6="checked"
        else:
            pass
        
    if access=="Hiring Manager":
        data_dict={'status':status,'access':access,'jobs':jobs,'Received':'Received','Requested':'Requested','k1':k1,'k2':k2,'k3':k3,'k4':k4,'k5':k5,'k6':k6}
    else:
        data_dict={'status':status,'access':access,'jobs':jobs,'Received':'Sent','Requested':'Pending','k2':k2,'k3':k3,'k4':k4,'k5':k5,'k6':k6}
    return render(request,'job_post_list.html',data_dict)
 



@login_required
def specific_post(request,id):
    access=request.session.get('access')
    u=JobPost.objects.get(id=id)
    return render(request,'specific_job_post.html',{'job':u,'access':access})




@login_required
def publish_jd(request,id):
    job=JobPost.objects.get(id=id)
    job.status=3
    job.save()
    return redirect("/portal/dashboard")




@login_required
def success_jd(request,id):
    job=JobPost.objects.get(id=id)
    job.status=4
    job.deleted_timestamp=timezone.now()
    job.save()
    return redirect("/portal/dashboard")



@login_required
def unsuccess_jd(request,id):
    job=JobPost.objects.get(id=id)
    job.status=5 
    job.deleted_timestamp=timezone.now()
    job.save()
    return redirect("/portal/dashboard")




def match():
    jm=JobPost.objects.all()
    data = serializers.serialize('json',jm)
    return data
     
  




@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("signin"))



@login_required
def edit_jd(request,id):
    access=request.session.get('access')
    if(request.method== "POST"):
        form=JobPostForm(request.POST)
        if form.is_valid():
            job=JobPost.objects.get(id=id)
            id=job.id
            
            create=job.created_timestamp
            job.delete()
            tags=list(request.POST['primary_skills'])
            for i in range(len(tags)):
                if(tags[i]==request.POST['secondary_skills']):
                    return render(request,'edit_jd.html',{'form':form,'messages':'You cant have same primary and secondary skills'})
            u=form.save(commit=False)
            u.id=id
            u.created_timestamp=create
            u.updated_timestamp=timezone.now()
            u.save()
            form.save_m2m()
            request.session['access']=access
            return redirect("/portal/dashboard")

        else:
            print(form.errors)
            return render(request,'edit_jd.html',{'form':form,'messages':'The Minimum Length for title is 3 characters,for Qualification field is 30 characters and for responsibilities field is 30 characters'})
        
    
    job=JobPost.objects.get(id=id)
    
    initial={'title':job.title,'responsibilities':job.responsibilities,'qualification':job.qualification,'additional_qualification':job.additional_qualification,'overall_experience': job.overall_experience,'primary_skills':job.primary_skills,'secondary_skills':job.secondary_skills,'tertiary_skills':job.tertiary_skills,'team':job.team,'people':job.people}
    form=JobPostForm(initial)
    return render(request,'edit_jd.html',{'form':form,'access':access,'id':id})





@login_required
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
                published_count=JobPost.objects.filter(status=3).count()
            except JobPost.DoesNotExist:
                published_count=0

            request.session['access'] = access
            specific=list(JobPost.objects.all().values_list('id'))
            specific=list(chain(*specific))
            print(specific)

            titles=list(JobPost.objects.all().values_list('title'))
            titles=list(chain(*titles))
            
            print(titles)
            categories = list() 
            succesful_closed = list()
            published = list()
            for ti in titles:
                categories.append(ti)  
            for spec in specific:
                try:
                    c=JobPost.objects.filter(id=spec).filter(status=3).count()
                    published.append(c)
                    

                except JobPost.DoesNotExist:
                    c=0
                    published.append(c)
            
                try:
                    c1=JobPost.objects.filter(id=spec).filter(status=4).count()
                    succesful_closed.append(c1)
                    

                except JobPost.DoesNotExist:
                    c1=0
                    succesful_closed.append(c1)  
              
                

            data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Recieved','Requested':'Requested','Published':'Published','access':access,  'categories': json.dumps(categories),
        'succesful_closed': json.dumps(succesful_closed),
        'published': json.dumps(published)}
            
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
                 published_count=JobPost.objects.filter(status=3).count()
             except JobPost.DoesNotExist:
                 published_count=0
             request.session['access'] = access

             titles=list(JobPost.objects.all().values_list('title'))
             titles=list(chain(*titles))
             print(titles)
             categories = list()
             succesful_closed = list()
             published = list()
             specific=list(JobPost.objects.all().values_list('id'))
             specific=list(chain(*specific))
             

             titles=list(JobPost.objects.all().values_list('title'))
             titles=list(chain(*titles))
             
             print(titles)
             categories = list() 
             succesful_closed = list()
             published = list()
             for ti in titles:
                 categories.append(ti)  
             for spec in specific:
                 try:
                     c=JobPost.objects.filter(id=spec).filter(status=3).count()
                     published.append(c)
                    

                 except JobPost.DoesNotExist:
                     c=0
                     published.append(c)
            
                 try:
                     c1=JobPost.objects.filter(id=spec).filter(status=4).count()
                     succesful_closed.append(c1)
                    

                 except JobPost.DoesNotExist:
                     c1=0
                     succesful_closed.append(c1)  
              
                
              
                

             data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Sent','Requested':'Pending','Published':'Published','access':access,  'categories': json.dumps(categories),
        'succesful_closed': json.dumps(succesful_closed),
        'published': json.dumps(published)}

        return render(request,'firstpage.html',data_dict)    
         
    else:

        if request.session.get('access')=='Hiring Manager':
            access=request.session.get('access')
            recieved_count=0
            requested_count=0
            published_count=0
            request.session['access'] = access
            data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Recieved','Requested':'Requested','Published':'Published','access':access}
    
        else:
            access=request.session.get('access')
            recieved_count=0
            requested_count=0
            published_count=0
            request.session['access'] = access
            data_dict = {'re_c': recieved_count,'req_c':requested_count,'pub_c':published_count,'Received':'Sent','Requested':'Pending','Published':'Published','access':access}
        return render(request,'firstpage.html',data_dict)






def signin(request):
    if request.user.is_authenticated:
        return redirect("/portal/dashboard")

    else:
        if(request.method=="POST"):
            form=LoginForm(request.POST)
            if form.is_valid():
                AID=form.cleaned_data['AID']
                password=form.cleaned_data['Password']
                try:
                    u=Profile.objects.get(AID=AID)
                except Profile.DoesNotExist:
                    form=LoginForm()
                    return render(request,'login.html',{'form':form,'messages':'Username does not exist'})
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
                    form=LoginForm()
                    return render(request,'login.html',{'form':form,'messages':'Incorrect Password'})
                    
                    
        else:
            form=LoginForm()
            return render(request,'login.html',{'form':form})

@login_required
def show_resume(request, file):
    fsock = open("../../media/"+file, 'r')
    response = HttpResponse(fsock, mimetype='application/pdf')
    return response