# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, UploadFileModel, Application
from .forms import EditDetails, UploadFile
# Create your views here.


def index(request):
    if (request.method == 'POST'):
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            print "here1"
            obj = form.save()
            return HttpResponseRedirect(reverse('editdetails', args=(obj.id,)))
    else:
        print "here3"
        form = UploadFile()
    return render(request, 'candidate/index.html', {'form': form})

def editdetails(request, objId):
    if request.method == 'POST':
        form = EditDetails(request.POST)
        if form.is_valid():
            print "here"
            obj = UploadFileModel.objects.get(id = objId)
            q = Candidate()
            name= form.cleaned_data['name']
            email= form.cleaned_data['email']
            address= form.cleaned_data['address']
            pincode= form.cleaned_data['pincode']
            experience= form.cleaned_data['experience']
            phone= form.cleaned_data['phone']
            q.name=name
            q.email=email
            q.address=address
            q.pincode=pincode
            q.experience=experience
            q.phone = phone
            q.cv_path = obj.file
            q.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        print objId
        print UploadFileModel.objects.get(id = objId).file
        form = EditDetails()
    return render(request, 'candidate/editdetails.html', {'form': form})

