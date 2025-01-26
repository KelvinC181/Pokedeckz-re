from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Card

# Create your views here.


class CardLibrary(generic.ListView):
    """
    Dispalys the card library
    """
    queryset = Card.objects.all()
    template_name = "card/card_library.html"


def card_detail(request, card_id):
    """
    Display an individual :model:`card.Card`.

    **Context**

    ``card``
        An instance of :model:`card.Card`.

    **Template:**

    :template:`card/card_detail.html`
    """
    queryset = Card.objects.all()
    card = get_object_or_404(queryset, card_id=card_id)

    return render(
        request,
        "card/card_detail.html",
        {"card": card},
    )