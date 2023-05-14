from django.contrib import admin
from django.urls import path
import adminpanel.views

urlpatterns = [
    path('', adminpanel.views.main),
    path('masters', adminpanel.views.masters),
    path('masters/<int:master_id>', adminpanel.views.one_master),
    path('services', adminpanel.views.services),
    path('services/<int:service_id>', adminpanel.views.one_service)
    ]

