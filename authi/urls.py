from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', views.custom_logout, name="logout"),
    path('stores/',views.findstore,name="findstore"),
    path('featured/',views.featuredproducts,name="fproducts"),
    path('payment/',views.paymentmethod,name= "payment"),
    ]
