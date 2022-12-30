from django.db import models
from django.contrib.auth.models import User , auth 

# Create your models here.
class Flights(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(default=0)
    available_seats  = models.IntegerField(default=60)
    Week_day  = models.CharField(max_length=10,default="",blank=True)
    dialy   = models.BooleanField(default=True)
    time    = models.TimeField(auto_now=False,auto_now_add=False)
    cost    = models.IntegerField(default=0)
    fromAdr = models.CharField(max_length=50,default=" ")
    toAdr   = models.CharField(max_length=50,default=" ")

class Customer(models.Model):
    pending = 'Pending'
    verified = 'Verified'

    STATUS = (
        (pending,pending),
        (verified,verified),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    contact = models.CharField(max_length = 10)
    orders = models.IntegerField(default=0)
    total_sale = models.IntegerField(default=0)

    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name

class Bookings(models.Model):
    flight_number = models.IntegerField(default=0)
    flight_name = models.CharField(max_length=100)
    date         = models.DateField()
    number = models.IntegerField(default=60)
    customer_name = models.CharField(max_length=50,default="")

class AvailableSeats(models.Model):
    date = models.DateField()
    number_of_available = models.IntegerField(default=60)
    flight_number = models.IntegerField(default=0)
    flight_name = models.CharField(max_length=100)

class BookTicket(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    date = models.DateField()
    tickets_available = models.IntegerField(default=60)
    customer_name = models.CharField(max_length=50,default="")