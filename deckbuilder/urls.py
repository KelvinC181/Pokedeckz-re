from . import views
from django.urls import path

urlpatterns = [
    path('', views.deckbuilder, name='deckbuilder'),
    path('my-decks', views.MyDecks.as_view(), name='my-decks'),
]