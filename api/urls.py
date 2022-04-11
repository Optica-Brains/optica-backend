from django.urls import path
from . import views
from .views import MyTokenObtainPairView


# simple JWT url configurations
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns= [
   path('create_user/',views.CreatUserView.as_view()),
   path('branches/',views.BranchList.as_view()),
   path('branches/<int:pk>/',views.BranchDetail.as_view()),
   path('batches/',views.BatchesList.as_view()),
   path('batches/<int:pk>/',views.BatchDetail.as_view()),
   path('users/',views.UsersView.as_view()),
   path('users/<int:pk>/',views.UserDetails.as_view()),
   path('summary/',views.BatchSummary.as_view()),
   path('rider/<int:pk>/',views.RiderDelivery.as_view()),
   path('manager/<int:pk>/',views.ManagerDelivery.as_view()),




   # jwt routes
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]