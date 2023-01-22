from rest_framework import serializers
from .models import Product, Category, Seller, Callback, Rating, Order, Basket

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = '__all__'

class CallbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Callback
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = '__all__'
