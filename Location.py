from input_functions import safe_input, numbered_choice
from display_funcs import decorate

class Location():
    def __init__(self, name, short_desc, long_desc, contains=[], level=0, starting_location=False, input_func=safe_input, output_func=print):
        self.name = name
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.contains = contains
        self.starting_location = starting_location
        self.level = level

        self.input_func = input_func
        self.output_func = output_func

        self.first_visit = None

        for l in self.contains:
            if type(l) == Location:
                l.contains.append(self)

    def enter(self):
        numbered_choice("What/Who/Where would you like to interact with?", [s.name for s in self.contains], self.contains, self.input_func, self.output_func).interact()
    
    def interact(self):
        self.output_func(self.name + " : " + self.short_desc)

    def get_fancy(self):
        return decorate(self)