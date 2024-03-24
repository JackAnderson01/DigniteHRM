from rest_framework import serializers
from .models import Vacancy


class VacancyCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=300)
    company = serializers.UUIDField()
    role = serializers.UUIDField()
    hiring_manager = serializers.UUIDField()
    description = serializers.CharField(max_length=2500)


    class Meta:
        model=Vacancy
        fields=['name', 'description', 'company' ,'role', 'hiring_manager']

class VacancyUpdateSerializer(serializers.ModelSerializer):
    pass

class VacancyDeleteSerializer(serializers.ModelSerializer):
    pass

class VacancyListSerializer(serializers.ModelSerializer):
    pass


STATUS_CHOICES = (
    ("ACTIVE", "active"),
    ("CLOSED", "closed"),
)
class UpdateVacancyStatus(serializers.ModelSerializer):
    id=serializers.UUIDField()
    status = serializers.ChoiceField(choices=STATUS_CHOICES)

    class Meta:
        model=Vacancy
        fields = ['id', 'status']
