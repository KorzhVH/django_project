from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=100)
    required_time = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.service_name


class Master(models.Model):
    RANK_CHOICES = (
        (1, 'Junior'),
        (2, 'Senior')
    )
    status_choice = (
        (1, 'Active'),
        (2, 'Day off'),
        (3, 'Sick leave'),
        (9, "Fired")
    )
    name = models.CharField(max_length=100)
    rank = models.IntegerField(choices=RANK_CHOICES)
    phone = models.IntegerField()
    services = models.ManyToManyField(Service)
    status = models.IntegerField(default=2, choices=status_choice)

    def __str__(self):
        return self.name


class Booking(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    client = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return {self.master}, {self.service}, {self.client}, {self.date}, {self.status}


class Schedule(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    def __str__(self):
        return {self.master},  {self.time_start}, {self.time_end}
