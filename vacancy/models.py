from django.db import models
import uuid
from employee.models import Role, Employee

# Create your models here.

STATUS_CHOICES = (
    ("ACTIVE", "active"),
    ("CLOSED", "closed"),
)


class Vacancy(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=300, null=False, blank=False)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, related_name='vacancy_role')
    hiring_manager = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='hiring_manager')
    description = models.TextField(max_length=2500)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
