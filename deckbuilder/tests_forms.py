from django.test import TestCase
from .forms import DeckForm
from .models import User

class DeckFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')

    def test_deck_form_valid_data(self):
        form = DeckForm(data={
            'deck_name': 'Test Deck',
            'deck_content': '1,2,3',
            'additional_info': 'Some info',
            'published': 1,
        })

        self.assertTrue(form.is_valid())

    def test_deck_form_no_data(self):
        form = DeckForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # Adjust according to required fields
