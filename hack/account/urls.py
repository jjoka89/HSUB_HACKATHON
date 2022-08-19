from django.urls import path
from . import views
urlpatterns = [
    #path('',views.home, name='home'),
    path('login',views.logins,name='login'),
    path('logout',views.logouts,name='logout'),
    path('join',views.join,name='join'),
    path('myPage', views.myPage, name='myPage'),
    path('delete', views.delete, name='delete'),
]