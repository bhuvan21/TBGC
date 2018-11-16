from input_functions import safe_input, numbered_choice
from display_funcs import decorate
from Location import Location
from Feature import Feature

from copy import deepcopy

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
        
        self.inventory = []
        self.inventory_size = 20

        self.input_func = input
        self.output_func = print
    
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
            self.goto(l)
        else:
            if type(inp) == Location:
                l.first_visit = False
                self.goto(inp)
            elif type(inp) == Feature:
                item = inp.interact()
                if item is not None:
                    if self.input_func(str, f"Would you like to pick up {item['name']}? (Y/n)", "That's not an option.", ["y", "Y", "n", "N"]).lower() == "y":
                        self.add_to_inventory(item)
                self.goto(l)

    def open_inventory(self):
        if len(self.inventory) == 0:
            self.output_func("Your inventory is empty.")
            return
        self.output_func("Here is your inventory:")
        inp = numbered_choice("What item would you like to look at? (number to select or q to quit)", [i["name"] for i in self.inventory], self.inventory, input_func=self.input_func, other_commands=["q", "Q"])
        if inp in ["q", "Q"]:
            return
        self.inspect_item(inp)
        self.open_inventory()

    def inspect_item(self, item):
        self.output_func(f"{item['name']} x{item['count']}")
        self.output_func(item["desc"])
        self.output_func(f"Costs {item['cost']}, Sells for {item['resell']}")
        self.output_func("Additional Information:")
        for k, v in item.items():
            if k not in ["name", "desc", "cost", "resell", "count"]:
                self.output_func(f"{k.replace('_', ' ').capitalize()} : {v}")
        
    def add_to_inventory(self, item):
        count = item.pop("count")
        for i in self.inventory:     
            count2 = i.pop("count")
            if i == item:
                if count + count2 <= item["max_stack"]:
                    self.output_func(f"{item['name']} x{count} has been added to your inventory.")
                    i["count"] = count + count2
                    return
                else:
                    if not(len(self.inventory) + 1 <= self.inventory_size):
                        self.output_func("Your inventory is full!")
                        return

        if len(self.inventory) + 1 <= self.inventory_size:
            self.output_func(f"{item['name']} x{count} has been added to your inventory.")
            item["count"] = count
            self.inventory.append(deepcopy(item))
            

        
