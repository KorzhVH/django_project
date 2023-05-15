from django.http import HttpResponse
from django.shortcuts import render
from salon.models import Service


def main(request):
    return HttpResponse()


def masters(request):
    return HttpResponse()


def one_master(request, master_id):
    return HttpResponse()


def services(request):
    if request.method == 'POST':
        service = Service(
            service_name=request.POST['service_name'],
            required_time=request.POST['required_time'],
            price=request.POST['price']
        )
        service.save()
    all_services = Service.objects.all()
    return render(request, 'services.html', {'all_services': all_services})

def one_service(request, service_id):
    return HttpResponse()
