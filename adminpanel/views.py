from django.http import HttpResponse
from django.shortcuts import render

def panel_handler(request):
    return HttpResponse("Temp message for admin panel")

def panel_booking_handler(request):
    return HttpResponse("Temp message for admin panel booking page")

def panel_specialist_handler(request):
    return HttpResponse("Temp message for admin panel specialists")

def panel_specialist_id_handler(request, specialist_id):
    return HttpResponse(f"Temp message for admin panel specialsts {specialist_id} page")