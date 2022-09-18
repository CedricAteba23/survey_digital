from django.db import models

from formulaire.models import Formulaire


class Resultats(models.Model):
    email = models.EmailField(max_length = 254)
    responses = models.CharField(max_length=9000, default='')
    date = models.DateTimeField(auto_now=True)
    duration = models.DurationField()
    formulaire = models.ForeignKey(Formulaire, related_name='resultats', on_delete=models.CASCADE)
