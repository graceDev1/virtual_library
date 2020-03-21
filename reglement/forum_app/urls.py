from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('load/',views.load_lib, name='load'),
    
    # authentification urls
    path('register/',views.registerPage, name='register'),
    path('login/',views.loginPage, name='login'),
    path('logout/',views.logoutPage, name='logout')
   
] 