from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q,Sum

class Price(models.Model):
    name = models.CharField(max_length=100,verbose_name='Restorant',blank=True)
    expense = models.IntegerField(default=0,blank=True,null=True,verbose_name='expense')

    def __str__(self):
        return "{} ".format(self.name)

class WorkType(models.Model):
    name = models.CharField(max_length=100,verbose_name='Work Type',blank=True)

    def __str__(self):
        return "{} ".format(self.name)

    class Meta: #veritabanında görünen yer
        verbose_name = "Work Type"

class Profile(models.Model):

    name = models.CharField(max_length=100,verbose_name='Ad Soyad',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Kullanıcı Adı')
    work_type = models.ForeignKey(WorkType, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='work type')
    starting_date = models.DateField(verbose_name='Başlangıç tarihi', help_text='Başlangıç tarihinizi giriniz.')
    ending_date = models.DateField(verbose_name='Bitiş tarihi', help_text='Bitiş tarihinizi giriniz.')
    expose = models.ForeignKey(Price, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='restaurant')
    #expose.expense    ücret atama fonksiyon ile yap.
    class Meta: 
        verbose_name_plural="Profil"
        ordering = ("name",)

    def __str__(self):   #veritabanında nasıl görüneceğini belirtir.
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:profile_view_id', kwargs={"id": self.id})
"""
    def current_restaurant(self):
        return CurrentRestaurant.objects.filter(name=self)

    def total_current_restaurant_price(self):
        ret = CurrentRestaurant.objects.filter(name=self).aggregate(Sum('expose__expense'))
        #print(ret)
        return ret
"""

class CurrentRestaurant(models.Model):
    
    name = models.ForeignKey(Profile,on_delete=models.CASCADE,verbose_name='Kullanıcı Adı',blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True,verbose_name='Bugünün Tarihi')
    profile = models.ForeignKey(WorkType, on_delete=models.SET_NULL, verbose_name="work type",blank=True, null=True)
    expose = models.ForeignKey(Price, blank=True, null=True, on_delete=models.SET_NULL ,verbose_name='restaurant')

    class Meta: #viewda kullanmak için
        verbose_name = "Cari Yemek Hareketi"
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

    get_full_name.short_description = "Adı Soyadı"
    
    def __str__(self):
        return "{} {}".format(self.get_full_name(),self.expose)

    def get_absolute_url(self):
        return reverse('accounts:currentrestaurant_view_id', kwargs={"id": self.id})

""" 
class Count(Profile):

   function = 'COUNT'
    name = 'Count'
    output_field = models.IntegerField()
    allow_distinct = True

    def __init__(self, expression, filter=None, **extra):
        if expression == '*':
            expression = expressions.Star()
        if isinstance(expression, Star) and filter is not None:
            raise ValueError('Star cannot be used with filter. Please specify a field.')
        super().__init__(expression, filter=filter, **extra)

    def convert_value(self, value, expression, connection):
        return 0 if value is None else value


    total=0
    Profile.objects.all()
    for prof in profiles:
        total=+1


    def budget(self):
        total_expense_amount=0  #toplam gider tutarı
        for i in 30:   buradaki 30 yerine bir kullanıcı ayda kaç kere kayıt yaptırmıs
            if restaurant==CINAR:
                expense_cinar=+18
            elif restaurant==CASH:
                expense_cash=+15
            elif restaurant==UNIVERSITY:
                expense_university=+15
            total_expense_amount=expense_cash+expense_cinar+expense_university
        return total_expense_amount


def budget_left(self):
        expense_list=Expense.objects.filter(project=self)
        total_expense_amount=0
        for expense in expense_list:
            total_expense_amount += expense.amount
        return self.budget - total_expense_amount

"""