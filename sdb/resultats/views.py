from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from resultats import serializers
from .models import Resultats
# from django.contrib.auth.decorators import login_required


class ResultatsList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Resultats.objects.all()
    serializer_class = serializers.ResultatsSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['type']

    # def perform_create(self, serializer):
        # serializer.save(formulaire=self.request.user)
        # serializer.save(enqueteur=self.request.user)
    

class ResultatsDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsOwnerOrReadOnly, IsAuthenticated,)
    queryset = Resultats.objects.all()
    serializer_class = serializers.ResultatsSerializer
