import datetime

from django.http import HttpResponse
from salon.models import Service, Master, Schedule
def root_handler(request):
    return HttpResponse("Temp message for root handler")


def services_handler(request):
    schedules = Schedule.objects.filter(date__gte=datetime.date.today(),
                                        date__lte=datetime.date.today() + datetime.timedelta(days=7)).all()
    master = Master.objects.filter(status=True, id_in=schedules).all()
    service = Service.objects.filter(id_in=master).distinct()
    return HttpResponse("Temp message for services")


def services_id_handler(request, service_id):
    return HttpResponse(f"Temp message for services with id {service_id}")


def specialists_handler(request):
    return HttpResponse("Temp message for specialists")


def specialists_id_handler(request, specialist_id):
    return HttpResponse(f"Temp message for services with id {specialist_id}")


def booking_handler(request, service_id, specialist_id, user_id):
    return HttpResponse(f"Temp message for booking of {service_id}, done by {specialist_id} for {user_id}")
