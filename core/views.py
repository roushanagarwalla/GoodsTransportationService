from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Dealer, Driver, Book
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    return render(request, "signup/signup.html")

def signup_dealer(request):
    if request.method == "POST":
        name = request.POST.get("name")        
        email = request.POST.get("email")        
        mob = request.POST.get("mob")        
        nature = request.POST.get("nature")        
        weight = request.POST.get("weight")        
        quantity = request.POST.get("quantity")        
        from_state = request.POST.get("from_state")        
        from_city = request.POST.get("from_city")        
        to_state = request.POST.get("to_state")        
        to_city = request.POST.get("to_city")        
        pass1 = request.POST.get("pass1")        
        pass2 = request.POST.get("pass2")      
        correct = True        
        if not pass1 == pass2:
            correct = False 
            messages.error(request, "The password does not match each other")
        user_exist = User.objects.filter(email=email)
        if user_exist.exists():
            correct = False 
            messages.error(request, "The Email already exists in our database, please Choose another one")  
        user_exist = Dealer.objects.filter(mob=mob)
        if user_exist.exists():
            correct = False 
            messages.error(request, "The Mobile Number already exists in our database, please Choose another one")
        if int(weight)<=0:
            correct = False 
            messages.error(request, "Weight should be greater than Zero")
        if int(quantity)<=0:
            correct = False 
            messages.error(request, "Quantity should be greater than Zero")
        if correct:
            user = User.objects.create_user(email, email, pass1)
            user.first_name = "dealer"
            user.save()
            dealer = Dealer(rel=user, name=name, mob=mob, nature=nature, weight=weight, quantity=quantity, from_state=from_state, from_city=from_city, to_state = to_state, to_city=to_city)
            dealer.save()
            messages.success(request, "Dealer Registration is Successful")
            return redirect("/login/dealer")
    return render(request, "signup/signup_dealer.html")

def signup_driver(request):
    if request.method == "POST":
        name = request.POST.get("name")        
        email = request.POST.get("email")        
        mob = request.POST.get("mob")        
        pass1 = request.POST.get("pass1")        
        pass2 = request.POST.get("pass2")
        age = request.POST.get("age")        
        exp = request.POST.get("exp")        
        tname = request.POST.get("tname")        
        truck_no = request.POST.get("truck_no")        
        capacity = request.POST.get("capacity")        
        from_state1 = request.POST.get("from_state1")        
        from_city1 = request.POST.get("from_city1")        
        to_state1 = request.POST.get("to_state1")        
        to_city1 = request.POST.get("to_city1")   
        
        from_state2 = request.POST.get("from_state2")        
        from_city2 = request.POST.get("from_city2")        
        to_state2 = request.POST.get("to_state2")        
        to_city2 = request.POST.get("to_city2")   

        from_state3 = request.POST.get("from_state3")        
        from_city3 = request.POST.get("from_city3")        
        to_state3 = request.POST.get("to_state3")        
        to_city3 = request.POST.get("to_city3") 

        correct = True        
        if not pass1 == pass2:
            correct = False 
            messages.error(request, "The password does not match each other")
        user_exist = User.objects.filter(email=email)
        if user_exist.exists():
            correct = False 
            messages.error(request, "The Email already exists in our database, please Choose another one")  
        user_exist = Driver.objects.filter(mob=mob)
        if user_exist.exists():
            correct = False 
            messages.error(request, "The Mobile Number already exists in our database, please Choose another one")        
        if int(age)<=0:
            correct = False
            messages.error(request, "Age must be greater than zero")
        if int(exp)<0:
            correct = False
            messages.error(request, "Age must be greater than or equal to zero")
        if int(capacity)<=0:
            correct = False
            messages.error(request, "Truck Capacity must be greater than zero")

        if correct:
            user = User.objects.create_user(email, email, pass1)
            user.first_name = "driver"
            user.save()
            driver = Driver(rel=user, name=name, mob=mob, age=age,driving_experience = exp , truck_no=truck_no, truck_capacity=capacity, transporter_name= tname,from_state1=from_state1, from_city1=from_city1, to_state1 = to_state1, to_city1=to_city1, from_state2=from_state2, from_city2=from_city2, to_state2 = to_state2, to_city2=to_city2, from_state3=from_state3, from_city3=from_city3, to_state3 = to_state3, to_city3=to_city3)
            driver.save()
            messages.success(request, "Driver Registration is Successful")
            return redirect("/login/driver")
    return render(request, "signup/signup_driver.html")

