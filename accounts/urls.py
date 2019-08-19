from django.urls import path
from . import views


app_name = "accounts"

urlpatterns = [

    #path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signin/', views.signin_view, name='signin_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('currentrestaurant/', views.currentrestaurant_view, name='currentrestaurant_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('Profile/<int:id>/', views.profile_view_id, name='profile_view_id'),
    path('currentrestaurant/<int:id>/', views.currentrestaurant_view_id, name='currentrestaurant_view_id'),
    path('list/', view=views.User_List, name="User_List"),

]