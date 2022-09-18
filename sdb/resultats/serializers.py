from rest_framework import serializers
from formulaire.models import Formulaire
from resultats.models import Resultats


class ResultatsSerializer(serializers.ModelSerializer):
    # formulaire = serializers.ReadOnlyField(source='formulaire.id')

    class Meta:
        model = Resultats
        fields = ['id', 'email', 'responses', 'date', 'duration', 'formulaire',]


class FormulaireSerializer(serializers.ModelSerializer):
    enquete = serializers.ReadOnlyField(source='enquete.id')
    enqueteur = serializers.ReadOnlyField(source='enqueteur.username')
    resultats = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Formulaire
        fields = ['id', 'created', 'titre', 'logo', 'elements', 'sujets', 'enquete', 'enqueteur', 'resultats']