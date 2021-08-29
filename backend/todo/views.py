from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .serializers import PersonSerializer
from .serializers import PayCheckSerializer
from .models import Todo
from .models import Person
from .models import PayCheck
import openpyxl
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

from rest_framework import generics

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PayCheckView(viewsets.ModelViewSet):
    queryset = PayCheck.objects.all()
    serializer_class = PayCheckSerializer