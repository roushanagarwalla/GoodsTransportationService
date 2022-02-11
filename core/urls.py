from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup, name="signup"),
    path('signup/driver', views.signup_driver, name="signup_driver"),
    path('signup/dealer', views.signup_dealer, name="signup_dealer"),
    path('login/', views.login, name="login"),
    path('login/driver', views.login_driver, name="login_driver"),
    path('login/dealer', views.login_dealer, name="login_dealer"),
    path('logout/', views.logout, name="logout"),
]