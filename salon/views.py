from django.http import HttpResponse
from django.shortcuts import render

# these handle requests. Swap return message for templates later
def root_handler(request):
    return HttpResponse("Temp message for root handler")

