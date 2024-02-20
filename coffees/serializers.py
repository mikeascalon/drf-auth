from rest_framework import serializers
from .models import Coffee

class CoffeeSerializer(serializers.ModelSerializer):

  price = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

  class Meta:
    fields = ("id","owner","name","description","price","created_at")
    model = Coffee