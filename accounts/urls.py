from django.urls import path
from . import views
from .views import ekle,ekle_id,ekle2,ekle2_id

app_name = "accounts"

urlpatterns = [

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('ProfileForm/', ekle, name='ProfileFormekle'),
    path('ProfileForm/<int:id>/', ekle_id, name='ProfileFormekle_id'),
    path('CurrentRestaurantForm/', ekle2, name='CurrentRestaurantFormekle'),
    path('CurrentRestaurantForm/<int:id>/', ekle2_id, name='CurrentRestaurantFormekle_id'),

]