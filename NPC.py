from utils import numbered_choice
import Location
from Conversation import Conversation

# Location class, instantiated for every location in the game
class NPC:
    def __init__(self, obj):
        attribs = obj.attrib
        
        # set requried attributes
        self.name = attribs["name"]
        self.intro = attribs["intro"]

        self.children = []
        self.children_names = []

        # instantiate children conversations
        for element in obj:
            if element.tag == "Conversation":
                self.children.append(Conversation(element))
                self.children_names.append(element.attrib["name"])

    # initiate talking with an npc
    def visit(self):
        # TODO MAKE THE REPROMPT SPECIFIABLE
        choice = self.children[numbered_choice(self.children_names, self.intro, "Eh?")]
        if type(choice) == Conversation:
            choice.start()
            self.visit()
        elif type(choice) == Location.Location:
            choice.goto()