from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q,Sum

class Price(models.Model):
    name = models.CharField(max_length=100,verbose_name='Restaurant',blank=True)
    expense = models.IntegerField(default=0,blank=True,null=True,verbose_name='Expense')

    def __str__(self):
        return "{} ".format(self.name)

class WorkType(models.Model):
    name = models.CharField(max_length=100,verbose_name='Work Type',blank=True)

    def __str__(self):
        return "{} ".format(self.name)

    class Meta: #veritabanında görünen yer
        verbose_name = "Work Type"

class Profile(models.Model):

    name = models.CharField(max_length=100,verbose_name='Name Surname',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Username')
    work_type = models.ForeignKey(WorkType, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='Work Type')
    starting_date = models.DateField(verbose_name='Starting Date', help_text='Enter your starting date.Date : yyyy-aa-gg')
    ending_date = models.DateField(verbose_name='Ending Date', help_text='Enter your ending date.Date : yyyy-aa-gg')
    expose = models.ForeignKey(Price, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='Restaurant')
    #expose.expense    ücret atama fonksiyon ile yap.
    class Meta: 
        verbose_name_plural="Profile"
        ordering = ("name",)

    def __str__(self):   #veritabanında nasıl görüneceğini belirtir.
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:profile_view_id', kwargs={"id": self.id})

"""
    def filter(self):
        fil = WorkType.objects.filter(work_type__name='stajyer')
        if fil:
            fil = Price.objects.filter(expose__name='üniversite yemekhanesi')
        else:
            fil = Price.objects.all()
        return fil
        
    def current_restaurant(self):
        return CurrentRestaurant.objects.filter(name=self)

    def total_current_restaurant_price(self):
        ret = CurrentRestaurant.objects.filter(name=self).aggregate(Sum('expose__expense'))
        #print(ret)
        return ret
"""
class CurrentRestaurant(models.Model):
    
    name = models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='Username',blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True,verbose_name='Created Date',help_text='Date : yyyy-aa-gg')
    profile = models.ForeignKey(WorkType, on_delete=models.SET_NULL, verbose_name="Work Type",blank=True, null=True)
    expose = models.ForeignKey(Price, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='Restaurant')

    class Meta: #viewda kullanmak için
        verbose_name = "Current Food Movement"
        verbose_name_plural = verbose_name
        ordering = ("-id",)
  
    def get_full_name(self):
        if self.name:
            if self.name.user:
                return self.name
            else:
                return "No User Inside The Profile"
        else:
            return "No Profile"

    get_full_name.short_description = "Name Surname"
    
    def __str__(self):
        return "{} {}".format(self.get_full_name(),self.expose)

    def get_absolute_url(self):
        return reverse('accounts:currentrestaurant_view_id', kwargs={"id": self.id})