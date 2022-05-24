from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.generic import TemplateView
from . import models, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# Create your views here.
class ListApi(generics.ListCreateAPIView):
    serializer_class = serializers.TokenSerializer
    queryset = models.TokenModel.objects.all()
    # authentication_classes = []
    # permission_classes = []


class CategoriesList(generics.ListCreateAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Categories.objects.all()
    # authentication_classes = []
    # permission_classes = []
    filter_backends = DjangoFilterBackend
    filterset_fields=['c_name']


class DetailCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategorySerializer
    queryset = models.Categories.objects.all()


class ProductList(generics.ListCreateAPIView):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields=['name']
    # permission_classes = []
    # authentication_classes = []


class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ProductsSerializer
    queryset = models.Products.objects.all()


class ListCustomUser(generics.ListCreateAPIView):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = []
    authentication_classes = []


class DetailCustomUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MyUser.objects.all()
    serializer_class = serializers.UserSerializer
    
    

class SiteList(generics.ListCreateAPIView):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer
    # permission_classes = []
    # authentication_classes = []


class SiteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Site.objects.all()
    serializer_class = serializers.SiteSerializer
    
    
class ZakazList(generics.ListCreateAPIView):
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.ZakazSerializer
    # permission_classes = []
    # authentication_classes = []


class ZakazDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Zakaz.objects.all()
    serializer_class = serializers.Zakaz2Serializer


class Zakaz2List(generics.ListCreateAPIView):
    queryset = models.Zakaz2.objects.all()
    serializer_class = serializers.Zakaz2Serializer
    # permission_classes = []
    # authentication_classes = []


class Zakaz2Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Zakaz2.objects.all()
    serializer_class = serializers.Zakaz2Serializer

class KonsultatsiyaList(generics.ListCreateAPIView):
    queryset = models.Konsultatsiya.objects.all()
    serializer_class = serializers.KonsultatsiyaSerializer
    # permission_classes = []
    # authentication_classes = []

class KonsultatsiyaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Konsultatsiya.objects.all()
    serializer_class = serializers.KonsultatsiyaSerializer
    # permission_classes = []
    # authentication_classes = []