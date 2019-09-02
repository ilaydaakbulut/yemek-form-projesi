from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [

    path('signup/', views.signup_view, name='signup_view'),
    path('signin/', views.signin_view, name='signin_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('profile/manage/', views.profile_manage, name='profile_manage'),
    path('currentrestaurant/manage/', views.currentrestaurant_manage, name='currentrestaurant_manage'),
    path('currentrestaurant/', views.currentrestaurant_view, name='currentrestaurant_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('Profile/<int:id>/', views.profile_view_id, name='profile_view_id'),
    path('currentrestaurant/<int:id>/', views.currentrestaurant_view_id, name='currentrestaurant_view_id'),
    path('list/', view=views.User_List, name="User_List"),
    path('profilelist/', view=views.Profile_List, name="profilelist"),
    path('profilelist/<int:id>/', view=views.Profile_view_by_id, name="Profile_List_id"),
    path('price/', view=views.price_view, name="price_view"),
    path('worktype/', view=views.worktype_view, name="worktype_view"),
]