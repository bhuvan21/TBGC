from utils import numbered_choice
import NPC

# Location class, instantiated for every location in the game
class Location:

    def __init__(self, obj):
        attribs = obj.attrib
        
        # set requried attributes
        self.name = attribs["name"]
        self.shortdesc = attribs["shortdesc"]

        # set unrequired attributes
        self.longdesc = attribs["longdesc"] if "longdesc" in attribs.keys() else self.shortdesc

        self.visit_count = 0
        self.children = []
        self.children_names = []

        # instantiate children locations, npcs and features
        for element in obj:
            if element.tag == "Location":
                self.children.append(Location(element))
                self.children_names.append(element.attrib["name"])
            elif element.tag == "Feature":
                # features are simply objects that can be interacted with and nothing more
                self.children_names.append(element.attrib["name"])
                self.children.append({"name" : element.attrib["name"], "text" : element.text, "type" : "Feature"})
            elif element.tag == "NPC":
                self.children.append(NPC.NPC(element))
                self.children_names.append(element.attrib["name"])

        # add each parent to the child's options so you can go back from a location or NPC
        for child in self.children:
            if type(child) == Location or type(child) == NPC.NPC:
                child.children_names.append(self.name)
                child.children.append(self)
    
    # goto the location, offer user children choices
    def goto(self):
        # print long desc if first visit
        self.visit_count += 1
        if self.visit_count <= 1:
            print(self.longdesc)
        else:
            print(self.shortdesc)
        
        # TODO MAKE THE PROMPTS CUSTOMISABLE FROM THE XML
        choice = self.children[numbered_choice(self.children_names, "Choose something", "CHOOSE SOMETHING")]
        if type(choice) == Location:
            choice.goto()
        elif type(choice) == dict:
            if choice["type"] == "Feature":
                print(choice["text"])
        elif type(choice) == NPC.NPC:
            choice.visit()
            
        self.goto() 