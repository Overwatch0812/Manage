from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from .serializers import studentSerializer
from rest_framework import generics

# Create your views here.
class studentApi(generics.ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer