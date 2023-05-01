from django.urls import path
from Rest import views

urlpatterns = [
    path('hello_world/', views.hello_world),
    path('hello/', views.hello),
    path('calculator/', views.calculator),
]