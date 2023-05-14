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
    if request.method == 'post':
        service = Service(
            name=request.POST['name'],
            required_time=request.POST['required_time'],
            price=request.POST['price']
        )
        service.save()
    services = Service.objects.all()
    return render(request, 'adminpanel/services.html', {'services': services})

def one_service(request, service_id):
    return HttpResponse()
