from django.shortcuts import render,redirect
from django.contrib.auth.models import User , auth 
from .models import Flights , Bookings, Customer, AvailableSeats
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
# Create your views here.
# def login(request):
#     #form  = request.method('POST')
#     if request.method == 'POST':
#         first_name  = request.POST['first_name'] 
#         last_name   = request.POST['last_name'] 
#         user_name   = request.POST['username'] 
#         email       = request.POST['email'] 
#         password1   = request.POST['password1'] 
#         password2   = request.POST['password2'] 
        
#         user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
#         user.save()
#         print("done")
#         #return render(request,'../templates/registration.html')
#         return redirect('/')
#     form  = SignUpForm()
#     return render(request,'../templates/signup.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            user.email = form.cleaned_data['email']
            user.username = user.email.split('@')[0]
            user.set_password(form.cleaned_data['password'])
            user.save()
            address = form.cleaned_data['address']
            contact = form.cleaned_data['contact']
            customer = Customer.objects.create(customer=user, address=address, contact=contact)
            customer.save()
            return redirect('http://localhost:8000/accounts/login/')
        
    else:
        form = SignUpForm()
        
    return render(request, '../templates/signup.html', {'form': form})


@login_required
def home(request):
    print(request.GET['id'])
    flight = Flights.objects.get(id=request.GET['id'])
    date = datetime.now()
    ava = AvailableSeats.objects.filter(date=request.GET['d'])
    dn = request.GET['d'].split('-')
    dd = datetime(int(dn[0]),int(dn[1]),int(dn[2]))
    if(len(ava) != 0):
        date = dd
        ava = ava[0]
    else:
        ava = AvailableSeats(date=dd,flight_name=flight.name,flight_number=flight.number)

    booking = Bookings(flight_number=flight.number,flight_name=flight.name, date= date, number= int(flight.number)-1,customer_name=request.user)
    booking.save()
    ava.number_of_available -= 1
    ava.save()

    return render(request,'../templates/home.html')

def my_bookings(request):
    user_name = request.user.username 
    #Order.objects.filter(payment_status="Completed")
    li = Flights.objects.filter().values()
    print(user_name)
    print(User.objects.all())
    return render(request,'../templates/bookings.html',{'li':li})

    
def bookTickets(request):
    if request.method == 'POST':
        from_adr  = request.POST['from_adr']
        to_adr  = request.POST['to_adr']
        
        li = Flights.objects.filter(fromAdr=from_adr.lower(),toAdr=to_adr.lower()).values()

        return render(request,'../templates/tickets.html',{'from_adr':from_adr,'to_adr':to_adr,'postRequest': "Test",'li':li})
    return render(request,'../templates/bookTickets.html',{'postRequest':"False"})

def timeSearch(request):
    start_time = request.POST['start_time']
    end_time = request.POST['end_time']
    li = Flights.objects.filter().values()
    lii = []
    
    for i in li :
        if str(i['time']) >= start_time and str(i['time']) <= end_time: 
          lii.append(i)  

    return render(request,'../templates/timeSearch.html',{'lii':lii})


@login_required
def dateSearch(request):
    li = Flights.objects.filter().values()
    d = request.POST['date22']
    dn = d.split('-')
    dd = datetime(int(dn[0]),int(dn[1]),int(dn[2])).strftime('%A')
    ll = []
    
    for i in li:
        if i['dialy']:
            ll.append(i)
        elif i["Week_day"] == dd:
            ll.append(i)

    return render(request,'../templates/dateSearch.html',{"ll": ll, "userdate": d})

def viewBookingsBasedOnNumber(request):
    pass


def viewBookingsBasedOnTime(request):
    pass

def viewBookings(request):
    all_bookings = Bookings.objects.filter(customer_name=request.user)
    return render(request, "../templates/bookings.html", {'all_bookings': all_bookings})

@login_required
def ticketBooking(request):
    return render(request,'../templates/booked.html')