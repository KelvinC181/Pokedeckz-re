from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Deck
from .forms import DeckForm
from card.models import Card


# Create your views here.
class DeckList(generic.ListView):
    """
    displays all public decks
    """
    queryset = Deck.objects.filter(published=1)
    template_name = "deckbuilder/deck_list.html"
    paginate_by = 12

def deckbuilder(request):
    """
    builds a deck as :model:`deckbuilder.Deck`.
    displays card to choose from :model:`card.Cards`

    **Context**
    ``deck_form``
        An instance of :form:`deckbuilder.DeckForm`

    ``cards``
        An instance of :model:`card.Card`.

    **Template:**

    :template:`deckbuilder/deckbuilder.html`
    """
    cards = Card.objects.all()
    deck_form = DeckForm

    if request.method == "POST":
        deck_form = DeckForm(data=request.POST)
        if deck_form.is_valid():
            saved_deck = deck_form.save(commit=False)
            saved_deck.author = request.user
            saved_deck.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Deck saved successfully'
            )
        else :
            messages.add_message(
                request, messages.ERROR,
                'Error while saving deck.'
            )

    deck_form = DeckForm()

    return render(
        request,
        "card/deckbuilder.html",
        {
            "cards": cards,
            "deck_form": deck_form
        },
    )