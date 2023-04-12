from rest_framework import serializers
from todoapp.models import product


class productseralizer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = '__all__'
