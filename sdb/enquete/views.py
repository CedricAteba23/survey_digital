from rest_framework import generics
from enquete import permissions, serializers
# from django_filters.rest_framework import DjangoFilterBackend
from enquete.models import Enquete
from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.decorators import login_required


class EnqueteList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Enquete.objects.all()
    serializer_class = serializers.EnqueteSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['type']

    def perform_create(self, serializer):
        serializer.save(enqueteur=self.request.user)

class EnqueteDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsOwnerOrReadOnly, IsAuthenticated,)
    queryset = Enquete.objects.all()
    serializer_class = serializers.EnqueteSerializer