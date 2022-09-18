from rest_framework import serializers
from enquete.models import Enquete

from formulaire.models import Formulaire
from users.models import User


class FormulaireSerializer(serializers.ModelSerializer):
    # resultats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # enquete = serializers.ReadOnlyField(source='enquete.id')
    enqueteur = serializers.ReadOnlyField(source='enqueteur.username')


    class Meta:
        model = Formulaire
        fields = ['id', 'created', 'titre', 'logo', 'elements', 'sujets', 'enquete', 'enqueteur'] 
        # 'resultats'

class EnqueteSerializer(serializers.ModelSerializer):
    formulaires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Enquete
        fields = ['id', 'titre', 'logo', 'formulaires']

class UserSerializer(serializers.ModelSerializer):
    enquetes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    enquetes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'enquetes', 'formulaires']