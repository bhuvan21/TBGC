from Game import Game
from Location import Location
from Feature import Feature
from items import create_boost
from input_functions import safe_input

b = Location("Yew Village > Barn", "A small barn. (What were you expecting?)", "", level=1)

f = create_boost("Blueberries", "Berries which happen to be blue.", 50, "health", 20)
c = Feature("Yew Village > Bush", "It's a small bush with a rabbit poking its head out. It even has some blueberries", f)
d = Feature("Yew Village > Statue", "A statue of Joe Bell, this town's founder.")
e = Location("Yew Village > Adventurer's Guild", "[WIP] Guild where budding youngsters apply to become adventurers", "Adventurer's guilds can be found all across the world. Once you're a member of the guild, you can enjoy special perks, as well as apply for adventuring jobs.", level=1)


a = Location("Yew Village", "A small town in the middle of nowhere.", "Here lies Yew Village, a small town in the middle of nowhere. The nearest town from here is Eagleast, but it's a trek away. The only building of note in the town is a small adventurer's guild.", level=0, starting_location=True, contains=[b, c, d, e])



x = Game(game_type={"starting_cutscene":None,
                    "character_creation_method":None,
                    "input_func":safe_input,
                    "output_func":print,
                    "player_type": {"named":True,
                                    "has_age":True,
                                    "has_gender":True,
                                    "combatable":False}},
        locations = [a])

x.start()