from django.urls import path
from . import views

urlpatterns = [
    path('view-mathematics/', views.mathematics, name='view-mathematics'),
path('add-mathematics/', views.add_mathematics, name='add-mathematics'),
]
