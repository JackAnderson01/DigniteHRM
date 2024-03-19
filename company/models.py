import uuid
from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owned_companies')
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(null=False, blank=False)
    website = models.URLField(null=True, blank=True)
    industry = models.CharField(max_length=255, null=False, blank=False)
    founded_date = models.DateField(null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    banner = models.ImageField(upload_to='company_banners/', null=True, blank=True)
    access_key = models.CharField(max_length=255, null=True, blank=True)
    access_key_expiry = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    

    def __str__(self):
        return self.name
    


    def is_company_owner(self, user, company_id):
        try:
            company = Company.objects.filter(id=company_id)
            return company.owner == user
        except Company.DoesNotExist:
            return False