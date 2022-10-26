from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('LED1/',views.LED1),
    path('LED1ON/',views.LED1ON),
    path('LED1OFF/',views.LED1OFF),
    path('LED2/',views.LED2),
    path('LED2ON/',views.LED2ON),
    path('LED2OFF/',views.LED2OFF),
]