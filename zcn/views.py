from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Category, Product

from .serializers import CategorySerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Create your views here.



def index(req):
    return HttpResponse('Hi from ZCN index')


@api_view(['GET', 'POST'])
def product(req):
    if req.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif req.method == 'POST':
        serializer = ProductSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'message': f"Student {serializer.validated_data.get('product_name')} saved successfully!"
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
