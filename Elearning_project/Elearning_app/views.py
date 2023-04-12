# from django.shortcuts import render
# from .models import Product
# from rest_framework import generics
# from .serializers import ProductSerializer
# # Create your views here.
# class ProductListView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class=ProductSerializer
#     """Cette methode est une surcharge"""
#     def get_queryset(self):
#         return super().get_queryset()