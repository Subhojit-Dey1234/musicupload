from .models import FileUpload,UserDetails
from rest_framework import serializers
from django.contrib.auth.models import User

class SerializerFileUpload(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = "__all__"


class SerializerUserDetails(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = "__all__"