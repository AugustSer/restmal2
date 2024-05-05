from rest_framework import serializers
from .models import Director, Administrator, User, Order


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('id', 'name', 'job_title')


class AdministratorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Administrator
        fields = ('id', 'name', 'years_old', 'contact_number', 'data_passport')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'visitor')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'user', 'status')

