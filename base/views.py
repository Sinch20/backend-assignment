from pickle import GET
from rest_framework import generics
from types import GenericAlias
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee 
from rest_framework import status
from .serializers import EmployeeSerializer
from .serializers import EmpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .mypagination import MyLimitOffsetPagination 
# Create your views here.



@api_view(['GET','POST'])
def employeeListView(request):
    if(request.method=='GET'):
        employees=Employee.objects.all()
        serializer=EmployeeSerializer(employees, many=True)
        return Response(serializer.data) 
    elif(request.method=='POST'):
        serializer=EmpSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE', 'PUT'])
def userDetail(request, pk):
    if(request.method=='GET'):
        employees=Employee.objects.get(id=pk)
        serializer=EmployeeSerializer(employees, many=False)
        return Response(serializer.data) 
    elif(request.method=='DELETE'):
        employees=Employee.objects.get(id=pk)
        employees.delete()
        return Response("User deleted successfully")
    elif(request.method=='PUT'):
        employees=Employee.objects.get(id=pk)
        serializer=EmpSerializer(employees, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class EmployeeListView(generics.ListAPIView):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    filter_backends=(DjangoFilterBackend, OrderingFilter, SearchFilter)
    filter_fields=('company_name', 'city', 'state', 'zip', 'email', 'age', 'id', 'web', )
    ordering_fields=('company_name', 'city', 'state', 'zip', 'email', 'age', 'id', 'web', )
    search_fields=('first_name','last_name')
    pagination_class=MyLimitOffsetPagination
    
    


   

