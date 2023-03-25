
from rest_framework import serializers

from bmain.models import Category


class CtgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['slug']





