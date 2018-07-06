class Player():
    PRONOUNS = {"m": {"subj":"he", "obj":"him"},
                "f": {"subj":"she", "obj":"her"},
                "o": {"subj":"they", "obj":"them"}}

    def __init__(self, name = None, age = None, gender = None, combatable = False, stats = {}):
        self.name = name
        self.age = age
        self.set_gender(gender)
        self.combatable = combatable
        if combatable:
            self.stats = stats
    
    def set_gender(self, gender):
        self.gender = gender.lower()
        self.pronouns = self.PRONOUNS[gender]
