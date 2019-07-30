from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import ProfileForm,CurrentRestaurantForm


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def ekle(request): #veritabanına girilen verileri kaydetme

    form =ProfileForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        "form": form,
    }
    return render(request,'ProfileForm.html',context)

def ekle_id(request,id): #veritabanına girilen verileri kaydetme

    context ={
    }
    return render(request,'ProfileForm.html',context)


def ekle2(request): #veritabanına girilen verileri kaydetme

    form =CurrentRestaurantForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        "form": form,
    }
    return render(request,'CurrentRestaurantForm.html',context)

def ekle2_id(request,id): #veritabanına girilen verileri kaydetme

    context ={
    }
    return render(request,'CurrentRestaurantForm.html',context)

