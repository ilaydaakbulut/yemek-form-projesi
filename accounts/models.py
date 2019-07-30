from django.db import models
import os
from django.urls import reverse
from django.contrib.auth.models import User

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
    name = models.CharField(max_length=30,verbose_name='Ad Soyad',null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
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
        return reverse('accounts:ProfileFormekle_id', kwargs={"id": self.id})

class CurrentRestaurant(models.Model):
    class Meta:
        verbose_name = "Cari Yemek Hareketi"
        verbose_name_plural = verbose_name
        ordering = ("-id",)
    CASH = 1
    CINAR = 2
    UNIVERSITY = 3
    STATUSES = (
        (CASH, "Ücret"),
        (CINAR, "Çınaraltı Restorant"),
        (UNIVERSITY, "Üniversite Yemekhanesi"),
    )
    
    created = models.DateField(verbose_name='Bugünün Tarihi')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Çalışan")
    status = models.IntegerField(verbose_name="Restaurant", choices=STATUSES, default=CASH)

    def get_full_name(self):
        if self.profile:
            if self.profile.user:
                return self.profile.user.get_full_name()
            else:
                return "No User Inside The Profile"
        else:
            return "No Profile"

    get_full_name.short_description = "Adı Soyadı"


    def __str__(self):
        return "{}".format(self.get_full_name())

    def get_absolute_url(self):
        return reverse('accounts:CurrentRestaurantFormekle_id', kwargs={"id": self.id})