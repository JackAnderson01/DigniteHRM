from django.shortcuts import render
from rest_framework.generics import *
from . import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from employee.models import Employee
from django.db.utils import IntegrityError

# Create your views here.
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

    