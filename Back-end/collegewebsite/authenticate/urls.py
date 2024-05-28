from django.urls import path
from authenticate import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.loginuser, name = 'loginuser'),
    path('logout', views.logoutuser, name = 'logoutuser'),
    path('signin', views.signin, name = 'signin'),
    path('profile', views.profile, name = 'profile'),
    path('change_password', views.change, name = 'change')
]