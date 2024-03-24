from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display=['id', 'owner', 'name']
# Register your models here.
admin.site.register(Company, CompanyAdmin)