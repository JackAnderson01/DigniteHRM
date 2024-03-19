import uuid
from django.db import models
from django.conf import settings
from company.models import Company

# Create your models here.
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    join_date = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to='employee_image/', null=True, blank=True)
    documents = models.FileField(upload_to='employee_files/', null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    additional_information = models.TextField(null=True, blank=True)

    def is_hr_manager(self):
        return self.role.name == 'HR Manager'

    def is_hr_intern(self):
        return self.role.name == 'HR Intern'

    def is_manager(self):
        # Assuming 'Manager' is a role name
        return self.role.name == 'Manager'

    def is_team_lead(self):
        # Assuming 'Team Lead' is a role name
        return self.role.name == 'Team Lead'

    def is_normal_employee(self):
        # Assuming 'Normal Employee' is a role name
        return self.role.name == 'Normal Employee'
    

    def __str__(self):
        return self.user.name
