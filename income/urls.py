from .views import IncomeList, IncomeDetail
from django.urls import path



urlpatterns = [
    path('', IncomeList.as_view(), name='income-list'),
    path('detail/<str:pk>/', IncomeDetail.as_view(), name='income-detail'),
  
    
]
