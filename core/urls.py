from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.index),
    path('dealer/', views.index_dealer, name="index_dealer"),
    path('driver/', views.index_driver, name="index_driver"),
    path('signup/', views.signup, name="signup"),
    path('signup/driver', views.signup_driver, name="signup_driver"),
    path('signup/dealer', views.signup_dealer, name="signup_dealer"),
    path('login/', views.login_user, name="login_user"),
    path('login/driver', views.login_driver, name="login_driver"),
    path('login/dealer', views.login_dealer, name="login_dealer"),
    path('logout/', views.handle_logout, name="logout"),
    path('book/<int:id>', views.book, name="book"),
    path('search/', views.search, name="search"),
    path('details/driver/<int:id>', views.driver_details, name="driver_details"),
    path('details/dealer/<int:id>', views.dealer_details, name="dealer_details"),
    path('login_otp/', views.login_otp, name="login_otp"),
    path('login_otp/driver', views.login_driver_otp, name="login_driver_otp"),
    path('login_otp/dealer', views.login_dealer_otp, name="login_dealer_otp"),
    path('verify_otp', views.verify_otp, name="verify_otp"),
]