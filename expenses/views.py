from email import message
from expenses.models import Expense
from expenses.serializers import ExpenseSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .utils import IsOwnerOrReadOnly 
from authentication.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request , format=None):

    return Response({
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'expense': reverse('expense-list', request=request, format=format),
        'income': reverse('income-list', request=request, format=format)
    })


class ExpenseList(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    



class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
 
    