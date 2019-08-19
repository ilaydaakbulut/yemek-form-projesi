from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#from django.urls import reverse_lazy
from django.urls import reverse
#from django.views import generic
from django.db.models import Q,Sum
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, CurrentRestaurantForm, SignInForm
#from .filters import UserFilter
from accounts.models import Profile,Price,CurrentRestaurant,WorkType
from .utils import get_query, paginate
"""
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
"""
def signin_view(request):
    form = SignInForm()
    if request.POST:
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            nextpage = request.POST.get("next") or reverse("accounts:currentrestaurant_view") #sayfa yönlendirmesi
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
            return redirect(reverse("accounts:profile_view"))
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
    currents  = CurrentRestaurant.objects.all()
    worktypes = WorkType.objects.all()
    search    = request.GET.get("search")
    work_type = request.GET.get("work_type")
    price     = request.GET.get("price")
    date_min  = request.GET.get("date_min")
    date_max  = request.GET.get("date_max")

    if search:
        entry_query = get_query(search, ("name",))
        profiles = profiles.filter(entry_query)

    if work_type:
        profiles = profiles.filter(work_type__pk=work_type)
        #worktypes = worktypes.filter(name=work_type)

    if price:
        profiles = profiles.filter(expose__pk=price)
        currents=currents.filter(expose__pk=price)

    # if is_valid_queryparam(date_min):
    #     currents = currents.filter(created__gte=date_min)

    # if is_valid_queryparam(date_max):
    #     currents = currents.filter(created__lt=date_max)

    num_post = profiles.count() #tarek abi ekledi
    
    total = currents.aggregate(Sum('expose__expense'))

    ctx = {
        "profiles": profiles,#name search
        "prices":prices, #restoran select
        "work_type": worktypes, #worktype select
        #"worktype":profiles.work_type
        "total":total,
    }

    return render(request, 'user_list.html', ctx)

"""
def search(request):
    user_list = ProfileForm.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})

"""  
"""

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

def ekle2(request): #veritabanına girilen verileri kaydetme

    form =CurrentRestaurantForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context ={
        "form": form,
    }
    return render(request,'currentRestaurant.html',context)
"""
