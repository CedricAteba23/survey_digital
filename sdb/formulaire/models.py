from distutils.command.upload import upload
from email.policy import default
from django.db import models
from enquete.models import Enquete

from users.models import User

def upload_path(instance, filename):
    return '/'.join(['logos', str(instance.titre), filename])

class Formulaire(models.Model):
    titre = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(blank=True, null=True, default='', upload_to=upload_path)
    elements = models.CharField(max_length=9000, default='')
    sujets = models.CharField(max_length=9000, default='')
    enqueteur = models.ForeignKey(User, related_name='formulaires', on_delete=models.CASCADE) 
    enquete = models.ForeignKey(Enquete, related_name='formulaires', on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created']