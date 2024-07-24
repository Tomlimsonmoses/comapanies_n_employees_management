# api/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Company, Department, Employee, EmployeeRole, ProgressTracker, User, AdminUser
from .serializers import (
    CompanySerializer, DepartmentSerializer, EmployeeSerializer,
    EmployeeRoleSerializer, ProgressTrackerSerializer, UserSerializer, AdminUserSerializer
)
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

class ReactView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        # Implement your logic here
        return Response({"message": "Welcome to Talent Verify!"})

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class CompanyListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'company_name'

class DepartmentListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]  # Adjust permissions as needed
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def post(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'department_id'

class EmployeeListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'employee_id_number'

class EmployeeRoleListView(generics.ListCreateAPIView):
    queryset = EmployeeRole.objects.all()
    serializer_class = EmployeeRoleSerializer

class EmployeeRoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeRole.objects.all()
    serializer_class = EmployeeRoleSerializer
    lookup_field = 'role_id'

class ProgressTrackerView(generics.RetrieveUpdateAPIView):
    queryset = ProgressTracker.objects.all()
    serializer_class = ProgressTrackerSerializer
    lookup_field = 'employee__employee_id_number'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Employee, Department

class EmployeesCountView(APIView):
    def get(self, request, *args, **kwargs):
        company_name = request.query_params.get('company')
        if company_name:
            try:
                company = Company.objects.get(company_name=company_name)
                employees_count = Employee.objects.filter(company=company).count()
                return Response({'count': employees_count})
            except Company.DoesNotExist:
                return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Company ID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

class DepartmentsCountView(APIView):
    def get(self, request, *args, **kwargs):
        company_name = request.query_params.get('company')
        if (company_name):
            try:
                company = Company.objects.get(company_name=company_name)
                departments_count = Department.objects.filter(company=company).count()
                return Response({'count': departments_count})
            except Company.DoesNotExist:
                return Response({'error': 'Company not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Company ID parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
