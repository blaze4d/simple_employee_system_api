from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import EmployeeSerializer, EmployeeArchiveSerializer, LogSerializer
from .helper import Converter
from django.contrib.admin.models import LogEntry

from .models import Employee, EmployeeArchive

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/employee-list/',
        'Detail View': '/employee-detail/<str:id>/',
        'Create': '/employee-create/',
        'Update': '/employee-update/',
        'Archive': '/employee-archive/<str:id>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def employeeList(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def employeeDetail(request, id):
    employees = Employee.objects.get(id=id)    
    serializer = EmployeeSerializer(employees, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def employeeCreate(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # data is okay and saved successfully. Return status code 200
        return Response(serializer.data,status=200)
    
    # data received is not valid, return status code 400
    return Response(request.data, status=400)

@api_view(['POST'])
def employeeUpdate(request, id):
    employee = Employee.objects.get(id=id)

    # check is employee exists
    if employee is None:
        # employee does not exist. Return status code 404
        return Response("Not found", status=404)

    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=200)

    # data received is not valid, return status code 400
    return Response(request.data, status=400)

@api_view(['DELETE'])
def employeeArchive(request, id):
    employee = Employee.objects.get(id=id)

    # convert the employee object to dict
    arch = Converter.employee_to_archive(employee)    
    archive_serializer = EmployeeArchiveSerializer(data = arch)

    if archive_serializer.is_valid():
        archive_serializer.save()
        employee.delete()
        return Response("Employee archived successfully",status=200)
    
    # data received is not valid, return status code 400
    return Response("Error occured " + str(archive_serializer.errors),status=400)


@api_view(['GET'])
def logList(request):
    logs = LogEntry.objects.all()
    serializer = LogSerializer(logs, many=True)
    return Response(serializer.data)