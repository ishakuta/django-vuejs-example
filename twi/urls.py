from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'tweets', views.TweetViewSet)


urlpatterns = [
    path('', views.index, name='tweets_index'),
    path('api/', include(router.urls))
]
