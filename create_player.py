from Player import Player
from input_functions import safe_input, numbered_choice


def create_player(player_type, input_func=safe_input, output_func=print):
    player = Player()
    if player_type["named"]:
        player.name = input_func(str, "What would you like to call your character? ")
    if player_type["has_age"]:
        player.age = input_func(int, f"How old is {player.name}? ", "That's not a valid age ")
    if player_type["has_gender"]:
        gender = input_func(str, f"What gender is {player.name}? (M/f/Other) ", "That's not a valid option.", ["m", "M", "f", "F", "o", "O"])
        if gender.lower() in ["male", "m"]:
            player.set_gender("m")
        elif gender.lower() in ["female", "f"]:
            player.set_gender("f")
        else:
            player.set_gender("o")
    
    player.combatable = player_type["combatable"]
    if player.combatable:
        if player_type["custom_class"] != None:
            player.bclass = player_type["custom_class"]
        else:
            numbered_choice("Choose from the following classes:", [c.name for c in player_type["available_classes"]], player_type["available_classes"], input_func, output_func)
        player.base_stats = player.bclass.stats
        player.stats = player.base_stats
        player.base_weapon = player.bclass.weapon
        player.weapon = player.base_weapon
        player.level = 1
    return player