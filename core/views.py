from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Dealer, Driver, Book
from django.contrib.auth import authenticate, login, logout

def signup(request):
    return render(request, "signup/signup.html")

def signup_dealer(request):
    if request.method == "POST":
        name = request.POST.get("name")        
        email = request.POST.get("email")        
        mob = request.POST.get("mob")        
        nature = request.POST.get("nature")        
        weight = request.POST.get("weight")        
        from_state = request.POST.get("from_state")        
        from_city = request.POST.get("from_city")        
        to_state = request.POST.get("to_state")        
        to_city = request.POST.get("to_city")        
        pass1 = request.POST.get("pass1")        
        pass2 = request.POST.get("pass2")
        user = User.objects.create_user(email, email, pass1)
        user.first_name = "dealer"
        user.save()
        dealer = Dealer(rel=user, name=name, mob=mob, nature=nature, weight=weight, from_state=from_state, from_city=from_city, to_state = to_state, to_city=to_city)
        dealer.save()
        redirect("/login/dealer")
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

        user = User.objects.create_user(email, email, pass1)
        user.first_name = "driver"
        user.save()
        
        driver = Driver(rel=user, name=name, mob=mob, age=age,driving_experience = exp , truck_no=truck_no, truck_capacity=capacity, transporter_name= tname,from_state1=from_state1, from_city1=from_city1, to_state1 = to_state1, to_city1=to_city1, from_state2=from_state2, from_city2=from_city2, to_state2 = to_state2, to_city2=to_city2, from_state3=from_state3, from_city3=from_city3, to_state3 = to_state3, to_city3=to_city3)
        driver.save()
        redirect("/login/driver")
    return render(request, "signup/signup_driver.html")

def login_user(request):
    return render(request, "login/login.html")

def login_dealer(request):
    if request.method == "POST":
        email = request.POST.get("email");
        password = request.POST.get("pass");
        user = authenticate(username=9678388634, password=password)
        if user is not None:
            login(request, user)
            return redirect("/dealer")
    return render(request, "login/login_dealer.html")

def login_driver(request):
    if request.method == "POST":
        email = request.POST.get("email");
        password = request.POST.get("pass");
        user = authenticate(username=1234567890, password="Roshan@1234")
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/driver")
    return render(request, "login/login_driver.html")

def logout(request):
    return redirect("/login")

def index_dealer(request):
    print(request.user)
    dealer = Dealer.objects.filter(rel = request.user).first()
    drivers = Driver.objects.filter(Q(from_city1=dealer.from_city, to_city1=dealer.to_city) | Q(from_city2=dealer.from_city, to_city2=dealer.to_city) | Q(from_city2=dealer.from_city, to_city2=dealer.to_city))
    print(drivers)
    return render(request, "index_dealer.html", context={
        "drivers": drivers,
    })

def index_driver(request):
    user = request.user
    driver = Driver.objects.filter(rel=user)
    if driver.first():
        bookings = Book.objects.filter(driver = driver.first())
        print(bookings)
    bookings = Book.objects.filter(driver=driver.first())
    return render(request, "index_driver.html", context={
        "bookings": bookings,
    })

def index(request):
    if request.user is None:
        return redirect("/login")
    if request.user.first_name == "driver":
        return redirect("/driver")
    if request.user.first_name == "dealer":
        return redirect("/dealer")
    return render(request, "index.html")

def book(request, id):
    user = request.user
    dealer = Dealer.objects.get(rel=user)
    driver = Driver.objects.get(id = id)
    booking = Book(dealer = dealer, driver = driver)
    booking.save()
    print("You have Booked ", driver)
    return redirect("/")