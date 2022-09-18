from rest_framework import generics
from enquete import permissions, serializers
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from formulaire import serializers
from formulaire.models import Formulaire
# from django.contrib.auth.decorators import login_required


class FormulaireList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Formulaire.objects.all()
    serializer_class = serializers.FormulaireSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['type']

    def perform_create(self, serializer):
        # serializer.save(enquete=self.request.user)
        serializer.save(enqueteur=self.request.user)

class FormulaireDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsOwnerOrReadOnly, IsAuthenticated,)
    queryset = Formulaire.objects.all()
    serializer_class = serializers.FormulaireSerializer

