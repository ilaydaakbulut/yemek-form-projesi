from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q,Sum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CurrentRestaurantForm, SignInForm,PriceForm,WorkTypeForm
from accounts.models import Profile,Price,CurrentRestaurant,WorkType
from .utils import get_query, paginate
from django.shortcuts import get_object_or_404

def signin_view(request):
    form = SignInForm()
    if request.POST:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            nextpage = request.POST.get("next") or reverse("home") #sayfa yönlendirmesi
            try:
                user = User.objects.get(Q(username=username)|Q(email=username))
                auth = authenticate(username=user.username, password=password)
                if auth and user and user.is_active:
                    login(request, user)
                    return redirect(nextpage)
            except:
                pass
            messages.warning(request, "Error, Invalid Input")
    return render(request, "signin.html", dict(form=form))

def signup_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "OK, SignUp has been succeeded!")
            return redirect(reverse("accounts:signin_view"))
        else:
            messages.warning(request, "Error, Invalid Input")
    return render(request, "signup.html", dict(form=form))

@login_required
def profile_view(request):
    form =ProfileForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,'profile.html', dict(form=form))

def profile_view_id(request,id): #veritabanına girilen verileri kaydetme

    context ={
    }
    return render(request,'profile.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect("/")

@login_required
def currentrestaurant_view(request):
    form =CurrentRestaurantForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url()) #sayfa yönlendirmesi yapar.
    return render(request,'currentRestaurant.html', dict(form=form))

def currentrestaurant_view_id(request,id): #veritabanına girilen verileri kaydetme

    context ={
    }
    return render(request,'currentRestaurant.html',context)

def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required
def User_List(request):
    profiles  = Profile.objects.all()
    prices    = Price.objects.all()
    worktypes = WorkType.objects.all()
    currents  = CurrentRestaurant.objects.all()
    search    = request.GET.get("search")
    worktype  = request.GET.get("worktype") #rastgele isimlendirilir
    price     = request.GET.get("price")
    date_min  = request.GET.get("date_min")
    date_max  = request.GET.get("date_max")

    if search:
        entry_query = get_query(search, ("profile__name",),)
        currents = currents.filter(entry_query)

    if worktype:
        currents = currents.filter(worktype__pk=worktype)

    if price:
        currents = currents.filter(expose__pk=price)

    if is_valid_queryparam(date_min):
        currents = currents.filter(created__gte=date_min)

    if is_valid_queryparam(date_max):
        currents = currents.filter(created__lt=date_max)
    
    total = currents.aggregate(Sum('expose__expense'))

    ctx = {
        "profiles": profiles,
        "prices":prices, #restoran select
        "worktypes": worktypes, #worktype select
        "currents":currents,
        "total":total,
    }
    return render(request, 'user_list.html', ctx)

@login_required
def Profile_List(request):
    profiles  = Profile.objects.all()
    currents  = CurrentRestaurant.objects.all()
    prices    = Price.objects.all()
    worktypes = WorkType.objects.all()

    ctx = {
        "profiles": profiles,#name search
        "currents": currents, #worktype select
        "worktypes":worktypes,
        "prices":prices,
    }
    return render(request,'profilelist.html',ctx)

@login_required
def profile_manage(request):
    args = {}
    if request.POST and request.is_ajax():
        worktype_pk = request.POST.get("worktype_pk") or -1
        worktype = WorkType.objects.filter(pk=worktype_pk).first()
        if worktype:
            args = list(map(lambda a: a.get_dict(), worktype.prices.all()))
            #print(args)
    return JsonResponse(args, safe=False)

@login_required
def Profile_view_by_id(request,id):
    profile  = get_object_or_404(CurrentRestaurant, pk=id)

    ctx = {
        "profile": profile,#name search
    }
    return render(request,'profilelist.html',ctx)

@login_required
def price_view(request):
    form = PriceForm()
    prices = Price.objects.all()
    if request.method =="POST" : 
        form = PriceForm(data=request.POST)
        if form.is_valid(): 
          form.save()
          return redirect(reverse("home"))
    ctx={
        "form" : form,
        "prices": prices,
    }
    return render(request, 'price.html', ctx)

@login_required
def worktype_view(request):
    form = WorkTypeForm()
    worktypes = WorkType.objects.all()
    if request.method =="POST" : 
        form = WorkTypeForm(data=request.POST)
        if form.is_valid(): 
          form.save()
          return redirect(reverse("home"))
    ctx={
        "form" : form,
        "worktypes": worktypes,
    }
    return render(request, 'worktype.html', ctx)

@login_required
def currentrestaurant_manage(request):
    args = {}
    if request.POST and request.is_ajax():
        worktype_pk = request.POST.get("worktype_pk") or -1
        worktype = WorkType.objects.filter(pk=worktype_pk).first()
        if worktype:
            args = list(map(lambda a: a.get_dict(), worktype.prices.all()))
            #print(args)
    return JsonResponse(args, safe=False)