from input_functions import safe_input, numbered_choice
from display_funcs import decorate
from Location import Location
from Feature import Feature

class Player():
    PRONOUNS = {"m": {"subj":"he", "obj":"him"},
                "f": {"subj":"she", "obj":"her"},
                "o": {"subj":"they", "obj":"them"}}

    def __init__(self, name=None, age=None, gender="o", combatable=False, stats={}):
        self.name = name
        self.age = age
        self.set_gender(gender)
        self.combatable = combatable
        if combatable:
            self.stats = stats
    
    def set_gender(self, gender):
        self.gender = gender.lower()
        self.pronouns = self.PRONOUNS[gender]
    
    def goto(self, l):
        if l.first_visit is None:
            l.first_visit = True
            l.output_func(l.get_fancy())
            l.output_func(l.long_desc)
            l.output_func(f"Welcome to {l.name}!")
        else:
            l.output_func(l.get_fancy())
            l.output_func(l.short_desc)
        self.enter(l)

    def enter(self, l):
        inp = numbered_choice("What/Who/Where would you like to interact with?", [s.name for s in l.contains], l.contains, l.input_func, l.output_func)
        if inp in ["I", "i"]:
            self.open_inventory()
        else:
            if type(inp) == Location:
                l.first_visit = False
                self.goto(inp)
            elif type(inp) == Feature:
                inp.interact()
                self.goto(l)

    def open_inventory(self):
        pass