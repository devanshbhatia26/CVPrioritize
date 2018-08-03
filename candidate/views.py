# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, UploadFileModel, Application
from .forms import EditDetails, UploadFile
from django.utils import timezone
# Create your views here.


def index(request):
    if (request.method == 'POST'):
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            print "here"
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
            print "validated"
            obj = UploadFileModel.objects.get(id = objId)
            q = Candidate()
            name = request.POST['name']
            email = request.POST['email']
            address = request.POST['address']
            pincode = request.POST['pincode']
            experience = request.POST['experience']
            phone = request.POST['phone']
            q.name = name
            q.email = email
            q.address = address
            q.pincode = pincode
            q.experience = experience
            q.phone = phone
            q.cv_path = obj.file
            q.created_timestamp = timezone.now()
            q.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print "Not Validated"
    else:
        print objId
        print UploadFileModel.objects.get(id = objId).file
        form = EditDetails()
    return render(request, 'candidate/editdetails.html', {'form': form})

