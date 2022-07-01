from .views import ExpenseList, ExpenseDetail
from django.urls import path



urlpatterns = [
    path('', ExpenseList.as_view(), name='expense-list'),
    path('detail/<str:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
  
    
]
