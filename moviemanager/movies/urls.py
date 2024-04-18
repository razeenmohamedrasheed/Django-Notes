from django.urls import path
from . import views

urlpatterns = [
    path('', views.listMovie,name="list"),
    path('create/', views.createMovie,name="create"),
    path('edit/', views.editMovie,name="edit"),
]
