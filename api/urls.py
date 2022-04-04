from django.urls import path
from . import views

urlpatterns= [
   path('login/',views.LoginView.as_view()),
   path('branches/',views.BranchList.as_view()),
   path('orders/',views.OrderList.as_view()),
   path('orders/<int:pk>/',views.OrderDetail.as_view()),
]