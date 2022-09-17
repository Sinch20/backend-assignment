from rest_framework import serializers
from base.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Item
        fields='__all__'

class EmployeeSerializer(serializers.ModelSerializer):

    first_name= serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=70)
    company_name = serializers.CharField(max_length=70)
    city = serializers.CharField(max_length=70)
    state= serializers.CharField(max_length=70)
    zip=  serializers.IntegerField()
    email=  serializers.EmailField()   
    web= serializers.CharField(max_length=100)
    age=  serializers.IntegerField()