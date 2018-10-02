from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse
from .serializers import TweetSerializer
from .models import Tweet


def index(request):
    return HttpResponse("Hello, world. You're at the twi index.")


class TweetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tweets to be viewed or edited.
    """
    queryset = Tweet.objects.all().order_by('-published_at')
    serializer_class = TweetSerializer
