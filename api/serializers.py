from rest_framework import serializers
from rest_framework.decorators import action
from .models import *





class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','batch']





class BatchSerializer(serializers.ModelSerializer):
   class Meta:
        model = Batch
        fields = ['batch_number','departure_time','delivery_time','status','branch_from','branch_to','messenger','branch_staff']


class BranchSerializer(serializers.ModelSerializer):
    batch_branch_to = BatchSerializer(read_only=True,many=True)
    batch_branch_from = BatchSerializer(read_only=True,many=True)
    class Meta:
        model = Branch
        fields = ['id','branch_name','branch_location','batch_branch_from','batch_branch_to']

        # create function for nested serializers
        def create(self,validated_data):
            branches_from_data = validated_data.pop('batch_branch_from')
            branch = Branch.objects.create(**validated_data)
            for branch_from_data in branches_from_data:
                Batch.objects.create(branch=branch,**order_data)
            return branch

        def create(self,validated_data):
            branches_to_data = validated_data.pop('batch_branch_to')
            branch = Branch.objects.create(**validated_data)
            for branch_to_data in branches_to_data:
                Batch.objects.create(branch=branch,**order_data)
            return branch


        # update function for nested serializers
        def update(self,instance,**validated_data):
            batches_from_data = validated_data.pop('batch_branch_from')
            batches = (instance.batch_branch_from).all()
            batches = list(batches)
            instance.branch_name = validated_data.get('branch_name', instance.branch_name)
            instance.branch_location = validated_data.get('branch_location', instance.branch_location)
            instance.save()


        # start changes here 
            for batch_from_data in batches_from_data:
                batch = batches.pop(0)
                batch.departure_time = batch_from_data('departure_time', batch.departure_time)
                batch.save()
            return instance

            # update function for nested serializers
        def update(self,instance,**validated_data):
            batches_to_data = validated_data.pop('batch_branch_to')
            batches = (instance.batch_branch_from).all()
            batches = list(batches)
            instance.branch_name = validated_data.get('branch_name', instance.branch_name)
            instance.branch_location = validated_data.get('branch_location', instance.branch_location)
            instance.save()


        # start changes here 
            for batch_to_data in batches_to_data:
                batch = batches.pop(0)
                batch.delivery_time = batch_from_data('delivery_time', batch.delivery_time)
                batch.save()
            return instance

# BatchSerializer.branch_from = BranchSerializer(read_only= True)
  


class UserSerializer(serializers.ModelSerializer):
    batch_messenger = BatchSerializer(read_only=True,many=True)
    class Meta:
        model = User
        exclude = ['password']


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=50,min_length=6,write_only=True)
    class Meta:
        branch = BranchSerializer(read_only=True)
        model = User
        fields = ['id','email','password','branch']


    def validate(self,attrs):
        email = attrs.get('email','')
        return attrs

    # create user function
    # def create(self,validated_data):
    #     return User.objects.create_user(**validated_data)





