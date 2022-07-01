
from cgitb import lookup
from income.models import Income
from authentication.models import User
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField



class IncomeSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='income-detail', format='html')

    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Income
        fields = '__all__'
        