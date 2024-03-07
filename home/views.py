from django.shortcuts import render
from .models import test
from .serializers import TestSerializer
from rest_framework import viewsets

# Create your views here.


class home(viewsets.ModelViewSet):
    queryset = test.objects.all()
    serializer_class = TestSerializer
