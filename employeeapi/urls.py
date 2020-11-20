from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('employee-list', views.employeeList, name="employee-list"),
    path('employee-detail/<str:id>', views.employeeDetail, name="employee-detail"),
    path('employee-create', views.employeeCreate, name="employee-create"),
    path('employee-update/<str:id>', views.employeeUpdate, name="employee-update"),
    path('employee-archive/<str:id>', views.employeeArchive, name="employee-archive"),
    path('log-list', views.logList, name="log-list")
]