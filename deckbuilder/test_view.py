from django.test import TestCase
from django.urls import reverse
from .models import Deck, User
from card.models import Card

class DeckDetailViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.card1 = Card.objects.create(card_id='1', name='Test Card 1')
        self.card2 = Card.objects.create(card_id='2', name='Test Card 2')
        self.deck = Deck.objects.create(
            deck_name='Test Deck',
            author=self.user,
            deck_content=f'{self.card1.card_id},{self.card2.card_id}',
            published=1
        )

    def test_deck_detail_view(self):
        response = self.client.get(reverse('deck_detail', args=[self.deck.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'deckbuilder/deck_detail.html')
        self.assertContains(response, self.card1.name)
        self.assertContains(response, self.card2.name)

class MyDecksViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.other_user = User.objects.create_user(username='otheruser', password='12345')
        self.client.login(username='testuser', password='12345')
        
        self.user_deck = Deck.objects.create(
            deck_name='User Deck',
            author=self.user,
            deck_content='1,2,3',
            published=1
        )
        
        self.other_user_deck = Deck.objects.create(
            deck_name='Other User Deck',
            author=self.other_user,
            deck_content='4,5,6',
            published=1
        )

    def test_my_decks_view(self):
        response = self.client.get(reverse('my_decks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'deckbuilder/my_decks.html')
        self.assertContains(response, self.user_deck.deck_name)
        self.assertNotContains(response, self.other_user_deck.deck_name)


class DeckbuilderViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.card1 = Card.objects.create(card_id='1', name='Test Card 1')
        self.card2 = Card.objects.create(card_id='2', name='Test Card 2')
        self.card3 = Card.objects.create(card_id='3', name='Test Card 3')
        self.client.login(username='testuser', password='12345')

    def test_deckbuilder_view_get(self):
        response = self.client.get(reverse('deckbuilder'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'deckbuilder/deckbuilder.html')

    def test_deckbuilder_view_post_valid_data(self):
        data = {
            'deck_name': 'Test Deck',
            'deck_content': f'{self.card1.card_id},{self.card2.card_id},{self.card3.card_id}',
            'additional_info': 'Some info',
            'published': 1,
        }
        response = self.client.post(reverse('deckbuilder'), data)
        self.assertEqual(response.status_code, 302)  # Redirect after saving

    def test_deckbuilder_view_post_invalid_data(self):
        data = {
            'deck_name': '',  # Invalid: Empty deck_name
            'deck_content': '',
            'additional_info': '',
            'published': '',
        }
        response = self.client.post(reverse('deckbuilder'), data)
        self.assertEqual(response.status_code, 200)  # Form errors should return the same page
        self.assertFormError(response, 'deck_form', 'deck_name', 'This field is required.')

class EditDeckViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.card1 = Card.objects.create(card_id='1', name='Test Card 1')
        self.card2 = Card.objects.create(card_id='2', name='Test Card 2')
        self.deck = Deck.objects.create(
            deck_name='Test Deck',
            author=self.user,
            deck_content=f'{self.card1.card_id},{self.card2.card_id}',
            published=1
        )
        self.client.login(username='testuser', password='12345')

    def test_edit_deck_view_get(self):
        response = self.client.get(reverse('edit_deck', args=[self.deck.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'deckbuilder/deckbuilder.html')
        self.assertContains(response, self.deck.deck_name)
        self.assertContains(response, self.deck.deck_content)
        self.assertContains(response, self.deck.additional_info)

    def test_edit_deck_view_post(self):
        data = {
            'deck_name': 'Updated Deck',
            'deck_content': f'{self.card1.card_id},{self.card2.card_id}',  # Use valid card IDs
            'additional_info': 'Updated info',
            'published': 1,
        }
        response = self.client.post(reverse('edit_deck', args=[self.deck.id]), data)
        self.assertEqual(response.status_code, 302)  # Redirect after saving



class DeleteDeckViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.deck = Deck.objects.create(
            deck_name='Test Deck',
            author=self.user,
            deck_content='1,2,3',
            published=1
        )
        self.client.login(username='testuser', password='12345')

    def test_delete_deck_view(self):
        response = self.client.post(reverse('delete_deck', args=[self.deck.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after deleting
        self.assertFalse(Deck.objects.filter(id=self.deck.id).exists())
