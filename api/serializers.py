from rest_framework import serializers
from rest_framework.decorators import action
from .models import *


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ['id','email','password']


    def validate(self,attrs):
        email = attrs.get('email','')
        return attrs

    # create user function
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','branch','departure_time','delivery_time']


class BranchSerializer(serializers.ModelSerializer):
    order_branch = OrderSerializer(read_only=True,many=True)
    class Meta:
        model = Branch
        fields = ['id','branch_name','branch_location','order_branch']

        # create function for nested serializers
        def create(self,validated_data):
            orders_data = validated_data.pop('order_branch')
            branch = Branch.objects.create(**validated_data)
            for order_data in orders_data:
                Order.objects.create(branch=branch,**order_data)
            return branch

        # update function for nested serializers
        def update(self,instance,**validated_data):
            orders_data = validated_data.pop('order_branch')
            orders = (instance.order_branch).all()
            orders = list(orders)
            instance.branch_name = validated_data.get('branch_name', instance.branch_name)
            instance.branch_location = validated_data.get('branch_location', instance.branch_location)
            instance.save()

            for order_data in orders_data:
                order = orders.pop(0)
                order.departure_time = order_data.get('departure_time', order.departure_time)
                order.delivery_time = order_data.get('delivery_time', order.delivery_time)
                order.save()
            return instance





