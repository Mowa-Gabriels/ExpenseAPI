
from cgitb import lookup
from expenses.models import Expense
from authentication.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



class ExpenseSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='expense-detail', format='html')

    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Expense
        fields = '__all__'
        