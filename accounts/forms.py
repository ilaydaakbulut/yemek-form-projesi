from django import forms
from django.contrib.auth.models import User
from .models import Profile, CurrentRestaurant

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('name','work_type', 'starting_date', 'ending_date', 'restaurant',)
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
