from email import message
from income.models import Income
from income.serializers import IncomeSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from expenses.utils import IsOwnerOrReadOnly 
from authentication.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication




class IncomeList(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
   

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
    



class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
 
    