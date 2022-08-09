from rest_framework import serializers
from .models import Tasks

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['Title', 'Description', 'Task']


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('__all__')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['Employee', 'Status']
