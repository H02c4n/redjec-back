from rest_framework import serializers
from .models import Category, Product





class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        #fields = ['category_name']
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):

    total = serializers.SerializerMethodField()

    class Meta:
        model = Product
        #fields = ['category', 'product_name', 'quantity', 'price', 'total']
        fields = '__all__'


    def get_total(self, obj):
        return obj.quantity * obj.price