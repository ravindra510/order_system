from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from orders.decorator import customer_permission_required
from .models import Order, Product, PlatformApiCall
from .serializers import OrderSerializer, ProductSerializer , PlatformApiCallSerializer
# from django.db.models import Prefetch
from .tasks import daily_task  # Celery task import
from functools import wraps
from django.http import HttpResponseForbidden
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


# Order CRUD View
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()  
    # queryset = Order.objects.all().select_related('customer').prefetch_related('products')
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated]
    @customer_permission_required
    def get_queryset(self):
        customer = self.request.user.customer
        queryset = Order.objects.filter(customer=customer)
        
        # Product filtering
        product_name = self.request.query_params.get('product_name', None)
        if product_name:
            queryset = queryset.filter(products__name__icontains=product_name)

        order_by = self.request.query_params.get('order_by', None)
        if order_by == 'asc':
            queryset = queryset.order_by('amount')
        elif order_by == 'desc':
            queryset = queryset.order_by('-amount')
        elif order_by == 'top5':
            queryset = queryset.order_by('-amount')[:5]

        return queryset

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        if Product.objects.filter(name=name).exists():
            return Response({"detail": "Product with this name already exists."}, status=400)
        return super().create(request, *args, **kwargs)

class PlatformApiCallViewSet(viewsets.ModelViewSet):
    queryset = PlatformApiCall.objects.all()
    serializer_class = PlatformApiCallSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def make_api_call(self, request, pk=None):
        platform_api_call = self.get_object()
        response_data = {"status": "success"} 
        platform_api_call.response_data = response_data
        platform_api_call.save()
        return Response({"message": "API call made successfully", "response": response_data})
    
