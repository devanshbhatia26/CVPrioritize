# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
import json
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, UploadFileModel, Application
from .forms import EditDetails, UploadFile
from django.utils import timezone
from cvscan.cli.cli import parse
from os.path import splitext
from .Calc_Score import score_calculation


def totimestamp(dt, epoch=datetime(1970,1,1)):
    td = dt - epoch
    return int((int(td.microseconds) + (int(td.seconds) + int(td.days) * 86400) * 10*6) / 10*6)


def index(request):
    if (request.method == 'POST'):
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            obj = UploadFileModel()
            filename = str(totimestamp(datetime.now())) + ".pdf"
            obj.file.save(filename, form.cleaned_data['file'])
            return HttpResponseRedirect(reverse('editdetails', args=(obj.id,)))
    else:
        form = UploadFile()
    return render(request, 'candidate/index.html', {'form': form})

def editdetails(request, objId):
    obj = UploadFileModel.objects.get(id=objId)

    if request.method == 'POST':
        form = EditDetails(request.POST)
        if form.is_valid():
            print "validated"
            obj = UploadFileModel.objects.get(id = objId)
            q = Candidate()
            q.name = request.POST['name']
            q.email = request.POST['email']
            q.address = request.POST['address']
            q.pincode = request.POST['pincode']
            q.experience = request.POST['experience']
            q.phone = request.POST['phone']
            q.skills = request.POST['skills']
            q.qualification = request.POST['qualification']
            q.cv_path = obj.file
            q.created_timestamp = timezone.now()
            q.save()
            score_calculation(q)
            obj.delete()
            
            
            return HttpResponseRedirect(reverse('home'))
        else:
            print "Not Validated"
    else:
        result = json.loads(parse(str(obj.file.url)[:-4]),'utf-8')
        print result
        email = ""
        if result["emails"]:
            email = result["emails"][0]
        qual = ""
        if result["qualifications"]:
            qual = ", " .join(result["qualifications"])
        skill = ""
        if result["skills"]:
            skill = ", ".join(result["skills"]) 
        exp = result["experience"]
        if exp in [0,1,2]:
            exp = '0-2'
        elif exp in [3,4,5]:
            exp = '3-5'
        elif exp in [6,7,8]:
            exp= '6-8'
        elif exp in [9,10,11,12]:
            exp = '9-12'
        elif exp in [13,14,15]:
            exp = '13-15'
        else:
            exp = '15+'
        form = EditDetails(initial = {
            'name' : result["name"],
            'email' : email,
            'phone' : result["phone_numbers"],
            'address' : result["address"]["district"] +", "+ result["address"]["state"],
            'pincode' : result["address"]["pincode"],
            'qualification' : qual,
            'skills' : skill,
            'experience' : exp
        })
    return render(request, 'candidate/editdetails.html', {'form': form})

