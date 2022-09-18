from rest_framework import serializers
from users.models import User
from enquete.models import Enquete


class EnqueteSerializer(serializers.ModelSerializer):
    formulaires = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    enqueteur = serializers.ReadOnlyField(source='enqueteur.username')

    class Meta:
        model = Enquete
        fields = ['id', 'created', 'titre', 'type', 'statut' , 'description', 'enqueteur', 'formulaires',]


class UserSerializer(serializers.ModelSerializer):
    enquetes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'enquetes']