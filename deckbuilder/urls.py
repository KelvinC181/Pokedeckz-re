from . import views
from django.urls import path

urlpatterns = [
    path('deckbuilder', views.DeckList.as_view(), name='deckbuilder'),
]