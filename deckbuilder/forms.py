from .models import Deck
from django import forms


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ("deck_name","deck_content","additional_info","published",)
