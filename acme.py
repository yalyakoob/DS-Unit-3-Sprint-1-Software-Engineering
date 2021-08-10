import random


class Product:
    """Creating Product Class And Initializing Attributes"""

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """Method To Determine Product Stealability"""

        if self.price / self.weight < 0.5:
            return "Not so stealable..."
        elif self.price / self.weight >= 0.5:
            if self.price / self.weight < 1.0:
                return "Kinda stealable."
            else:
                return "Very stealable!"

    def explode(self):
        """Method To Determine What Will Happen To Product If Too Flammable"""

        if self.flammability * self.weight < 10:
            return "...fizzle"
        elif self.flammability * self.weight >= 10:
            if self.flammability * self.weight < 50:
                return "...boom!"
            else:
                return "...BABOOM!!"


class BoxingGlove(Product):
    """Subclass Of Product"""

    def __init__(self, name, price=10, weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        super().__init__(name=str(name), price=int(price), weight=int(weight),
                         flammability=float(flammability),
                         identifier=int(identifier))

    def explode(self):
        """Method To Determine What Will Happen To Product If Too Flammable"""

        return "...it's a glove."

    def punch(self):
        """Method To Determine Aftermath of Boxing Glove Punch"""

        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5:
            if self.weight < 15:
                return "Hey that hurt!"
            else:
                return "OUCH!"
