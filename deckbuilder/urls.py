from . import views
from django.urls import path

urlpatterns = [
    path('deckbuilder', views.Hompage_view, name='deckbuilder'),
]