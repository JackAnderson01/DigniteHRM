from rest_framework import serializers
from .models import Company

class CompanyCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=255),
    address = serializers.CharField(max_length=255),
    phone_number = serializers.CharField(max_length=20),
    email = serializers.EmailField(),
    website = serializers.URLField(),
    industry = serializers.CharField(max_length=50)
    founded_date = serializers.DateField(),
    description = serializers.CharField(),
    logo = serializers.ImageField(),
    banner = serializers.ImageField(), 

    class Meta:
        model = Company
        fields = ["name", "address", "phone_number", "email", "website", "industry", "founded_date","description", "logo", "banner"]


    def validate(self, data):
        if(data['name'] == ""):
            raise serializers.ValidationError("Company name cannot be left empty.")
        if(len(data['name']) < 5):
            raise serializers.ValidationError("Company name must contain more than 4 alphabets.")
        if(data['address'] == ""):
            raise serializers.ValidationError("Company address cannot be left empty.")
        if(len(data['address']) < 10):
            raise serializers.ValidationError("Company address must contain more than 10 alphabets.")
        if(data['phone_number'] == ""):
            raise serializers.ValidationError("Company number cannot be left empty.")
        if(len(data['phone_number']) < 9):
            raise serializers.ValidationError("Company number must contain 9 numbers.")
        if(data['email'] == ""):
            raise serializers.ValidationError("Email cannot be left empty.")
        if(data['website'] == ""):
            raise serializers.ValidationError("Website cannot be left empty.")
        if(data['industry'] == ""):
            raise serializers.ValidationError("Industry cannot be left empty.")
        if(data['founded_date'] == None):
            raise serializers.ValidationError("You must provide date at which you founded the company.")
        if(data['description'] == None or ""):
            raise serializers.ValidationError("You must provide description of the company.")
        
        
        return super().validate(data)
    
class CompanyVerifyAccessSerializer(serializers.ModelSerializer):
    access_key=serializers.CharField()
    id=serializers.UUIDField()

    class Meta:
        model = Company
        fields = ["access_key", "id"]


    