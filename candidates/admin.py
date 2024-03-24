from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display=['id', 'candidate_name', 'candidate_email', 'resume']
    list_filter=['id', 'candidate_name', 'candidate_email']
    search_fields = ['candidate_name', 'candidate_email']

# Register your models here.
admin.site.register(Candidate, CandidateAdmin)