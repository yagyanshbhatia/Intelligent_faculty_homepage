from django import forms
from django.contrib.auth.models import User

from .models import About,Edu,Teaching,Experience,Todolist
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ['name','position', 'dept', 'college','image', 'intro','email','telephone','officeaddress']

class EduForm(forms.ModelForm):

    class Meta:
        model = Edu
        fields = [ 'institute', 'degree', 'timeperiod']

class ExperienceForm(forms.ModelForm):

    class Meta:
        model = Experience
        fields = [ 'position', 'institute', 'timeperiod']

class TeachingForm(forms.ModelForm):

    class Meta:
        model = Teaching
        fields = ['course','currentorpast']

class TodolistForm(forms.ModelForm):

    class Meta:
        model = Todolist
        fields = ['reminder','date','month']