from .serializers import CondutorSerializer
from .models import Condutor
from rest_framework import viewsets

class CondutorView(viewsets.ModelViewSet):
    queryset = Condutor.objects.all()
    serializer_class = CondutorSerializer
