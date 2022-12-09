from .views import *
from django.urls import path


urlpatterns = [
    path('accounts/profile/', users, name = 'redirect'),
    path('', index, name = "index"),
    path('customer', customer, name = "customer" )
]