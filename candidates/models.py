from django.db import models
import uuid
from vacancy.models import Vacancy

# Create your models here.
PROGRESS_CHOICES = (
    ("APPLICATION_INITIATED", "application_initiated"),
    ("SHORTLISTED", "shortlisted"),
    ("REJECTED", "rejected"),
    ("INTERVIEW_SCHEDULED", "interview_scheduled"),
    ("INTERVIEW_PASSED", "interview_passed"),
    ("INTERVIEW_FAILED", "interview_failed"),
    ("JOB_OFFERED", "job_offered"),
    ("OFFER_DECLINED", "offer_declined"),
    ("PERSONAL_ISSUES", "personal_issues"),
    ("HIRED", "hired"),
)

class Candidate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='vacancy')
    candidate_name = models.CharField(max_length=70, null=False, blank=False)
    candidate_email = models.EmailField(max_length=100, null=False, blank=False)
    resume = models.FileField(upload_to='candidate_files/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.candidate_name