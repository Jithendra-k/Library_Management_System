from django.urls import path
from . import views

urlpatterns = [
    path('view-biology/', views.biology, name='view-biology'),
path('add-biology/', views.add_biology, name='add-biology'),
]
