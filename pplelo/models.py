from django.db import models





class Player(models.Model):
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.nickname

class Match(models.Model):
    match_id = models.CharField(max_length=100)
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2')
    player3 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player3')
    player4 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player4')
    player5 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player5')
    player6 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player6')
    player7 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player7')
    player8 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player8')
    player9 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player9')
    player10 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player10')

    def __str__(self):
        return self.match_id

class Statistic(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_statistic')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="match_statistic")
    name_opponents_team = models.CharField(max_length=40)
    game_map = models.CharField(max_length=40)
    game_result = models.CharField(max_length=20)
    match_id_string = models.CharField(max_length=100)
    nickname_player = models.CharField(max_length=40)
    kr = models.CharField(max_length=20)
    kd = models.CharField(max_length=20)
    kak = models.CharField(max_length=20)
    win = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.match} - {self.player}"

