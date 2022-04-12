from rest_framework import serializers
from rest_framework.decorators import action
from .models import *





class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_number']

# To be showed in batch serialize only
class UserShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','full_name']

class BranchShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BatchSerializer(serializers.ModelSerializer):
   batch_orders = OrderSerializer(many=True)
   messenger = UserShowSerializer(read_only=True)
   branch_to = BranchShowSerializer(read_only=True)
   branch_from = BranchShowSerializer(read_only=True)
   branch_staff = UserShowSerializer(read_only=True)

   branch_to_id = serializers.IntegerField(required=False)
   branch_from_id = serializers.IntegerField()
   messenger_id = serializers.IntegerField(required=False)
   branch_staff_id = serializers.IntegerField(required=False)

   def create(self,validated_data):
        orders_data = validated_data.pop('batch_orders')

        batch = Batch.objects.create(**validated_data)

        for order_data in orders_data:
            Order.objects.create(batch=batch,**order_data)
        return batch

   class Meta:
        model = Batch
        fields='__all__'
        # fields = ['branch_to_id','id','batch_orders','batch_number','departure_time','delivery_time','status','branch_from','branch_to','messenger','branch_staff']


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
                Batch.objects.create(branch=branch,**branch_from_data)
            return branch

        def create(self,validated_data):
            branches_to_data = validated_data.pop('batch_branch_to')
            branch = Branch.objects.create(**validated_data)
            for branch_to_data in branches_to_data:
                Batch.objects.create(branch=branch,**branch_to_data)
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
                batch.delivery_time = batch_to_data('delivery_time', batch.delivery_time)
                batch.save()
            return instance

# BatchSerializer.branch_from = BranchSerializer(read_only= True)
  


class UserSerializer(serializers.ModelSerializer):
    batch_messenger = BatchSerializer(read_only=True,many=True)
    password = serializers.CharField(
        min_length=6, write_only=True, required=True)
    class Meta:
        model = User
        fields = '__all__'

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





