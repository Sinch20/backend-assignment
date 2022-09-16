from cProfile import Profile
from rest_framework import serializers
from base.models import Employee

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['company_name', 'city', 'state', 'zip', 'email', 'age', 'id', 'web']

class EmployeeSerializer(serializers.Serializer):
    id=  serializers.IntegerField()
    first_name= serializers.CharField(max_length=70)
    last_name = serializers.CharField(max_length=70)
    company_name = serializers.CharField(max_length=70)
    city = serializers.CharField(max_length=70)
    state= serializers.CharField(max_length=70)
    zip=  serializers.IntegerField()
    email=  serializers.EmailField()   
    web= serializers.CharField(max_length=100)
    age=  serializers.IntegerField()

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields='__all__'