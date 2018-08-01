# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
from .forms import EditDetails, UploadFile
# Create your views here.


def index(request):
    if (request.method == 'POST'):
         form = UploadFile(request.POST, request.FILES)
         if form.is_valid():
            # file is saved
            form.save()
    else:
        form = UploadFile()
        return render(request, 'candidate/index.html', {'form': form})

def editdetails(request):
    if request.method == 'POST':
        form = EditDetails(request.POST)
        if form.is_valid():
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
            q.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        # Retrieve data for cvscan

        # data= {'name': q.name,
        #         'email': q.email,
        #         'address' : q.address,
		# 'pincode' : q.pincode,
		# 'experience' : q.experience,
        #         'phone' : q.phone,
        # }
        # form = EditDetails(initial = data)

        form = EditDetails()
    return render(request, 'candidate/editdetails.html', {'form': form})

