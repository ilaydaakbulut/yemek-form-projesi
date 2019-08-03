from django.contrib import admin
from django.urls import path,include 
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.conf.urls import url
from django_filters.views import FilterView
from accounts.filters import UserFilter



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    #url(r'^search/$', FilterView.as_view(filterset_class=UserFilter,template_name='search/user_list.html'), name='search'),
    path('search/',FilterView.as_view(filterset_class=UserFilter,template_name='user_list.html'), name='search'),
] 
