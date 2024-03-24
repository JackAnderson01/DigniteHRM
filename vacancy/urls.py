from django.urls import path
from .views import VacancyCreateView, VacancyListView, VacancyUpdateView, VacancyStatusUpdateView, VacancyDeleteView, VacancyRetrieveView


urlpatterns = [
    path("create", VacancyCreateView.as_view(), name="CreateVacancy"),
]