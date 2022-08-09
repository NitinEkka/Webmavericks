from django.urls import path
from . import views
from .views import ClientTool, ManagerTool, EmployeeTool

urlpatterns = [
    path("", ClientTool.as_view()),
    path("manager/", ManagerTool.as_view()),
    path("Employee/", EmployeeTool.as_view()),

]