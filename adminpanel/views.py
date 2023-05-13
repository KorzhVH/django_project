from django.http import HttpResponse
from django.shortcuts import render
from salon.models import Service, Schedule, Master
def main(request):
    return HttpResponse()

def masters(request):
    return HttpResponse()

def one_master(request, master_id):
    return HttpResponse()

def services(request):
    return HttpResponse()

def one_service(request, service_id):
    return HttpResponse()