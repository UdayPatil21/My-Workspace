from django.urls import  path
from . import  views

urlpatterns = [
    path('', views.login, name='login'),
    path('home',views.home,name='home'),
    path('submit',views.submit, name='submit'),
    path('addUser',views.addUser,name='addUser'),
    path('history',views.history,name='history')
]