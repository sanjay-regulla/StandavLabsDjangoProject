from django.urls import include, path,re_path
from django.contrib.auth import views
from django.views.generic import TemplateView
from . import  views  

urlpatterns = [
    
    path('signup/',views.user_signup),
    path('login/',views.user_login),
    path('logout/',views.user_logout),
    path('product/',views.user_products),
    path('add-product/',views.add_user_products),
    ]