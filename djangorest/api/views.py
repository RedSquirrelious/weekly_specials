from django.shortcuts import render
from rest_framework import generics
from .serializers import MarketSerializer
from .models import Market


class CreateView(generics.ListCreateAPIView):
    '''defines behavior for api'''
    queryset = Market.objects.all()
    serializer_class = MarketSerializer

    def perform_create(self, serializer):
        '''save post when creating market'''
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer