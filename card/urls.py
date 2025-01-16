from . import views
from django.urls import path

urlpatterns = [
    path('', views.CardLibrary.as_view(), name='home'),
]