from rest_framework import serializers
from users.models import Outlet


class OutletSerializer(serializers.Serializer):
    outletname = serializers.CharField(max_length=30)
    foodyype = serializers.CharField(max_length=20)
    ownerfirstname = serializers.CharField(max_length=20)
    ownerlastname = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=200)
    addresslink = serializers.URLField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=30)

    def create(self, validate_data):
        return Outlet.objects.create(**validate_data)
