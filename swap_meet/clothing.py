from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, category= "Clothing", condition=float(0)):
        self.category = category
        self.condition = condition
    def __str__(self):
        return (f"The finest clothing you could wear.")

