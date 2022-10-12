from django.shortcuts import render
from rest_framework import generics, serializers
from api.serializer import TodoSerializer
from api.models import Contact

# Create your views here.
class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = TodoSerializer