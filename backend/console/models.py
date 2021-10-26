# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils import timezone
# Create your models here.

class Community(models.Model):
	label = models.CharField(max_length = 200)

class User(models.Model):
	username = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	#community = models.ForeignKey(Community, default = None, on_delete = models.CASCADE)


class Admin(models.Model):
	username = models.CharField(max_length = 200)
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	#community = models.ForeignKey(Community, default = None, on_delete = models.CASCADE)

class Camera(models.Model):
	coordinates = models.CharField(max_length = 200, blank = True, unique = True)
	live_stream = models.CharField(max_length = 200, blank = True)
	#community = models.ForeignKey(Community, default = None, on_delete = models.CASCADE)
	#def __str__(self):
	#	return self.camera_id


class Footage(models.Model):
	camera = models.ForeignKey(Camera, default = None, on_delete = models.CASCADE)
	date = models.DateField(default=datetime.date.today())
	time = models.TimeField(auto_now_add = True)
	URL = models.CharField(max_length = 200, blank = True)
	thumbnail = models.CharField(max_length = 200, blank = True)


class video_instance_form(ModelForm):
	class Meta:
		model = Footage
		fields = ['URL', 'date']

class access_instance(models.Model):
	username = models.CharField(max_length = 200)
	accessed_camera = models.ForeignKey(Camera, default = None, blank = True, null = True, on_delete = models.CASCADE)
	accessed_footage = models.ForeignKey(Footage, default = None, on_delete=models.CASCADE)

	accessed_camera_location = models.CharField(max_length=50, blank = True)
	accessed_footage_date = models.CharField(max_length=50, blank = True)
	accessed_footage_time = models.CharField(max_length=50, blank = True)

	date = models.DateField(default=datetime.date.today())
	time = models.TimeField(auto_now_add = True)



#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#basic-sign-up
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



#class Profile(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  bio = models.TextField(max_length=500, blank=True)
   # location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)


#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   # instance.profile.save()
