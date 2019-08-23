from django.contrib import admin
from django.urls import path,include 
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
] 
