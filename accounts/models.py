from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q,Sum
from .utils import get_query

class Price(models.Model):
    name = models.CharField(max_length=100,verbose_name='Restaurant',blank=True)
    expense = models.FloatField(default=0.0,blank=True,null=True,verbose_name='Expense')

    def __str__(self):
        return "{} ".format(self.name)
        
    def get_dict(self):
        return dict(
            pk= self.pk,
            name=self.name,
            expense=self.expense,
        )

class WorkType(models.Model):
    name = models.CharField(max_length=100,verbose_name='Work Type',blank=True)
    prices = models.ManyToManyField(Price, blank=True, related_name='worktype_prices', verbose_name='Prices Preferences')

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

    class Meta: 
        verbose_name_plural="Profile"
        ordering = ("name",)

    def __str__(self):   #veritabanında nasıl görüneceğini belirtir.
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:profile_view_id', kwargs={"id": self.id})


    # def Filter(self):
    #     WorkType.objects.filter(name='Stajyer').first()
    #     filters = CurrentRestaurant.objects.filter(worktype=WorkType.objects.filter(name='Stajyer').first())
    #     if filters:
    #         filters = CurrentRestaurant.objects.filter(expose__name='Üniversite Yemekhanesi')
    #         print(filters)
    #     else:
    #         filters = Price.objects.all()

    #     return filters

class CurrentRestaurant(models.Model):
    
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='Username',blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True,verbose_name='Created Date',help_text='Date : yyyy-aa-gg')
    worktype = models.ForeignKey(WorkType, on_delete=models.SET_NULL, verbose_name="Work Type",blank=True, null=True)
    expose = models.ForeignKey(Price, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='Restaurant')

    class Meta: #viewda kullanmak için
        verbose_name = "Current Food Movement"
        verbose_name_plural = verbose_name
        ordering = ("-id",)
  
    def get_full_name(self):
        if self.profile:
            if self.profile.user:
                return self.profile
            else:
                return "No User Inside The Profile"
        else:
            return "No Profile"

    get_full_name.short_description = "Name Surname"
    
    def __str__(self):
        return "{} {}".format(self.get_full_name(),self.expose)

    def get_absolute_url(self):
        return reverse('accounts:currentrestaurant_view_id', kwargs={"id": self.id})