from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from employee.models import Employee
from django.db.utils import IntegrityError
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class CompanyVerifyAccessKeyView(APIView):
    

    def post(self, request):
        data = request.data

        # custom validations:
        if 'access_key' not in data:
            return Response(data={"error": "Access Key is required."}, status=status.HTTP_400_BAD_REQUEST)
        if(data['access_key'] == ""):
            return Response(data={"error": "Access Key cannot be left empty."}, status=status.HTTP_400_BAD_REQUEST)
        if(data['access_key'] == None):
            return Response(data={"error": "Access Key is required."}, status=status.HTTP_400_BAD_REQUEST)
        if 'id' not in data:
            return Response(data={"error": "Company Id is required."}, status=status.HTTP_400_BAD_REQUEST)
        if(data['id'] == ""):
            return Response(data={"error": "Id must be provided."}, status=status.HTTP_400_BAD_REQUEST)
        if(data['id'] == None):
            return Response(data={"error": "Company Id is required."}, status=status.HTTP_400_BAD_REQUEST)


        company = Company.objects.filter(access_key=data['access_key'], id=data['id'])
        if(company.exists()):
            
            # If user has already verified an access_key
            if(company.first().is_verified and timezone.now() < company.first().access_key_expiry):
                return Response(data={"error": f"Access Key already verified."}, status=status.HTTP_401_UNAUTHORIZED)

             # If access_key has expired sending an error:
            if(company.first().access_key_expiry and timezone.now() > company.first().access_key_expiry):
                return Response(data={"error": f"Access Key expired. Please try relogin."}, status=status.HTTP_401_UNAUTHORIZED)

            company.update(is_verified=True, access_key_expiry=datetime.now() + timedelta(days=1))
            refresh = RefreshToken.for_user(company.first().owner)
            return Response(data={"message": "Access Key Verified.", "name":company.first().name, 'refresh': str(refresh), 'access': str(refresh.access_token), 'logo': f"{company.first().logo}" }, status=status.HTTP_200_OK)
        return Response(data={"error": "Invalid Access Key"}, status=status.HTTP_401_UNAUTHORIZED)

        

class CompanyCreateView(CreateAPIView):
    serializer_class = serializers.CompanyCreationSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=request.data)
        user = request.user

        is_user_employee = Employee.objects.filter(user=user)
        if(is_user_employee.exists()):
            return Response(data={"error": "Employee cannot register a company with his official email."}, status=status.HTTP_401_UNAUTHORIZED)

        
        if serializer.is_valid():
            try:
                approved_company = Company.objects.filter(owner=request.user, is_approved=True)
                unapproved_company = Company.objects.filter(owner=request.user, is_approved=False)
                if(approved_company):
                    return Response({"error": "A company with this owner already exists."}, status=status.HTTP_400_BAD_REQUEST)
                
                if(unapproved_company):
                    return Response({"error": "Admin has not yet approved your company."}, status=status.HTTP_400_BAD_REQUEST)
                
                Company.objects.create(owner=request.user ,name = serializer.validated_data.get('name'), address = serializer.validated_data.get('address'), phone_number = serializer.validated_data.get('phone_number'), email = serializer.validated_data.get('email'), website = serializer.validated_data.get('website'), industry = serializer.validated_data.get('industry'), founded_date = serializer.validated_data.get('founded_date'), description = serializer.validated_data.get('description'), logo = serializer.validated_data.get('logo'), banner = serializer.validated_data.get('banner'), 
                            )
                return Response(data={"data": serializer.validated_data}, status=status.HTTP_200_OK)
            except IntegrityError as e:
                # Check if the error is due to a UNIQUE constraint violation
                if 'UNIQUE constraint' in str(e):
                    return Response({"error": "A company with this owner already exists."}, status=status.HTTP_400_BAD_REQUEST)
                # Handle other types of IntegrityError or database errors
                else:
                    return Response({"error": "An error occurred while creating the company."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                # Handle other types of exceptions
                return Response({"error": "An error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

        return Response(data={"error" :serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    