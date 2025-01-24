from . import views
from django.urls import path

urlpatterns = [
    path('', views.deckbuilder, name='deckbuilder'),
    path('my-decks/', views.MyDecks.as_view(), name='my_decks'),
    path('<int:id>/', views.deck_detail, name="deck_detail"),
]