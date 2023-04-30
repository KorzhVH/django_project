from django.http import HttpResponse
from django.shortcuts import render


def login_handler(request):
    return HttpResponse("Temp message for login")

def register_handler(request):
    return HttpResponse("Temp message for registration")

def logout_handler(request, user_id):
    return HttpResponse("Temp message for logout")