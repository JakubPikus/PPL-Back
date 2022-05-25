from .models import Player, Match, Statistic
from rest_framework import serializers



class PlayerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Player
        fields = ['id','nickname',]



class MatchSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Match
        fields = ['id','match_id','player1','player2','player3','player4','player5','player6','player7','player8','player9','player10',]



class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = ['id','player','match','kr','kd','kak','win','name_opponents_team','game_map','game_result','match_id_string','nickname_player',]