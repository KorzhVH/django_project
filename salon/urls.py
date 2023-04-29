from django.contrib import admin
from django.urls import path
import salon.views

urlpatterns = [
    path('/', salon.views.r),
]
