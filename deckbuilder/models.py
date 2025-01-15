from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Private"), (1, "Public"))

# Create your models here.
class Deck(models.Model):
    deck_name = models.CharField(max_length=20)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saved_decks"
    )
    deck_list = models.TextField()
    published = models.IntegerField(choices=STATUS, default=0)
    additional_info = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-updated_on"]
    def __str__(self):
        return f"{self.deck_name}"