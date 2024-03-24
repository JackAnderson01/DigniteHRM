from django.contrib import admin
from .models import Vacancy

# Register your models here.

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'hiring_manager', 'description', 'status']
    list_filter = ['id', 'name', 'role', 'hiring_manager','status']
    search_fields = ['name', 'role', 'hiring_manager']


admin.site.register(Vacancy, VacancyAdmin)