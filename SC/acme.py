import random


class Product:
    '''This is my Description.

    Maybe I should come back to this when I'm done?
    '''

    def __init__(self, name=None, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        steal_index = (self.price / self.weight)
        if steal_index < 0.5:
            return 'Not so stealable...'
        elif 0.5 <= steal_index < 1.0:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        boom = (self.flammability * self.weight)
        if boom < 10:
            return '...fizzle'
        else:
            return '...BABOOOOMMMm!!!!'


class BoxingGlove(Product):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, price=10, weight=10, flammability=0.5):
        super().__init__(name=name, price=price, weight=weight,
                         flammability=flammability)

    def explode(self):
        return 'Its a glove...'

    def punch(self):
        w = self.weight
        if w < 5:
            print('that tickles.')
        elif 5 <= w < 15:
            print('Hey that hurt!')
        else:
            print('ouchie')
