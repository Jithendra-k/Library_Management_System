from django.urls import path
from . import views

urlpatterns = [
    path('view-oops/', views.oops, name='view-oops'),
path('add-oops/', views.add_oops, name='add-oops'),
]
