from rest_framework.viewsets import ModelViewSet
from django.shortcuts import redirect, render
from .models import Basket, Callback, Category, Order, Product, Rating, Seller
from .serializers import  CategorySerializer, SellerSerializer, CallbackSerializer, ProductSerializer, RatingSerializer, BasketSerializer, OrderSerializer
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework
from django.db.models import Q


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delProd(self,request, pk=None):
        product=self.queryset.get(id=pk)
        product.delete()
        return Response('Удалено')



class OrdertViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delOrder(self,request, pk=None):
        order=self.queryset.get(id=pk)
        order.delete()
        return Response('Удалено')



class GetProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title']

class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delBasket(self,request, pk=None):
        basket=self.queryset.get(id=pk)
        basket.delete()
        return Response('Удалено')




class CallbackViewSet(ModelViewSet):
    queryset = Callback.objects.all()
    serializer_class = CallbackSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delCall(self,request, pk=None):
        callback=self.queryset.get(id=pk)
        callback.delete()
        return Response('Удалено')


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delCat(self,request, pk=None):
        category=self.queryset.get(id=pk)
        category.delete()
        return Response('Удалено')



class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delRat(self,request, pk=None):
        rating=self.queryset.get(id=pk)
        rating.delete()
        return Response('Удалено')



class SellerViewSet(ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    @action(methods=['Delete'], detail=True, url_path='delete')
    def delSell(self,request, pk=None):
        seller=self.queryset.get(id=pk)
        seller.delete()
        return Response('Удалено')


class GetOrderView(ListAPIView):
    queryset = Order.objects.filter(Q(total__gt=100000) & Q(total=100000) )
    serializer_class = OrderSerializer

