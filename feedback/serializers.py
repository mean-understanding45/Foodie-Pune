from rest_framework import serializers
from .models import Feedback
class FeedbackSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    desc = serializers.CharField(max_length=100)
    date = serializers.DateField()
    
    def create(self, validate_data):
        return Contact.objects.create(**validate_data)