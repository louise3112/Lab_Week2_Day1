class Team:
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        for player in self.players:
            if player == player_name:
                return True
        return False

    #Alternative approaches:
    # def has_player(self, player_name):
    #     return self.players.count(player_name) > 0

    # def has_player(self, player_name):
    #     return player_name in self.players

    def play_game(self, game_result):
        if game_result == True: #This could also be written as 'if game_result:' since game_result is boolean
            self.points += 3