from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)

# Company model
class Company(models.Model):
    company_name = models.CharField(max_length=255, primary_key=True)
    date_of_registration = models.DateField()
    company_registration_number = models.CharField(max_length=100)
    address = models.TextField()
    contact_person = models.CharField(max_length=100)
    number_of_employees = models.IntegerField()
    contact_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.company_name

# Admin user model
class AdminUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.user.username

# Department model
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.department_name

# Employee model
class Employee(models.Model):
    employee_id_number = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    email_address = models.EmailField()
    contact_phone = models.CharField(max_length=20)
    hire_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class EmployeeRole(models.Model):
    role_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='roles')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    date_started = models.DateField()
    date_left = models.DateField(null=True, blank=True)
    duties = models.TextField()

    def __str__(self):
        return f"{self.employee.name} - {self.role}"




# Progress Tracker model
class ProgressTracker(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='progress_tracker')
    progress = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee.user.username}'s Progress Tracker"

