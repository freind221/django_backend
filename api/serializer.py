from rest_framework import serializers
from api.models import Contact

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
    
        model = Contact
        fields = '__all__'