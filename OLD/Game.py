from create_player import create_player


class Game():
    def __init__(self, game_type, locations, player=None):
        self.player = player
        if game_type["starting_cutscene"] != None:
            game_type["starting_cutscene"]()
        if self.player is None:
            if game_type["character_creation_method"] == None:
                self.player = create_player(game_type["player_type"], game_type["input_func"])
            else:
                self.player = game_type["character_creation_method"]()
        self.player.input_func = game_type["input_func"]
        self.player.output_func = game_type["output_func"]
        self.locations = locations
        
    def start(self):
        for l in self.locations:
            if l.starting_location:
                self.player.goto(l)
        