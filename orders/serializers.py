from rest_framework import serializers
from .models import Order, Product, Customer, Seller, PlatformApiCall

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'amount']

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    seller = serializers.StringRelatedField()
    products = ProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'seller', 'products', 'amount']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'mobile']

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'name', 'mobile']

class PlatformApiCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformApiCall
        fields = ['id', 'user', 'requested_url', 'requested_data', 'response_data']


