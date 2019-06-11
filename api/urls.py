from django.urls import path, include
from .views import *
from newsapp.models import *
from rest_framework import routers




router = routers.DefaultRouter()


router.register('tag', TagAPIView)
router.register('category', CategoryAPIView)
router.register('topic', TopicAPIView)
router.register('news', NewsAPIView)





urlpatterns = [
   path('', include(router.urls)),
]
