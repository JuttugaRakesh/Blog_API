from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import  UniqueValidator
from .models import BlogPost


class UserSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False)
    username = serializers.CharField(required=True, validators=[UniqueValidator(
        queryset=User.objects.all(), message="Username already exist")])
    email = serializers.EmailField(validators=[UniqueValidator(
        queryset=User.objects.all(), message="Email already exist")])
    password = serializers.CharField(min_length=6, required=True, write_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model=User
        fields=['id','first_name','last_name','username',"email","password","isAdmin"]

    def get_first_name(self, obj):
        return obj.username.capitalize()

    def get_isAdmin(self, obj):
        return obj.is_staff


class BlogPostserializers(serializers.ModelSerializer):
    user_details =UserSerializers(source='user', read_only=True)

    class Meta:
        model=BlogPost
        fields='__all__'