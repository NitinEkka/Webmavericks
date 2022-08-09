from django.shortcuts import render
from rest_framework import generics
from .models import Tasks
from .serializers import ClientSerializer , ManagerSerializer , EmployeeSerializer

class ClientTool(generics.ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Tasks.objects.all()

class ManagerTool(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManagerSerializer
    queryset = Tasks.objects.all()

class EmployeeTool(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Tasks.objects.all()


