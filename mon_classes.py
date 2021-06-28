class Normal:
    super_effective = []
    effective = []
    not_very_effective = ['rock', 'steel']
    no_effect = ['ghost']
    super_effective_against = ['fighting']
    effective_against = []
    not_very_effective_against = []
    no_effect_against = ['ghost']

class Fighting:
    super_effective = ['normal', 'rock', 'steel', 'ice', 'dark']
    effective = []
    not_very_effective = ['flying', 'poison', 'bug', 'psychic', 'fairy']
    no_effect = ['ghost']
    super_effective_against = ['flying', 'psychic', 'fairy']
    effective_against = []
    not_very_effective_against = ['rock', 'bug', 'dark']
    no_effect_against = []

class Flying:
    super_effective = ['fighting', 'bug', 'grass']
    effective = []
    not_very_effective = ['rock', 'steel', 'electric']
    no_effect = []
    super_effective_against = ['rock', 'electric', 'ice']
    effective_against = []
    not_very_effective_against = ['fighting', 'bug', 'grass']
    no_effect_against = ['ground']

class Poison:
    super_effective = ['grass', 'fairy']
    effective = []
    not_very_effective = ['poison', 'ground', 'rock', 'ghost']
    no_effect = ['steel']
    super_effective_against = ['ground', 'psychic']
    effective_against = []
    not_very_effective_against = ['fighting', 'poison', 'bug', 'grass', 'fairy']
    no_effect_against = []


class Ground:
    super_effective = ['electric', 'fire', 'poison', 'rock', 'steel']
    effective = []
    not_very_effective = ['bug', 'grass']
    no_effect = ['flying']
    super_effective_against = ['grass', 'ice', 'water']
    effective_against = []
    not_very_effective_against = ['poison', 'rock']
    no_effect_against = ['electric']

class Rock:
    super_effective = ['bug', 'fire', 'flying', 'ice']
    effective = []
    not_very_effective = ['fighting', 'ground', 'steel']
    no_effect = []
    super_effective_against = ['fighting', 'grass', 'ground', 'steel', 'water']
    effective_against = []
    not_very_effective_against = ['fire', 'flying', 'normal', 'poison']
    no_effect_against = []

class Bug:
    super_effective = ['dark', 'grass', 'psychic']
    effective = []
    not_very_effective = ['fairy', 'fighting', 'fire', 'flying', 'ghost', 'poison', 'steel']
    no_effect = []
    super_effective_against = ['fire', 'flying', 'rock']
    effective_against = []
    not_very_effective_against = ['fighting', 'grass', 'ground']
    no_effect_against = []

class Ghost:
    super_effective = ['ghost', 'psychic']
    effective = []
    not_very_effective = ['dark', 'steel']
    no_effect = ['normal']
    super_effective_against = ['ghost', 'dark']
    effective_against = []
    not_very_effective_against = ['bug', 'poison']
    no_effect_against = ['normal', 'fighting']

class Steel:
    super_effective = ['fairy', 'ice', 'rock']
    effective = []
    not_very_effective = ['electric', 'fire', 'water', 'steel']
    no_effect = []
    super_effective_against = ['fighting', 'fire', 'ground']
    effective_against = []
    not_very_effective_against = ['bug', 'dragon', 'fairy', 'flying', 'grass', 'ice', 'normal', 'psychic', 'rock', 'steel']
    no_effect_against = ['poison']

class Fire:
    super_effective = ['bug', 'grass', 'ice', 'steel']
    effective = []
    not_very_effective = ['dragon', 'fire', 'rock', 'water']
    no_effect = []
    super_effective_against = ['ground', 'rock', 'water']
    effective_against = []
    not_very_effective_against = ['bug', 'fairy', 'fire', 'grass', 'ice', 'steel']
    no_effect_against = []

class Water:
    super_effective = ['fire', 'ground', 'rock']
    effective = []
    not_very_effective = ['dragon', 'grass', 'water']
    no_effect = []
    super_effective_against = ['electric', 'grass']
    effective_against = []
    not_very_effective_against = ['fire', 'ice', 'steel', 'water']
    no_effect_against = []

class Grass:
    super_effective = ['ground', 'rock', 'water']
    effective = []
    not_very_effective = ['bug', 'dragon', 'fire', 'flying', 'grass', 'poison', 'steel']
    no_effect = []
    super_effective_against = ['bug', 'fire', 'flying', 'ice', 'poison']
    effective_against = []
    not_very_effective_against = ['electric', 'grass', 'ground', 'water']
    no_effect_against = []

class Electric:
    super_effective = ['flying', 'water']
    effective = []
    not_very_effective = ['dragon', 'electric', 'grass']
    no_effect = ['ground']
    super_effective_against = ['ground']
    effective_against = []
    not_very_effective_against = ['electric', 'flying', 'steel']
    no_effect_against = []

class Psychic:
    super_effective = ['fighting', 'poison']
    effective = []
    not_very_effective = ['psychic', 'steel']
    no_effect = []
    super_effective_against = ['bug', 'dark', 'ghost']
    effective_against = []
    not_very_effective_against = ['fighting', 'psychic']
    no_effect_against = []

class Ice:
    super_effective = ['dragon', 'flying', 'grass', 'ground']
    effective = []
    not_very_effective = ['fire', 'ice', 'steel', 'water']
    no_effect = []
    super_effective_against = ['fighting', 'fire', 'rock', 'steel']
    effective_against = []
    not_very_effective_against = ['ice']
    no_effect_against = []

class Dragon:
    super_effective = ['dragon']
    effective = []
    not_very_effective = ['steel']
    no_effect = ['fairy']
    super_effective_against = ['dragon', 'fairy', 'ice']
    effective_against = []
    not_very_effective_against = ['electric', 'fire', 'grass', 'water']
    no_effect_against = []

class Dark:
    super_effective = ['ghost', 'psychic']
    effective = []
    not_very_effective = ['dark', 'fighting', 'fairy']
    no_effect = []
    super_effective_against = ['bug', 'fairy', 'fighting']
    effective_against = []
    not_very_effective_against = ['dark', 'ghost']
    no_effect_against = ['psychic']

class Fairy:
    super_effective = ['dark', 'dragon', 'fighting']
    effective = []
    not_very_effective = ['fire', 'poison', 'steel']
    no_effect = []
    super_effective_against = ['poison', 'steel']
    effective_against = []
    not_very_effective_against = ['bug', 'dark', 'fighting']
    no_effect_against = ['dragon']

class_list = [Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark, Fairy]
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

