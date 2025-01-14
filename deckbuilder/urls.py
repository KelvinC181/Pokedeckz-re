from . import views
from django.urls import path

urlpatterns = [
    path('', views.Hompage_view, name='home'),
]