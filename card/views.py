from django.views import generic
from .models import Card

# Create your views here.

class CardLibrary(generic.ListView):
    queryset = Card.objects.all()
    template_name = "card/card_library.html"