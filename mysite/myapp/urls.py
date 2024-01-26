from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('human/', views.human, name="human"),
    path('cat/',views.cat, name="cat"),
]