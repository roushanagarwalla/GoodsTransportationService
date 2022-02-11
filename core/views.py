from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Dealer

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
        # if(pass1==pass2):
        # user = User.objects.create_user(mob, email, pass1)
        user = User.objects.get(username = mob)
        # print(user) 
        dealer = Dealer(rel=user, name=name, mob=mob, nature=nature, weight=weight, from_state=from_state, from_city=from_city, to_state = to_state, to_city=to_city)
        dealer.save()
    return render(request, "signup/signup_dealer.html")

def signup_driver(request):
    return render(request, "signup/signup_driver.html")

def login(request):
    return render(request, "login/login.html")

def login_dealer(request):
    return render(request, "login/login_dealer.html")

def login_driver(request):
    return render(request, "login/login_driver.html")

def logout(request):
    return redirect("/login")

def index(request):
    return render(request, "index.html")