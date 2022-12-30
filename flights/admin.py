from django.contrib import admin
from .models import Flights,Bookings,BookTicket, AvailableSeats
# Register your models here.
admin.site.register(Flights)
admin.site.register(Bookings)
admin.site.register(BookTicket)
admin.site.register(AvailableSeats)