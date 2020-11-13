from rest_framework import serializers
from .models import UsersModel, OrdersModel


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdersModel
        fields = '__all__'


