from . import views 
from django.urls import path
urlpatterns =[ 
    path('signup',views.signup),
    path('home',views.home),
    path('bookings',views.viewBookings),
    path('bookTickets',views.bookTickets),
    path('dateSearch',views.dateSearch),
    path('timeSearch',views.timeSearch),
    path('ticketBooking',views.ticketBooking),
    path('demo',views.home)

]