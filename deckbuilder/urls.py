from . import views
from django.urls import path

urlpatterns = [
    path('', views.deckbuilder, name='deckbuilder'),
]