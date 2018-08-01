# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'candidate/index.html', {})

def editdetails(request, candidate_id):
    if request.method == 'POST':
        form = EditDetails(request.POST)
        q= Candidate.objects.get(id = candidate_id)
        if form.is_valid():
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
	    q.phone=phone
            q.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        q=Candidate.objects.get(id = candidate_id)
        data= {'name': q.name,
                'email': q.email,
                'address' : q.address,
		'pincode' : q.pincode,
		'experience' : q.experience,
                'phone' : q.phone,
        }
        form = EditDetails(initial = data)
    return render(request, 'candidate/editdetails.html', {'form': form})
