# api/urls.py

from django.urls import path
from .views import (
    CompanyListView,
    CompanyDetailView,
    EmployeeListView,
    EmployeeDetailView,
    EmployeeRoleListView,
    EmployeeRoleDetailView,
    DepartmentListView,
    DepartmentDetailView,
    RegisterView,
    LoginView,
    ProgressTrackerView,
    EmployeesCountView, 
    DepartmentsCountView
)

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Companies URLs
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<str:company_name>/', CompanyDetailView.as_view(), name='company-detail'),
    path('companies/create/', CompanyListView.as_view(), name='company-create'),
    path('companies/update/<str:company_name>/', CompanyDetailView.as_view(), name='company-update'),

    # Departments URLs
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<str:department_id>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/<str:company_name>/create/', DepartmentListView.as_view(), name='department-create'),

    # Employees URLs
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path('employees/<str:employee_id_number>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/create/', EmployeeListView.as_view(), name='employee-create'),

    # Employee Roles URLs
    path('employeeroles/', EmployeeRoleListView.as_view(), name='employeerole-list'),
    path('employeeroles/<int:pk>/', EmployeeRoleDetailView.as_view(), name='employeerole-detail'),
    path('employeeroles/create/', EmployeeRoleListView.as_view(), name='employeerole-create'),
    path('employeeroles/update/<int:pk>/', EmployeeRoleDetailView.as_view(), name='employeerole-update'),

    # Progress Tracker URLs
    path('progress/', ProgressTrackerView.as_view(), name='progress-list'),
    path('progress/<int:pk>/', ProgressTrackerView.as_view(), name='progress-detail'),

    # New URLs for employee and department counts
    path('employees/count/', EmployeesCountView.as_view(), name='employee-count'),
    path('departments/count/', DepartmentsCountView.as_view(), name='department-count'),
]
