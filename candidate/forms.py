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
    Qualifiction=forms.CharField(min_length=20,max_length=2000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Qualification'}))
    Skills=forms.MultiValueField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Skills'}))

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
