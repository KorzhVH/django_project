from django.contrib import admin
from django.urls import path
import adminpanel.views

urlpatterns = [
    path('adminpanel', adminpanel.views.main),
    path('adminpanel/masters', adminpanel.views.masters),
    path('adminpanel/masters/<int:master_id>', adminpanel.views.one_master),
    path('adminpanel/services', adminpanel.views.services),
    path('adminpanel/services/<int:service_id>', adminpanel.views.one_service)
    ]

