from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView
from images.models import Image
from .serializers import ImageSerializer
from django.http import Http404

import random

def get_ids():
    return Image.objects.values_list('id', flat=True)

def pick_random_object(objects):
    return random.choice(objects).id

class AllImageAPIView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageAPIView(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class RandomImageAPIView(ListAPIView):
    def get_queryset(self):
        ids = get_ids()
        return Image.objects.filter(id=random.choice(ids))
    serializer_class = ImageSerializer

class RandomExcludeAPIView(ListAPIView):
    def get_queryset(self):
        params = self.kwargs['params']
        
        params = map(int, (params.split('+')))
        params = set(params)

        ids = list(set(get_ids()) - params)

        if not ids:
            raise Http404

        return Image.objects.filter(id=random.choice(ids))

    serializer_class = ImageSerializer
    
