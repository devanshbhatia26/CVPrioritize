from django import forms
from django.conf import settings
from django.utils import timezone
from django.forms import ModelForm
from .models import UploadFileModel
class EditDetails(forms.Form):
    EXPERIENCE_CHOICES = (
    ('1-3','1-3'),
    ('3-6','3-6'),
    ('6-9','6-9'),
    ('9-12','9-12'),
    ('12-15','12-15')
    )
    use_required_attribute=False
    name=forms.CharField(min_length=4,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    email=forms.EmailField(min_length=4,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    phone=forms.CharField(min_length=10,max_length=10,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    address=forms.CharField(min_length=20,max_length=2000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Address'}))
    pincode=forms.CharField(min_length=6,max_length=6,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'PIN'}))
    experience=forms.ChoiceField(choices=EXPERIENCE_CHOICES,widget=forms.Select(attrs={'class':'form-control'}))
    qualification=forms.CharField(min_length=20,max_length=2000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Qualification'}))
    skills=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Skills'}))

    def clean_name(self):
        if not self.cleaned_data['name']:
            raise ValidatonError("Name cannot be empty")
        return self.cleaned_data['name']
    
    def clean_email(self):
        if not self.cleaned_data['email']:
            raise ValidationError("Email cannot be empty")
        return self.cleaned_data['email']
    
    def clean_phone(self):
        if not self.cleaned_data['phone']:
            raise ValidationError("Phone cannot be empty")
        return self.cleaned_data['phone']
    
    def clean_address(self):
        if not self.cleaned_data['address']:
            raise ValidationError("Address cannot be empty")
        return self.cleaned_data['address']
    
    def clean_pincode(self):
        if not self.cleaned_data['pincode']:
            raise ValidationError("Pincode cannot be empty")
        return self.cleaned_data['pincode']
    
    def clean_qualification(self):
        if not self.cleaned_data['qualification']:
            raise ValidationError("Qualification cannot be empty")
        return self.cleaned_data["qualification"]
    
    def clean_skills(self):
        if not self.cleaned_data['skills']:
            raise ValidationError("Skills cannot be empty")
        return self.cleaned_data['skills']

class UploadFile(ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['file']
    
    def clean(self):
        print self.cleaned_data
        if not self.cleaned_data['file']:
            raise ValidationError("Upload the file first.")
        import os
        from django.core.exceptions import ValidationError
        valid_extensions = ['.pdf']
        ext = os.path.splitext(self.cleaned_data['file'].name)[1]
        if not ext.lower() in valid_extensions:
            raise ValidationError(u'Unsupported file extension.') 
        return self.cleaned_data
