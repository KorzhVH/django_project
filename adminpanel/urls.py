from django.contrib import admin
from django.urls import path
import adminpanel.views

urlpatterns = [
    path('panel', adminpanel.views.panel_handler),
    path('panel/booking', adminpanel.views.panel_booking_handler),
    path('panel/specialist', adminpanel.views.panel_specialist_handler),
    path('panel/specialist/<int:specialist_id>', adminpanel.views.panel_specialist_id_handler)
]
