from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import PlayerSerializer, MatchSerializer, StatisticSerializer
from .models import Player, Match, Statistic





class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('-id')
    serializer_class = PlayerSerializer
    http_method_names = ['get']


class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all().order_by('-id')
    serializer_class = MatchSerializer
    http_method_names = ['get']



class StatisticViewSet(APIView):

    serializer_class = StatisticSerializer

    def get_queryset(self):
        statistics = Statistic.objects.all().order_by('-id')
        return statistics
    
    def get(self, request, *args, **kwargs):
        try:
            nickname_player = request.query_params['nickname_player']
            if nickname_player != None:
                statistics = Statistic.objects.filter(nickname_player=nickname_player).order_by('-id')[:20]
                statistics_filter = reversed(statistics)
                serializer = StatisticSerializer(statistics_filter, many=True)
        except:
            statistics = self.get_queryset()
            serializer = StatisticSerializer(statistics, many=True)

        return Response(serializer.data)


    

    
