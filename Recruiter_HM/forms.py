from django import forms
from .models import JobPost



class LoginForm(forms.Form):
    AID=forms.CharField(min_length=7,max_length=7,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'AID'}))
    Password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
   


class ChangePassword(forms.Form):
    
    Old_Password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Old Password'}))
    New_Password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    Confirm_Password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm New Password'}))

    def clean(self):
        cleaned_data=super().clean()
        Old_Password=cleaned_data.get('Old_Password')
        New_Password=cleaned_data.get('New_Password')
        Confirm_Password=cleaned_data.get('Confirm_Password')
        if New_Password!=Confirm_Password:
            raise forms.ValidationError('Password Does Not Matach')


class ForgetPassword(forms.Form):
    use_required_attribute=False
    New_Password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'New Password'}))
    Confirm_Password=forms.CharField(min_length=8,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm New Password'}))
    
    
    def clean(self):
        cleaned_data=super().clean()
        New_Password=cleaned_data.get('New_Password')
        Confirm_Password=cleaned_data.get('Confirm_Password')
        if New_Password!=Confirm_Password:
            raise forms.ValidationError('Password Does Not Matach')

class JobPostForm(forms.ModelForm):
    class Meta:
        model=JobPost
        fields=['title','responsibilities','qualification','overall_experience','primary_skills','secondary_skills']
        

class Candidate(forms.Form):
    use_required_attribute=False
    Name=forms.CharField(min_length=4,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    Email=forms.EmailField(min_length=4,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    Contact=forms.CharField(min_length=10,max_length=10,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Phone Number'}))
    Address=forms.CharField(min_length=20,max_length=2000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Address'}))
    Pin=forms.CharField(min_length=6,max_length=6,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'PIN'}))
    Experience=forms.CharField(min_length=1,max_length=2,widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Experience'}))
    Qualifiction=forms.CharField(min_length=20,max_length=2000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Qualification'}))
  