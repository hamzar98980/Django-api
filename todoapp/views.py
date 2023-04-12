from django.http import HttpResponse
from django.shortcuts import render
from todoapp.searializer import productseralizer
from todoapp.models import product
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView


# Create your views here.


class ListProductAPIView(ListAPIView):
    queryset = product.objects.all()
    serializer_class = productseralizer


class createProductAPIView(CreateAPIView):
    queryset = product.objects.all()
    serializer_class = productseralizer


class destroyProductAPIView(DestroyAPIView):
    queryset = product.objects.all()
    serializer_class = productseralizer


class updateProductAPIView(UpdateAPIView):
    queryset = product.objects.all()
    serializer_class = productseralizer


def myworld(request):
    return HttpResponse('hey user')
