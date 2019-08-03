from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q

class Profile(models.Model):
    INTERN = 1
    WORKER = 2
    WORKTYPES = [
        (INTERN, 'Stajyer'),
        (WORKER, 'Çalışan'),
    ]

    CASH = 1
    CINAR = 2
    UNIVERSITY = 3
    RESTAURANTS = (
        (CASH, "Ücret"),
        (CINAR, "Çınaraltı Restorant"),
        (UNIVERSITY, "Üniversite Yemekhanesi"),
    )
    name = models.CharField(max_length=100,verbose_name='Ad Soyad',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Kullanıcı Adı')
    work_type = models.IntegerField(choices=WORKTYPES, default=INTERN, verbose_name='Alan Seçimi')
    starting_date = models.DateField(verbose_name='Başlangıç tarihi', help_text='Başlangıç tarihinizi giriniz.')
    ending_date = models.DateField(verbose_name='Bitiş tarihi', help_text='Bitiş tarihinizi giriniz.')
    restaurant = models.IntegerField(verbose_name="Restaurant", default=CASH, choices=RESTAURANTS)


    class Meta: 
        verbose_name_plural="Profil"
        ordering = ("name",)

    def __str__(self):   #veritabanında nasıl görüneceğini belirtir.
        return self.name

    def get_absolute_url(self):
        return reverse('accounts:profile_view_id', kwargs={"id": self.id})

class CurrentRestaurant(models.Model):
    
    CASH = 1
    CINAR = 2
    UNIVERSITY = 3
    STATUSES = (
        (CASH, "Ücret"),
        (CINAR, "Çınaraltı Restorant"),
        (UNIVERSITY, "Üniversite Yemekhanesi"),
    )
    
    created = models.DateField(verbose_name='Bugünün Tarihi')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Çalışan",blank=True, null=True)
    status = models.IntegerField(verbose_name="Restaurant", choices=STATUSES, default=CASH)
    
    class Meta:
        verbose_name = "Cari Yemek Hareketi"
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

    get_full_name.short_description = "Adı Soyadı"

    def __str__(self):
        return "%s" %(self.get_full_name())

    def get_absolute_url(self):
        return reverse('accounts:currentrestaurant_view_id', kwargs={"id": self.id})

"""
    def sec(self):
        person = self.get_gender_display()
        if person == "Stajyer":
            return 'hiiiiiii'
"""