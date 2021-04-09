from django.urls import path
from . import views
from .expiry import *
import threading
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('plans', views.plans, name='plans'),
    path('payments', views.payments, name='payments'),
    path('userplans', views.userplans, name='userplans'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('expirycheck', views.expirycheck, name='expirycheck'),
]
#t = threading.Thread(target=expired_check(), args=(), kwargs={})
#t.setDaemon(True)
#t.start()