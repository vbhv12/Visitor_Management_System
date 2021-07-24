from django.forms import ModelForm
from .models import *
from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from datetime import datetime


def checkforpeople(value):
    if value>5:
        raise forms.ValidationError("Residents are more than allowed")

def checkforphone(value):
    if len(str(value))>10 or len(str(value))<10:
        raise forms.ValidationError("Enter valid phone number")

    for num in Host.objects.all():
            if num.Phone_no == value:
                raise forms.ValidationError("Enter a unique phone number")



def checkforage(value):
    if value<21:
        raise forms.ValidationError("Age is less than required (minimum is 21)")


#def checkforflat_no(value):
 #       for instance in Host.objects.all():
  #          if instance.flat_no == value:
   #             raise forms.ValidationError("This flat is not available")

class HostForm(ModelForm):
    no_of_people=forms.IntegerField(validators=[checkforpeople])
    Phone_no=forms.IntegerField(validators=[checkforphone])
    age = forms.IntegerField(validators=[checkforage])
    #flat_no = forms.IntegerField(validators=[checkforflat_no])
    class Meta:
        model = Host
        fields = '__all__'
        exclude = ['user','email_id','flat_no']

class HostForm1(ModelForm):
    no_of_people=forms.IntegerField(validators=[checkforpeople])
    Phone_no=forms.IntegerField(validators=[checkforphone])
    age = forms.IntegerField(validators=[checkforage])
    #flat_no = forms.IntegerField(validators=[checkforflat_no])
    class Meta:
        model = Host
        fields = '__all__'
        exclude = ['user','email_id']


class createuserform(UserCreationForm):

    class Meta:
        model=User
        fields=['username','email','password1','password2']



    def clean_email(self):
        email = self.cleaned_data.get("email")
        user_count=User.objects.filter(email=email).count()
        if user_count >0:
            raise forms.ValidationError("Enter different email")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        user_count=User.objects.filter(username=username).count()
        if user_count >0:
            raise forms.ValidationError("Enter different username,this is already taken.")
        return username  

def checkforphone1(value):
    if len(str(value))>10 or len(str(value))<10:
        raise forms.ValidationError("Enter valid phone number")



class VisitorForm(ModelForm):
    Phone_no=forms.IntegerField(validators=[checkforphone1])
    class Meta:
        model = Visitor
        fields = '__all__'
        exclude = ['user']
        
class VisitDetailsForm(ModelForm):
    class Meta:
        model = VisitDetails
        fields = '__all__'


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields ='__all__'
        
    def clean_event_date_time(self):
        event_date_time=self.cleaned_data.get("event_date_time")
        event_date_time= str(event_date_time)
        date_object = datetime.strptime(event_date_time, '%Y-%m-%d').date()
        if date.today() >=date_object :
            raise forms.ValidationError(u'Please enter valid date')
        return event_date_time

class EventVisitorForm(ModelForm):
    class Meta:
        model = EventVisitor
        fields = '__all__'
