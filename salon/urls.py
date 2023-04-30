from django.contrib import admin
from django.urls import path
import salon.views

urlpatterns = [
    path('/', salon.views.root_handler), #homepage
    path('/services', salon.views.services_handler),
    path('/services/<int:service_id>', salon.views.services_id_handler),
    path('/specialist', salon.views.specialists_handler),
    path('/specialist/<int:service_id>', salon.views.specialists_id_handler),
    path('/booking', salon.views.booking_handler),

]
