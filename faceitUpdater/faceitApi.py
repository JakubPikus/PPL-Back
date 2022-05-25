import requests
from pplelo.models import Player, Match, Statistic
from datetime import datetime


def _get_match_json():

    headers_dict = {'Authorization': 'Bearer d0f23c73-6216-44c3-bab7-8f458184a942'}
    past_matches_json = requests.get('https://open.faceit.com/data/v4/hubs/18d8cc72-e76a-43f0-bbd3-ca7cf48a6115/matches?type=past&offset=0&limit=100', headers=headers_dict)
    
    try:
        past_matches_json.raise_for_status()
        return past_matches_json.json()
    except:
        return None

def _get_statistic_json(match_id):

    headers_dict = {'Authorization': 'Bearer d0f23c73-6216-44c3-bab7-8f458184a942'}
    statistic_json = requests.get('https://open.faceit.com/data/v4/matches/' + match_id + '/stats', headers=headers_dict)
    
    try:
        statistic_json.raise_for_status()
        return statistic_json.json()['rounds']
    except:
        return None



    

def update_match():
    json = _get_match_json()
    if json is not None:
        try:

            past_matches = json['items']

            for past_match in past_matches:

                if Match.objects.filter(match_id=past_match['match_id']).exists():
                    pass

                else:

                    if past_match['status'] == "FINISHED":

                        players_array=[]

                        for player in past_match['teams']['faction1']['roster']:
                            
                            if Player.objects.filter(nickname=player['nickname']).exists():
                                players_array.append(Player.objects.get(nickname=player['nickname']))
                            else:
                                new_player = Player()
                                new_player.nickname = player['nickname']
                                new_player.save()
                                players_array.append(Player.objects.get(nickname=player['nickname']))
                                

                        for player in past_match['teams']['faction2']['roster']:
                            if Player.objects.filter(nickname=player['nickname']).exists():
                                players_array.append(Player.objects.get(nickname=player['nickname']))
                            else:
                                new_player = Player()
                                new_player.nickname = player['nickname']
                                new_player.save()
                                players_array.append(Player.objects.get(nickname=player['nickname']))
                        
                        new_match = Match()
                        new_match.match_id = past_match['match_id']
                        new_match.player1 = players_array[0]
                        new_match.player2 = players_array[1]
                        new_match.player3 = players_array[2]
                        new_match.player4 = players_array[3]
                        new_match.player5 = players_array[4]
                        new_match.player6 = players_array[5]
                        new_match.player7 = players_array[6]
                        new_match.player8 = players_array[7]
                        new_match.player9 = players_array[8]
                        new_match.player10 = players_array[9]
                        new_match.save()

                        statistics = _get_statistic_json(past_match['match_id'])

                        name_team1 = statistics[0]['teams'][0]['team_stats']['Team']
                        name_team2 = statistics[0]['teams'][1]['team_stats']['Team']
                        game_map = statistics[0]['round_stats']['Map']
                        game_result = statistics[0]['round_stats']['Score'].split(" / ")
                        match_id_string = statistics[0]['match_id']

                        for team in statistics[0]['teams']:
                            if team['team_stats']['Team'] == name_team1:
                                opponents_team = name_team2
                            else:
                                opponents_team = name_team1

                            for player_new_statistic in team['players']:
                                new_statistic = Statistic()
                                new_statistic.player = Player.objects.get(nickname=player_new_statistic['nickname'])
                                new_statistic.match = Match.objects.get(match_id=past_match['match_id']) 
                                new_statistic.kr = player_new_statistic['player_stats']['K/R Ratio']
                                new_statistic.kd = player_new_statistic['player_stats']['K/D Ratio']
                                new_statistic.kak = player_new_statistic['player_stats']['Kills'] + '/' + player_new_statistic['player_stats']['Assists'] + '/' + player_new_statistic['player_stats']['Deaths']
                                if player_new_statistic['player_stats']['Result'] == "1":
                                    new_statistic.win = "W"
                                    if int(game_result[0])/int(game_result[1]) > 1:
                                        new_statistic.game_result = game_result[0] + " / " + game_result[1]
                                    else:
                                        new_statistic.game_result = game_result[1] + " / " + game_result[0]

                                else:
                                    new_statistic.win = "L"
                                    if int(game_result[0])/int(game_result[1]) < 1:
                                        new_statistic.game_result = game_result[0] + " / " + game_result[1]
                                    else:
                                        new_statistic.game_result = game_result[1] + " / " + game_result[0]


                                new_statistic.name_opponents_team = "vs " + opponents_team
                                new_statistic.game_map = game_map
                                new_statistic.match_id_string = match_id_string
                                new_statistic.nickname_player= player_new_statistic['nickname']
                                
                                new_statistic.save()

        except:
            pass

        






   


