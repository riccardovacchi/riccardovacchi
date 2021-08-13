from django.db import models

# Create your models here.
class Rolls(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    prezzo = models.FloatField()
    