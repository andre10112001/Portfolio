from django.urls import path
from . import views

app_name = 'homepage'  # Replace with your app's name

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('', views.homepage, name='homepage'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('products/', views.products, name="products"),
    path('basket/', views.basket, name="basket"),
    path('category/<str:category>/', views.category_games, name='category_games'),
    path('product_info/<str:product_id>/', views.product_info, name="product_info")
]
