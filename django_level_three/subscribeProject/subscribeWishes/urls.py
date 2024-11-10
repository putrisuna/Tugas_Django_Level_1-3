from django.urls import path
from subscribeWishes import views

urlpatterns = {
    path('customers/', views.customer, name='customer'),
}