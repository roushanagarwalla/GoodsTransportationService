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
    path('logout/', views.logout, name="logout"),
    path('book/<int:id>', views.book, name="book")
]