def login_user(request):
    return render(request, "login/login.html")

def login_dealer(request):
    if request.method == "POST":
        email = request.POST.get("email");
        password = request.POST.get("pass");
        user = authenticate(username=email, password=password)
        if user is not None:
            if not user.first_name == "dealer":
                messages.error(request, "You have not registered as a Dealer")
            else:
                login(request, user)
                return redirect("/dealer")
        else:
            messages.error(request, "You have entered Wrong Email or Password")
    return render(request, "login/login_dealer.html")

def login_driver(request):
    if request.method == "POST":
        email = request.POST.get("email");
        password = request.POST.get("pass");
        user = authenticate(username=email, password=password)
        if user is not None:
            if not user.first_name == "driver":
                messages.error(request, "You have not registered as a Driver")
            else:
                login(request, user)
                return redirect("/driver")
        else:
            messages.error(request, "You have entered Wrong Email or Password")
    return render(request, "login/login_driver.html")

@login_required
def handle_logout(request):
    logout(request=request)
    return redirect("/login")

@login_required
def index_dealer(request):
    dealer = Dealer.objects.filter(rel = request.user)
    if dealer.count() == 0:
        messages.error(request, "You are not a dealer")
        return redirect("/driver")
    else:
        dealer = dealer.first()
    drivers = Driver.objects.filter(Q(from_city1=dealer.from_city, to_city1=dealer.to_city) | Q(from_city2=dealer.from_city, to_city2=dealer.to_city) | Q(from_city3=dealer.from_city, to_city3=dealer.to_city))
    if drivers.count() == 0:
        drivers = None
    return render(request, "index_dealer.html", context={
        "drivers": drivers,
        "dealer": dealer,
    })

@login_required
def index_driver(request):
    user = request.user
    driver = Driver.objects.filter(rel=user)
    if driver.count() == 0:
        messages.error(request, "You are not a driver")
        return redirect("/dealer")
    else:
        bookings = Book.objects.filter(driver = driver.first())
    if bookings.count() == 0:
        bookings = None

    return render(request, "index_driver.html", context={
        "bookings": bookings,
        "driver": driver.first(),
    })

@login_required
def index(request):
    if request.user is None:
        return redirect("/login")
    if request.user.first_name == "driver":
        return redirect("/driver")
    if request.user.first_name == "dealer":
        return redirect("/dealer")
    return render(request, "index.html")

@login_required
def book(request, id):
    user = request.user
    dealer = Dealer.objects.get(rel=user)
    if dealer is None:
        messages.error(request, "You are not a Dealer")
        return redirect("/")
    driver = Driver.objects.get(id = id)
    if driver is None:
        messages.error(request, "The driver does not exists")
        return redirect("/")
    booking = Book(dealer = dealer, driver = driver)
    booking.save()
    messages.success(request, "The driver has been successfully Booked")
    return redirect("/")

@login_required
def search(request):
    if request.method == "POST":       
        from_state = request.POST.get("from_state")        
        from_city = request.POST.get("from_city")        
        to_state = request.POST.get("to_state")        
        to_city = request.POST.get("to_city")
        drivers = Driver.objects.filter(Q(from_city1=from_city, to_city1=to_city) | Q(from_city2=from_city, to_city2=to_city) | Q(from_city3=from_city, to_city3=to_city))
        if drivers.count() <=0:
            drivers=None
        return render(request, "search_detail.html", context={"drivers": drivers})
    return render(request, "search.html")

@login_required
def driver_details(request, id):
    if request.user.first_name == "driver":
        messages.error(request, "You are not allowed to see other driver's Details")
        return redirect("/")
    else:
        driver = Driver.objects.get(id = id)
        if driver is None:
            messages.error(request, "Driver Not Found")
            return redirect("/")
        return render(request, "driver_details.html", context = {"driver": driver})

@login_required
def dealer_details(request, id):
    if request.user.first_name == "dealer":
        messages.error(request, "You are not allowed to see other dealer's Details")
        return redirect("/")
    dealer = Dealer.objects.get(id = id)
    if dealer is None:
        messages.error(request,"Dealer Not Found")
        return redirect("/")
    return render(request, "dealer_details.html", context = {"dealer": dealer})