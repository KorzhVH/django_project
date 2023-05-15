from django.http import HttpResponse
from django.shortcuts import render
from salon.models import Service, Master, Schedule


def main(request):
    return HttpResponse()


def masters(request):
    if request.method == 'POST':
        master = Master(
            name=request.POST['name'],
            rank=request.POST['rank'],
            phone=request.POST['phone'],
            # services=Service.objects.get(id=request.POST['service']),
            status=2
        )
        master.save()

        services_ids = [value for key, value in request.POST.items() if key.startswith('service')]
        for service_id in services_ids:
            service = Service.objects.get(id=service_id)
            master.services.add(service)
        master.save()
    all_masters = Master.objects.all()
    services = Service.objects.all()
    return render(request, 'all_masters.html', {'all_masters': all_masters, 'services':services})


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
    service = Service.objects.filter(service=service_id)
    return render(request, 'one_service.html', {'title':service.service_name, 'service':service})
