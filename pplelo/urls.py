from django.urls import include, path
from django.urls import re_path as url
from rest_framework import routers
from .views import PlayerViewSet, MatchViewSet, StatisticViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'players', PlayerViewSet)
router.register(r'matches', MatchViewSet)




urlpatterns = [
    path('api/', include(router.urls)),
    path('api/statistics/', views.StatisticViewSet.as_view(), name='statistics'),
]