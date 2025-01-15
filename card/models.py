from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Card(models.Model):
    card_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    card_image = CloudinaryField('image', default='placeholder')