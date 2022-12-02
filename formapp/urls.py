from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.secondForm, name="secondForm"),
    path('formapp', views.home, name="home"),
    path("success", views.success)
]
