from django.urls import path
from . import views

app_name = 'homepage'  # Replace with your app's name

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('products/', views.products, name="products")
]
