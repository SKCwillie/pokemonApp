class Type:
    def __init__(self, super_effective, effective, not_very_effective, no_effect,
                 super_effective_against, effective_against, not_very_effective_against, no_effect_against):
        self.super_effective = super_effective
        self.effective = effective
        self.not_very_effective = not_very_effective
        self.no_effect = no_effect
        self.super_effective_against = super_effective_against
        self.effective_against = effective_against
        self.not_very_effective_against = not_very_effective_against
        self.no_effect_against = no_effect_against

normal = Type([],
              [],
              ['rock', 'steel'],
              ['ghost'],
              ['fighting'],
              [],
              [],
              ['ghost'])

fighting = Type(['normal', 'rock', 'steel', 'ice', 'dark'],
                [],
                ['flying', 'poison', 'bug', 'psychic', 'fairy'],
                ['ghost'],
                ['flying', 'psychic', 'fairy'],
                [],
                ['rock', 'bug', 'dark'],
                [])

flying = Type(['fighting', 'bug', 'grass'],
              [],
              ['rock', 'steel', 'electric'],
              [],
              ['rock', 'electric', 'ice'],
              [],
              ['fighting', 'bug', 'grass'],
              ['ground'])

poison = Type(['grass', 'fairy'],
              [],
              ['poison', 'ground', 'rock', 'ghost'],
              ['steel'],
              ['ground', 'psychic'],
              [],
              ['fighting', 'poison', 'bug', 'grass', 'fairy'],
              [])


ground = Type(['electric', 'fire', 'poison', 'rock', 'steel'],
              [],
              ['bug', 'grass'],
              ['flying'],
              ['grass', 'ice', 'water'],
              [],
              ['poison', 'rock'],
              ['electric'])

rock = Type(['bug', 'fire', 'flying', 'ice'],
            [],
            ['fighting', 'ground', 'steel'],
            [],
            ['fighting', 'grass', 'ground', 'steel', 'water'],
            [],
            ['fire', 'flying', 'normal', 'poison'],
            [])

bug = Type(['dark', 'grass', 'psychic'],
           [],
           ['fairy', 'fighting', 'fire', 'flying', 'ghost', 'poison', 'steel'],
           [],
           ['fire', 'flying', 'rock'],
           [],
           ['fighting', 'grass', 'ground'],
           [])

ghost = Type(['ghost', 'psychic'],
             [],
             ['dark', 'steel'],
             ['normal'],
             ['ghost', 'dark'],
             [],
             ['bug', 'poison'],
             ['normal', 'fighting'])

steel = Type(['fairy', 'ice', 'rock'],
             [],
             ['electric', 'fire', 'water', 'steel'],
             [],
             ['fighting', 'fire', 'ground'],
             [],
             ['bug', 'dragon', 'fairy', 'flying', 'grass', 'ice', 'normal', 'psychic', 'rock', 'steel'],
             ['poison'])

fire = Type(['bug', 'grass', 'ice', 'steel'],
            [],
            ['dragon', 'fire', 'rock', 'water'],
            [],
            ['ground', 'rock', 'water'],
            [],
            ['bug', 'fairy', 'fire', 'grass', 'ice', 'steel'],
            [])

water = Type(['fire', 'ground', 'rock'],
             [],
             ['dragon', 'grass', 'water'],
             [],
             ['electric', 'grass'],
             [],
             ['fire', 'ice', 'steel', 'water'],
             [])

grass = Type(['ground', 'rock', 'water'],
             [],
             ['bug', 'dragon', 'fire', 'flying', 'grass', 'poison', 'steel'],
             [],
             ['bug', 'fire', 'flying', 'ice', 'poison'],
             [],
             ['electric', 'grass', 'ground', 'water'],
             [])

electric = Type(['flying', 'water'],
                [],
                ['dragon', 'electric', 'grass'],
                ['ground'],
                ['ground'],
                [],
                ['electric', 'flying', 'steel'],
                [])

psychic = Type(['fighting', 'poison'],
               [],
               ['psychic', 'steel'],
               [],
               ['bug', 'dark', 'ghost'],
               [],
               ['fighting', 'psychic'],
               [])

ice = Type(['dragon', 'flying', 'grass', 'ground'],
           [],
           ['fire', 'ice', 'steel', 'water'],
           [],
           ['fighting', 'fire', 'rock', 'steel'],
           [],
           ['ice'],
           [])

dragon = Type(['dragon'],
              [],
              ['steel'],
              ['fairy'],
              ['dragon', 'fairy', 'ice'],
              [],
              ['electric', 'fire', 'grass', 'water'],
              [])

dark = Type(['ghost', 'psychic'],
            [],
            ['dark', 'fighting', 'fairy'],
            [],
            ['bug', 'fairy', 'fighting'],
            [],
            ['dark', 'ghost'],
            ['psychic'])

fairy = Type(['dark', 'dragon', 'fighting'],
             [],
             ['fire', 'poison', 'steel'],
             [],
             ['poison', 'steel'],
             [],
             ['bug', 'dark', 'fighting'],
             ['dragon'])

class_list = [normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water,
              grass, electric, psychic, ice, dragon, dark, fairy]
mon_types = ('normal', 'fighting', 'flying', 'poison', 'ground', 'rock', 'bug', 'ghost', 'steel', 'fire', 'water', 'grass', 'electric', 'psychic', 'ice', 'dragon', 'dark', 'fairy')

for i in class_list:
    for j in mon_types:
        if (j not in i.super_effective and j not in i.not_very_effective and j not in i.no_effect):
            i.effective.append(j)
        if (j not in i.super_effective_against and j not in i.not_very_effective_against and j not in i.no_effect_against):
            i.effective_against.append(j)

mon_types_dict = {}
count = 0

for i in mon_types:
    mon_types_dict[i] = class_list[count]
    count += 1

