from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class VacancyListView(ListAPIView):
    pass

class VacancyRetrieveView(RetrieveAPIView):
    pass

class VacancyCreateView(CreateAPIView):
    serializer_class = VacancyCreationSerializer

    def post(self, request):
        data=request.data
        serializer = self.serializer_class(data=data)
        if(serializer.is_valid()):
           return Response(data={"message":"Vacancy Created Successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(data={serializer.errors}, status=status.HTTP_201_CREATED)

class VacancyUpdateView(UpdateAPIView):
    pass

class VacancyDeleteView(DestroyAPIView):
    pass

class VacancyStatusUpdateView(UpdateAPIView):
    pass