from rest_framework import serializers
from .models import Company, Department, Employee, EmployeeRole, ProgressTracker, User, AdminUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_admin', 'is_employee']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class AdminUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    company = CompanySerializer()

    class Meta:
        model = AdminUser
        fields = ['user', 'company']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        company_data = validated_data.pop('company')
        user = User.objects.create(**user_data)
        company = Company.objects.create(**company_data)
        admin_user = AdminUser.objects.create(user=user, company=company)
        return admin_user

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class EmployeeRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeRole
        fields = '__all__'

class ProgressTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgressTracker
        fields = '__all__'
        read_only_fields = ('updated_at',)
