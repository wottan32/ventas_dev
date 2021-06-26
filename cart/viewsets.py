from rest_framework import viewsets
from .import models
from .import serializers

from django.conf import settings

from .serializers import AddressSerializer, CategorySerializer, ColourVariationSerializer, OrderItemSerializer, ProductSerializer, PaymentSerializer, OrderSerializer, SizeVariationSerializer
from .models import ColourVariation, Product, OrderItem, Address, Order, Category, Payment, SizeVariation


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class ColourVariationViewSet(viewsets.ModelViewSet):
    queryset = ColourVariation.objects.all()
    serializer_class = ColourVariationSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SizeVariationViewSet(viewsets.ModelViewSet):
    queryset = SizeVariation.objects.all()
    serializer_class = SizeVariationSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer




