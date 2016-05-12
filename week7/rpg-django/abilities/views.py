from rest_framework import viewsets
from .models import Ability
from .serializers import AbilitySerializer


class AbilitiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows abilities to be viewed or edited.
    """
    queryset = Ability.objects.all().order_by('name')
    serializer_class = AbilitySerializer
