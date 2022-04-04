from django.urls import path
from . import views
from .views import MyTokenObtainPairView


# simple JWT url configurations
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns= [
   path('login/',views.LoginView.as_view()),
   path('branches/',views.BranchList.as_view()),
   path('orders/',views.OrderList.as_view()),
   path('orders/<int:pk>/',views.OrderDetail.as_view()),

   # jwt routes
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]