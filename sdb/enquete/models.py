from django.db import models
from django.conf import settings

from users.models import User

class Enquete(models.Model):
    titre = models.CharField(max_length=100, blank=True, default='')
    type = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    created = models.DateField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='En cours')
    enqueteur = models.ForeignKey(User, related_name='enquetes', on_delete=models.CASCADE)


    class Meta:
        ordering = ['created']