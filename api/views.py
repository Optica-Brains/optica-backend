from django.forms.models import model_to_dict
from django.shortcuts import render
from rest_framework import generics,status,permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .permissions import IsManagerOrReadOnly
from rest_framework.decorators import APIView



# Create your views here.
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['id'] = user.id
        token['full_name'] = user.full_name
        token['branch'] = model_to_dict(user.branch) if user.branch else {}
        token['roles'] = list(user.groups.all().values())
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CreatUserView(generics.GenericAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsManagerOrReadOnly]

    serializer_class = CreateUserSerializer

    # handle user post data
    def post(self,request):
        user = request.data
        # send user data to the serializer
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        return Response(user_data,status=status.HTTP_201_CREATED)


class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# branch view
class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BatchesList(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

class BatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


# total batches view function
class BatchSummary(APIView):
    def get(self, request):
        delivered = Batch.total_deliveries('delivered')
        batches = Batch.total_batches()
        dispatched = Batch.total_deliveries('dispatched')
        return Response({
            'batches': batches,
            'delivered' : delivered,
            'dispatched' : dispatched
        })


class ManagerDelivery(APIView):
    def get(self,request,pk):
        manager_delivery = Batch.objects.filter(id=pk).first().manager_delivery()
        serializer = BatchSerializer(manager_delivery)
        
        if manager_delivery:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_201_CREATED)


class RiderDelivery(APIView):
    def get(self,request,pk):
        print(Batch.objects.filter(id=pk))
        batch = Batch.objects.filter(id=pk).first().rider_delivery()
        serializer = BatchSerializer(batch)

        if batch:
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_201_CREATED)