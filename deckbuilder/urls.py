from . import views
from django.urls import path

urlpatterns = [
    path('', views.deckbuilder, name='deckbuilder'),
    path('decks/', views.DeckList.as_view(), name='deck_list'),
    path('my-decks/', views.MyDecks.as_view(), name='my_decks'),
    path('<int:deck_id>/', views.deck_detail, name='deck_detail'),
    path('<int:deck_id>/edit/',views.edit_deck, name='edit_deck'),
    path('<int:deck_id>/delete/',views.delete_deck, name='delete_deck'),
]