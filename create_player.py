from Player import Player
from input_functions import safe_input

def create_player(player_type, input_func = safe_input, output_func = print):
    player = Player()
    if player_type["named"]:
        player.name = input_func("What would you like to call your character?")
    if player_type["has_age"]:
        player.age = input_func(f"How old is {player.name}")
    if player_type["has_gender"]:
        gender = input_func(f"What gender is {player.name}? (M/f/Other)")
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
            output_func(f"What class would you like {player.name} to be?")
            for n, c in enumerate(player_type["available_classes"]):
                output_func(f"{n+1}. {c.name}")
                output_func(c.info)
            player.bclass = player_type["available_classes"][input_func(int, "That's not a valid choice.", range(1, len(player_type["available_classes"])+1))]
        player.base_stats = player.bclass.stats
        player.stats = player.base_stats
        player.base_weapon = player.bclass.weapon
        player.weapon = player.base_weapon
        player.level = 1

    return player