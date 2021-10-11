from collections import namedtuple


class Person:
    def __init__(self, name, race, health, mana, armor):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.armor = armor

    def __repr__(self):
        return f'{self.name} {self.race}'

    @staticmethod
    def function(number):
        result = number * 5
        return result


hero_1 = Person('Varick', 'black', 100, 20, 50)
print(hero_1.armor)
print(hero_1.function(21))


def function(number):
    result = number * 5
    return result


PersonNameTuple = namedtuple('PersonNameTuple', 'name, race, health, mana, armor, function')

hero_2 = PersonNameTuple('Fog', 'steam', 90, 21, 51, function)
print(hero_2)
print(hero_2.health)
print(hero_2.function(21))
print(type(hero_2))

hero_1.race = 'fox'
print(hero_1)

# hero_2.race = 'param'  # AttributeError: can't set attribute tuple!
hero_3 = hero_2._replace(race='elf')
print(hero_3.race)
