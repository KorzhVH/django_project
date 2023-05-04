from django.contrib import admin
from django.urls import path
import user.views

urlpatterns = [
    path('login', user.views.login_handler),
    path('register', user.views.register_handler),
    path('logout', user.views.logout_handler)
]
