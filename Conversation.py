import random
from utils import numbered_choice

# conversation class, instatiated for every conversation (a choice while speaking to an npc)
class Conversation:
    def __init__(self, obj):
        attribs = obj.attrib

        # set required attributes
        self.name = attribs["name"]
        self.type = attribs["type"]

        self.children = []
        self.children_names = []

        # instantiate children conversations and speeches
        for element in obj:
            if element.tag == "Conversation":
                self.children.append(Conversation(element))
                self.children_names.append(element.attrib["name"])
            elif element.tag == "Speech":
                self.children.append({"type" : "Speech", "text" : element.text})
            elif element.tag == "ConversationEnd":
                self.end = element
        
    # have the conversation
    def start(self):
        # procedural means speeches follow each other chronologically
        if self.type == "procedural":
            for child in self.children:
                if type(child) == dict:
                    print(child["text"])
        # random means a random speech is chosen and outputted
        elif self.type == "random":
            speeches = [child for child in self.children if type(child) == dict]
            print(random.choice(speeches)["text"])
        
        # if there is a further conversation to be had, offer the choices
        conversations = [child for child in self.children if type(child) == Conversation]
        if len(self.children_names) != 0:
            choice = conversations[numbered_choice(self.children_names, "", "Eh?")]
            # if the conversation has moved back sufficiently after hitting a stop, replay this convo, if not, keep going back
            back = choice.start()
            if back == 0:
                self.start()
            else:
                return back - 1
        else:
            # when a convo dead end is hit, move back however many steps specified
            return int(self.end.attrib["steps"]) - 1