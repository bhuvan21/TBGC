class Feature():
    def __init__(self, name, info, item_pickup=None):
        self.name = name
        self.info = info
        self.item_pickup = item_pickup
    
    def interact(self, output_func=print):
        output_func(self.info)
        if self.item_pickup is not None:
            return self.item_pickup