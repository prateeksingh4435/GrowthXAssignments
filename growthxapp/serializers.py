from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User , UploadAssigment

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True, 'validators': [validate_password]},
            'email': {'required': True, 'validators': [UniqueValidator(queryset=User.objects.all())]},
            'user_type': {'required': True},
        }

    def create(self, validated_data):
        user = User(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        
class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
       
        exclude = (
            'password', 'last_login', 'is_active', 'is_superuser', 'is_staff',
            'groups', 'user_permissions', 'date_joined', 
        )
        
        
class Alladmins(serializers.ModelSerializer):
    class Meta:
        model = User
        
        exclude = (
            'password', 'last_login', 'is_active', 'is_superuser', 'is_staff',
            'groups', 'user_permissions', 'date_joined','username',
        )
        
        
class UploadAssignmentSerializer(serializers.ModelSerializer):
    Tagadmin = serializers.CharField()  
    userobj = serializers.CharField()
    class Meta:
        model = UploadAssigment
        fields = ('userobj', 'task', 'Tagadmin')

  
    
    
class UploadAssignmentAnotherSerializer(serializers.ModelSerializer):

    class Meta:
        model = UploadAssigment
        fields = ('id','userobj', 'task')
