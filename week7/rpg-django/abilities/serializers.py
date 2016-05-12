from rest_framework import serializers
from .models import Ability


class AbilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ability
        fields = ('url', 'name', 'damage', 'icon', 'rarity')
