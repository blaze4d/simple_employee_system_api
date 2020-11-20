from rest_framework import serializers
from .models import Employee, EmployeeArchive
from django.contrib.admin.models import LogEntry

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeArchive
        fields = "__all__"

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogEntry
        fields = "__all__"

