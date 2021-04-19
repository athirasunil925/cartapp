from django.urls import path
from . import views
app_name='foodcart_app'
urlpatterns=[
    path('',views.food,name='food'),
    path('menu/',views.menu,name='menu'),
    path('gallery/', views.gallery, name='gallery'),
    path('<slug:product_slug>/', views.productcatdetail, name='productcatdetail'),
    ]