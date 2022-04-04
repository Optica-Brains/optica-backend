from rest_framework import serializers
from .models import *


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ['email','password']


    def validate(self,attrs):
        email = attrs.get('email','')
        return attrs

    # create user function
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()
    class Meta:
        model = Order
        fields = ['id','branch','departure','arrival']