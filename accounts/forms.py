# -*- encoding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator, RegexValidator
from django import forms
from django.contrib.auth.models import User
from .models import Profile, CurrentRestaurant

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('name','user','work_type', 'starting_date', 'ending_date', 'restaurant',)
		def __init__(self, *args, **kwargs):
			super(ProfileForm, self).__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs = {'class': 'form-control'}

class CurrentRestaurantForm(forms.ModelForm):
	class Meta:
		model = CurrentRestaurant
		fields = ('created', 'profile', 'status',)
		def __init__(self, *args, **kwargs):
			super(CurrentRestaurantForm, self).__init__(*args, **kwargs)
			for field in self.fields:
				self.fields[field].widget.attrs = {'class': 'form-control'}

class SignInForm(forms.Form):
    default_attrs = {'class': 'form-control'}
    username_validators = [
        MaxLengthValidator(limit_value=255, message=_("Maximum length allowed is %(max_length)s") % dict(max_length=255)), 
        MinLengthValidator(limit_value=2, message=_("Minimum length allowed is %(min_length)s") % dict(min_length=2)),
    ]
    password_validators = [
        MaxLengthValidator(limit_value=255, message=_("Maximum length allowed is %(max_length)s") % dict(max_length=255)), 
        # PATCH: limit_value = 1, min_length = 5
        MinLengthValidator(limit_value=1, message=_("Minimum length allowed is %(min_length)s") % dict(min_length=5)),
    ]
    username = forms.CharField(widget=forms.TextInput(
        attrs=default_attrs.update(dict(placeholder=_("Email or Username")))
    ), validators=username_validators, required=True, label=_("Email or Username"))
    password  = forms.CharField(widget=forms.PasswordInput(
        attrs=default_attrs.update(dict(placeholder=_("Password")))
    ), validators=password_validators, required=True, label=_("Password"))