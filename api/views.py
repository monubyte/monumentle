from django.shortcuts import render, redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
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

class RandomImageAPIView(RetrieveAPIView):
    def get(self, request):
        ids = get_ids()
        image = Image.objects.get(id=random.choice(ids))

        return Response(ImageSerializer(image).data)

class RandomExcludeAPIView(RetrieveAPIView):
    def get(self, request, params):
        params = self.kwargs['params']
        
        params = map(int, (params.split('+')))
        params = set(params)

        ids = list(set(get_ids()) - params)

        if not ids:
            raise Http404

        image = Image.objects.get(id=random.choice(ids))

        return Response(ImageSerializer(image).data)


    # serializer_class = ImageSerializer
    
